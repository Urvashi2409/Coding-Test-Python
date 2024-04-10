from app.models.models import Post
from app.db import Session

class PostService:
    """
    Service class for Post operations.
    """

    @staticmethod
    def create_post(post_data, user_id):
        """
        Create a new post.
        """
        session = Session()
        post = Post(text=post_data.text, user_id=user_id)
        session.add(post)
        session.commit()
        session.refresh(post)
        session.close()
        return post

    @staticmethod
    def get_posts(user_id):
        """
        Get all posts of a user.
        """
        session = Session()
        posts = session.query(Post).filter(Post.user_id == user_id).all()
        session.close()
        return posts

    @staticmethod
    def delete_post(post_id, user_id):
        """
        Delete a post.
        """
        session = Session()
        post = session.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
        if not post:
            session.close()
            return False
        session.delete(post)
        session.commit()
        session.close()
        return True
