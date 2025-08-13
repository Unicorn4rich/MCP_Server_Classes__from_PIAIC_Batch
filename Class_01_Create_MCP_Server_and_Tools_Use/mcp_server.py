# Ye file Server hai hmara
from mcp.server.fastmcp import FastMCP

# from mcp.client.stdio            ->  ye hmari history mantain nahi karta tha connection loose hony par net gaya ya light to sari conversation khatam.
# from mcp.client.streamable_http  -> recomended -> have session id ->  ye hmari history mantain karta hai connection loose hony par bhi jab dubara connection banega to wahi se start karega conversation ko.


# instance of FastMCP
mcp = FastMCP(name="my_mcp", stateless_http=True) # mcp server name & dont save conversation history.

#--------------------------------------------------------


@mcp.tool() # decorater
def hello_function(name: str):
    """This function says hello."""
    return f"Hellooooooooooooooooooooooooo {name}"


@mcp.tool()
def bye_function():
    """This function says goodbye."""
    return "Byeeeeeeeeeeeeeeeeee"


#--------------------------------------------------------
# jo request server par ati hai or jo yahn se jati hai usko manages karta hai.
mcp_app = mcp.streamable_http_app()