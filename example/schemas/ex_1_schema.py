import graphene
from graphene import ObjectType, String, Int, List, Field
from graphene.types import Mutation

# In-memory data storage
users = []

# Define the User type
class User(ObjectType):
    id = Int()
    name = String()
    age = Int()

# Define the Query
class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    users = List(User)

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_users(root, info):
        return users

# Define the CreateUser mutation
class CreateUser(Mutation):
    class Arguments:
        name = String(required=True)
        age = Int(required=True)

    user = Field(lambda: User)

    def mutate(root, info, name, age):
        user = User(id=len(users) + 1, name=name, age=age)
        users.append(user)
        return CreateUser(user=user)

# Define the Mutation
class Mutation(ObjectType):
    create_user = CreateUser.Field()

# Create the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
