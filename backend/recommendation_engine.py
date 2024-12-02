import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy.orm import Session
from .models import Program, User

class RecommendationEngine:
    def __init__(self, db: Session):
        self.db = db
        self.update_recommendation_matrix()
    
    def update_recommendation_matrix(self):
        # Fetch all programs and convert to DataFrame
        programs = self.db.query(Program).all()
        program_df = pd.DataFrame([
            {
                'id': p.id, 
                'title': p.title, 
                'categories': ' '.join(p.categories or []),
                'description': p.description or ''
            } for p in programs
        ])
        
        # Combine features for recommendation
        program_df['content'] = program_df['title'] + ' ' + program_df['categories'] + ' ' + program_df['description']
        
        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(program_df['content'])
        self.similarity_matrix = cosine_similarity(tfidf_matrix)
        self.program_df = program_df
    
    def get_recommendations(self, user: User, num_recommendations: int = 5):
        # Consider user's liked programs and interest tags
        liked_program_ids = [like.program_id for like in user.liked_programs]
        
        # If no liked programs, recommend based on interest tags
        if not liked_program_ids:
            return self._recommend_by_tags(user, num_recommendations)
        
        # Calculate recommendations based on similar programs to liked ones
        scores = np.zeros(len(self.program_df))
        for program_id in liked_program_ids:
            idx = self.program_df[self.program_df['id'] == program_id].index[0]
            scores += self.similarity_matrix[idx]
        
        # Sort and get top recommendations
        top_indices = scores.argsort()[::-1][:num_recommendations]
        recommended_program_ids = self.program_df.iloc[top_indices]['id'].tolist()
        
        return recommended_program_ids
    
    def _recommend_by_tags(self, user: User, num_recommendations: int = 5):
        # If user has interest tags, recommend based on those
        if user.interest_tags:
            tag_scores = np.zeros(len(self.program_df))
            for tag in user.interest_tags:
                tag_mask = self.program_df['categories'].str.contains(tag, case=False)
                tag_indices = self.program_df[tag_mask].index
                tag_scores[tag_indices] += 1
            
            top_indices = tag_scores.argsort()[::-1][:num_recommendations]
            return self.program_df.iloc[top_indices]['id'].tolist()
        
        # Fallback to most recent programs
        return self.db.query(Program.id).order_by(Program.date_time.desc()).limit(num_recommendations).all()
