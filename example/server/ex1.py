import os, sys
sys.path.append('/'.join([os.getcwd(),'example']))

# main.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse

from schema import schema  # Import the schema defined earlier

import graphene
import uvicorn

app = FastAPI()

@app.post("/graphql")
async def graphql_endpoint(request: Request):
    try:
        # Parse the incoming JSON request
        data = await request.json()
        query = data.get("query")
        variables = data.get("variables")
        operation_name = data.get("operationName")

        if not query:
            raise HTTPException(status_code=400, detail="No query found in the request.")

        # Execute the GraphQL query
        result = schema.execute(
            query,
            variable_values=variables,
            operation_name=operation_name,
        )

        # Prepare the response
        response = {}
        if result.errors:
            response["errors"] = [str(error) for error in result.errors]
        if result.data:
            response["data"] = result.data

        return JSONResponse(response)

    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail=str(e))

# Optional: Serve GraphiQL interface
@app.get("/graphiql", response_class=HTMLResponse)
async def graphiql():
    html_content = """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <title>GraphiQL</title>
        <link href="https://unpkg.com/graphiql/graphiql.min.css" rel="stylesheet" />
        <script
          crossorigin
          src="https://unpkg.com/react/umd/react.production.min.js"
        ></script>
        <script
          crossorigin
          src="https://unpkg.com/react-dom/umd/react-dom.production.min.js"
        ></script>
        <script
          crossorigin
          src="https://unpkg.com/graphiql/graphiql.min.js"
        ></script>
      </head>
      <body style="margin: 0; overflow: hidden;">
        <div id="graphiql" style="height: 100vh;"></div>
        <script>
          const graphQLFetcher = graphQLParams =>
            fetch('/graphql', {
              method: 'post',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(graphQLParams),
            })
              .then(response => response.json())
              .catch(() => response.json());

          ReactDOM.render(
            React.createElement(GraphiQL, { fetcher: graphQLFetcher }),
            document.getElementById('graphiql'),
          );
        </script>
      </body>
    </html>
    """
    return HTMLResponse(content=html_content)

if __name__ == '__main__':
    uvicorn.run('ex1:app',port=800, reload=True)