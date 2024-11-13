# Example 2
# Learning about how to use CRUD consept of Graphql using python.
from graphene import ObjectType, Int, List, Field, String
from graphene.types import Mutation

from database import SessionLocal, engine, UserModel

# Define User Type for Schema Definition Languagues (SDLs). 
class User(ObjectType):
    id = Int()
    name = String()
    age = Int()


# Define for query data from graphql with fastAPI.
# R: Read
class Query(ObjectType):

# TODO: Make it right.

    def resolve_all(root):
        return SessionLocal.query(UserModel).all()
    

# Defind for Update data from graphql with fastAPI.
# U: Update
class UpdateUser(ObjectType):
    
# TODO: Make it can use with FastAPI    
    class