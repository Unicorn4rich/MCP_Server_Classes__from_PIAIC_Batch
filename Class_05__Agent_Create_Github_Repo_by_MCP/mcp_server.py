from mcp.server.fastmcp import FastMCP # -> Server create Class -> ye server jsonrpc protcols ko follow karta hai matlab POST request ho sakti hain 

# Server Tool, Resource, or Prompt rakhta hai.
mcp = FastMCP(name="my_mcp", stateless_http=True) # -> session save nahi hoga memory lose.

from mcp.server.fastmcp.prompts import base  # Import for prompts

#-------------------------------------------------------------------
# MCP Tools

@mcp.tool()
def hello(name: str):
    """function return greeting message"""
    # API CALLING LOGICS
    # DB CALLING LOGICS
    # SANITY CALLING LOGICS
    # LOGIC
    # LOGIC
    # LOGIC
    # LOGIC
    return f"helloooooooooooooooooooooooooooooooooo {name}"


#---------------------------------------
# MCP Resources

# @mcp.resource("docs://documents")
# def my_resource():
#     return "I am my_resooooooooooooooooooooooource"


# #---------------------------------------
# # MCP Prompt

@mcp.prompt()
def my_prooompt()-> list[base.Message]: # -> optional -> by-default -> simple function bana sakty hain.
    my_message = "I am my Prompt"
    
    return [base.UserMessage(my_message)] # optional -> bhaly is class ko return na karwaen by-dfault ye khud bana leta hai.



mcp_app = mcp.streamable_http_app() # -> streaming ki form mein data lata hai chunks mein -> matlab request leta hai response deta hai.




