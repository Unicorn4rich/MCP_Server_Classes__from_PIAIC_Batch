# Ye file Server hai hmara
from mcp.server.fastmcp import FastMCP

# from mcp.client.stdio            ->  ye hmari history mantain nahi karta tha connection loose hony par net gaya ya light to sari conversation khatam.
# from mcp.client.streamable_http  -> recomended -> have session id ->  ye hmari history mantain karta hai connection loose hony par bhi jab dubara connection banega to wahi se start karega conversation ko.


# instance of FastMCP
mcp = FastMCP(name="my_mcp", stateless_http=True) # mcp server name & dont save conversation history.

#--------------------------------------------------------
# URL alag cheez hai or URI alag cheez isme details zada hoti hain.
#         scheme       host
# uri -> resource://my-resource

# scheme   domain    endpoint
# https://shoaib.com/skills


my_docs = {  # just imagine ke ye wo data file/picture/pdf hai jo hamne apne laptop se chatgpt pe upload kiyya hai.
    "student_name" : "Shoaib"
}


#                 uri
@mcp.resource("docs://document") # ye resource chaly or hamen docs return kardy.
def show_docs():
    """Show all available documents."""
    return my_docs




#--------------------------------------------------------
# jo request server par ati hai or jo yahn se jati hai usko manages karta hai.
mcp_app = mcp.streamable_http_app()

# Run this command to start MCP Server -> active vertual envoirment -> uv run uvicorn mcp_server:mcp_app --port 9000 --reload

#1. If not starting server then delete .venv folder and create it again.
#2. uv sync -> all dependences installed in virtual environment.
#2. uv venv && uv pip install -e . -> second tariqa




