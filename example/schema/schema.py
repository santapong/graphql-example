# schema.py
import graphene

# In-memory data storage for demonstration purposes
books_data = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
]

# Define the Book type
class Book(graphene.ObjectType):
    id = graphene.Int()
    title = graphene.String()
    author = graphene.String()

# Define the Query type
class Query(graphene.ObjectType):
    all_books = graphene.List(Book)
    book_by_id = graphene.Field(Book, id=graphene.Int(required=True))

    def resolve_all_books(root, info):
        return books_data

    def resolve_book_by_id(root, info, id):
        for book in books_data:
            if book["id"] == id:
                return book
        return None

# Define the Mutation type
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)

    book = graphene.Field(Book)

    def mutate(root, info, title, author):
        new_id = max(book["id"] for book in books_data) + 1 if books_data else 1
        new_book = {"id": new_id, "title": title, "author": author}
        books_data.append(new_book)
        return CreateBook(book=new_book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

# Create the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
