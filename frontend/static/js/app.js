document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const googleLoginBtn = document.getElementById('google-login-btn');

    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = loginForm.email.value;
            const password = loginForm.password.value;

            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();
                if (response.ok) {
                    localStorage.setItem('token', data.access_token);
                    window.location.href = '/dashboard';
                } else {
                    alert(data.detail || 'Login failed');
                }
            } catch (error) {
                console.error('Login error:', error);
            }
        });
    }

    if (googleLoginBtn) {
        googleLoginBtn.addEventListener('click', () => {
            // Implement Google OAuth login flow
            // This will typically involve redirecting to Google's OAuth endpoint
        });
    }
});
