# Example 1

import requests

url = 'http://localhost:8001/graphql'
mutation = '''
mutation CreateUser($name: String!, $age: Int!) {
  createUser(name: $name, age: $age) {
    user {
      id
      name
      age
    }
  }
}
'''
variables = {
    "name": "Bob",
    "age": 25
}

response = requests.post(url, json={'query': mutation, 'variables': variables})
print(response.json())
