Repo link  -> https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/05_capabilities_and_transport

1. MCP Server -> Tools + Resource + Prompt

2. MCP Clients:
               -postman
               -req lib
               -mcp client
               -agent sdk

-----------------------------------------------------------------------------------
Project setup:
1. uv init
2. uv run main.py
3. uv add mcp  -> Write code in your file
4. active vertual envoirment
5. uv run uvicorn mcp_server:mcp_app --port 9000 --reload    -> run command for MCP server -> Not found -> becouse browser get request karta hai or mcp ko post request chahiye.

6. Go to postman -> Post request -> url past with mcp endpoint-> http://127.0.0.1:8000/mcp
   Set postman header: Click Headers

   Accept          =          application/json, text/event-stream
   Content-Type    =          application/json


 Set Body: Click Body -> click -> raw -> click -> JSON


   fill box with jsonrpc request:  -> initialize req kar rhy hain session id leny ke liye
   {
    "jsonrpc" : "2.0",          -> model
    "method"  : "initialize",   -> session id lena server se -> becouse statless=False hai mcp server ka jabhi wo ab 3 steps mein data dega.
    "params"  : {},             -> empty
    "id"      : 1               -> request id -> jawab bhi isi id se aega.
   }
   

7. MCP response: -> response ke headers ko open kar ke session id milegi.
   mcp-session-id       = b6a0a873b27f41a4bf88c901afae5be9 -> isy ham apne main header mein set kar denge baqi config ke neechy.
   MCP-Protocol-Version = 2025-06-18

8. Ab Body mein jaa kar (Initialize) req wala code hata kar ye wala code likh denge:
   {
    "jsonrpc": "2.0",
    "method": "notifications/initialized"
   }

9. 202 Accepted -> successfully permission mil gai kaam karne ki server pe memory ke sath.

10. ab jab ke hamen ijazat mil gai hai memory ke sath kaam akrne ki to ham ab tools call karenge:
    {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 1,
    "params": {}
    }

11. response successfully aega jo bhi tool hoga mcp mein:

{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "tools": [
            {
                "name": "hello_function",
                "description": "",
                "inputSchema": {
                    "properties": {},
                    "title": "hello_functionArguments",
                    "type": "object"
                }
            }
        ]
    }
}
   