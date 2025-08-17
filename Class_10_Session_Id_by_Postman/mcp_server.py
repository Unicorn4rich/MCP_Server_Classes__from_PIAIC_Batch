from mcp.server.fastmcp import FastMCP


# MCP server mein kuch options aisy haiiin jo False karne se milty hain or False -> karne se yadash/memory milti hai server ko
app = FastMCP(name="my_mcp", stateless_http=False) # statless/statefull => stateless_http=True -> Direct  jwab dega. and stateless_http=False -> required (1. initialize) (2. get session id) (3. notification)
#----------------------------------------------------------------

@app.tool()
def hello_function():
    return "hellooooooooooooooooo"



#----------------------------------------------------------------
mcp_app = app.streamable_http_app()