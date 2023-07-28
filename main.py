'''
Created on July 28, 2023

@author: Surya Pugal

source:
    # https://vegibit.com/interacting-with-a-database-using-sqlalchemy-crud-operations/
    # https://www.youtube.com/watch?v=0RqfzBRDWtk
    
'''


from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///example.db', echo=True)
# print(engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    
Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# create
def create_user(name, email):
    new_user = User(name=name, email=email)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(new_user)
    session.commit()
    session.close()

# create more users
def create_more_user(users):
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all(users)
    session.commit()
    session.close()
    
# Read
def get_user_by_id(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    session.close()
    return user

# retrieve all data
def get_all_users():
    Session = sessionmaker(bind=engine)
    session = Session()
    users = session.query(User).all()
    session.close()
    return users

# Update
def update_user(user_id, new_name, new_email):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.name = new_name
        user.email = new_email
        session.commit()
    session.close()
    
    # Delete
def delete_user(user_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()

    
    
if __name__ == "__main__":
    # Create and insert a new user
    # create_user("John Doe", "john.doe@example.com")
    
    # user1 = User(name = "Sam Smith", email = "sam.smith@example.com")
    # user2 = User(name = "John Anderson", email = "john.anderson@example.com")
     
    # create_more_user([user1, user2])
    
    # Retrieve and print the user
    # user = get_user_by_id(2)
    # if user:
    #     print(f"User ID: {user.id}, Name: {user.name}, Email: {user.email}")
    
    # retrieve all
    # users = get_all_users()
    
    # for user in users:
    #     print(f"USer ID:{user.id}")
    #     print(f"USer name:{user.name}")
    #     print(f"USer email:{user.email}")
    #     print(f"{user.id}, {user.name}, {user.email}")
    
     # Update the user
    # update_user(1, "Jane Smith", "jane.smith@example.com")



  # Delete the user
    delete_user(1)
    
    # Check if the user still exists
    user = get_user_by_id(1)
    if not user:
        print("User does not exist.")