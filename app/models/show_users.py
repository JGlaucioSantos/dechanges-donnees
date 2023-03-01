from models import User
from models import CreateSession

session = CreateSession.create_session()

# query users

users = session.query(User).all()
for user in users:
    print(user.email, user.password)