from app.models.models import User
from app.db import Session

class UserService:
    """
    Service class for User operations.
    """

    @staticmethod
    def create_user(user_data):
        """
        Create a new user.
        """
        session = Session()
        user = User(email=user_data.email, password=user_data.password)
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return user

    @staticmethod
    def authenticate_user(email, password):
        """
        Authenticate user based on email and password.
        """
        session = Session()
        user = session.query(User).filter(User.email == email, User.password == password).first()
        session.close()
        return user
