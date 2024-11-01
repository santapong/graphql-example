"""
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