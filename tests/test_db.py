import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

# Use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()
    
    def test_timeline_post(self):
        # Create 2 timeline posts and check if the id is auto-incremeneted
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
        
        # Get the posts in order that they were created to test
        created_posts = list(TimelinePost.select().order_by(TimelinePost.id))
        
        # Check the details of the first post
        self.assertEqual(created_posts[0].name, 'John Doe')
        self.assertEqual(created_posts[0].email, 'john@example.com')
        self.assertEqual(created_posts[0].content, 'Hello world, I\'m John!')

        # Check the details of the second post
        self.assertEqual(created_posts[1].name, 'Jane Doe')
        self.assertEqual(created_posts[1].email, 'jane@example.com')
        self.assertEqual(created_posts[1].content, 'Hello world, I\'m Jane!')

        
if __name__ == '__main__':
    unittest.main()