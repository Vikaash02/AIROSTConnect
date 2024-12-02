{% extends "base.html" %}

{% block content %}
<div class="admin-dashboard">
    <h1>Admin Dashboard</h1>
    
    <section class="upload-program">
        <h2>Upload New Program</h2>
        <form id="upload-program-form">
            <div>
                <label>Title:</label>
                <input type="text" name="title" required>
            </div>
            <div>
                <label>Platform:</label>
                <select name="platform">
                    <option value="online">Online</option>
                    <option value="f2f">Face-to-Face</option>
                </select>
            </div>
            <div>
                <label>Date and Time:</label>
                <input type="datetime-local" name="date_time" required>
            </div>
            <div>
                <label>Registration Method:</label>
                <input type="text" name="registration_method">
            </div>
            <div>
                <label>Categories:</label>
                <input type="text" name="categories" placeholder="Comma-separated tags">
            </div>
            <div>
                <label>Description:</label>
                <textarea name="description"></textarea>
            </div>
            <button type="submit">Upload Program</button>
        </form>
    </section>

    <section class="program-list">
        <h2>Existing Programs</h2>
        <table id="programs-table">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Platform</th>
                    <th>Date</th>
                    <th>Categories</th>
                </tr>
            </thead>
            <tbody>
                <!-- Programs will be dynamically populated -->
            </tbody>
        </table>
    </section>
</div>
{% endblock %}
