import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, TimelinePost

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        # Clean up the database before each test
        TimelinePost.delete().execute()
        
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Ximena Vazquez Mellado</title>" in html
        assert '<a href="/#about-me">' in html  # Check for specific link
    
    def test_timeline(self):
        # Response of getting a timeline post - when nothing is added yet
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        
    def test_post_timeline_post(self):
        # Test adding timeline posts
        post_response = self.client.post("/api/timeline_post", data={
                "name": "Test Name",
                "email" : "test.name@gmail.com",
                "content" : "This is a test post"
        })
        assert post_response.status_code == 200
        post_json = post_response.get_json()
        assert post_json["name"] == "Test Name"
        assert post_json["email"] == "test.name@gmail.com"
        assert post_json["content"] == "This is a test post"
        
    def test_post_and_get_timeline_posts(self):
        # Add multiple timeline posts
        self.client.post("/api/timeline_post", data={
            "name": "First Post",
            "email": "first@example.com",
            "content": "First post content"
        })
        self.client.post("/api/timeline_post", data={
            "name": "Second Post",
            "email": "second@example.com",
            "content": "Second post content"
        })

        # Retrieve the timeline posts
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json_response = response.get_json()
        assert "timeline_posts" in json_response
        assert len(json_response["timeline_posts"]) == 2
        
        # Verify posts exist and that ids are auto-incremeneted
        first_post = json_response["timeline_posts"][1]
        assert first_post["name"] == "First Post"
        assert first_post["email"] == "first@example.com"
        assert first_post["content"] == "First post content"
        
        second_post = json_response["timeline_posts"][0]
        assert second_post["name"] == "Second Post"
        assert second_post["email"] == "second@example.com"
        assert second_post["content"] == "Second post content"

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline Posts</title>" in html
        assert '<form id="timeline-form"' in html 
        
        