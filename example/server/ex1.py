from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from graphene import Schema
from schemas.ex_1_schema import schema  # Import the Graphene schema
import json
from starlette.responses import HTMLResponse

app = FastAPI()

# GraphQL endpoint
@app.post("/graphql")
async def graphql_endpoint(request: Request):
    data = await request.json()
    success, result = await graphql_handler(data)
    status_code = 200 if success else 400
    return JSONResponse(status_code=status_code, content=result)

@app.get("/graphql")
async def graphql_playground():
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <title>GraphQL Playground</title>
        <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/graphql-playground-react@1.7.20/build/static/css/index.css"
        />
        <link rel="shortcut icon" href="https://cdn.jsdelivr.net/npm/graphql-playground-react@1.7.20/build/favicon.png" />
        <script src="https://cdn.jsdelivr.net/npm/graphql-playground-react@1.7.20/build/static/js/middleware.js"></script>
      </head>
      <body>
        <div id="root"></div>
        <script>
          window.addEventListener('load', function() {
            GraphQLPlayground.init(document.getElementById('root'), {
              endpoint: '/graphql'
            })
          })
        </script>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

async def graphql_handler(data):
    try:
        query = data.get("query")
        variables = data.get("variables")
        operation_name = data.get("operationName")
        result = await schema.execute_async(query, variable_values=variables, operation_name=operation_name)
        response = {}
        if result.errors:
            response["errors"] = [str(error) for error in result.errors]
            success = False
        if result.data:
            response["data"] = result.data
            success = True
        return success, response
    except Exception as e:
        return False, {"errors": [str(e)]}
