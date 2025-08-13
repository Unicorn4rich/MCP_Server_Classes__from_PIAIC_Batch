1. MCP -> Model Context Protocol -> ye apne pass tools bana kar rakhta hai.

2. Work flow Agent + MCP -> 
   Agent Pochega MCP se ke kitne tools hain apke pass to MCP bata dega mere pass itne tools hain
   phir Agent bolega ke is waly tool ko chala do jo mai bata rha hn or uske jo parameters mein values requred hain wo bhi 
   mai dey rha hn uske bad wo tool chalega or Agent SDK ko uska output mil jaega.

3. Filtration on tools -> 
   Agent jab tools mangta hai kisi topic/query se related to MCP pe bohut sary tools ban kar rakhy
   hoty hain to MCP kya karta hai Agent requrment ke mutabik jo tools match karte hain unki list utha kar Agent ko dikha 
   deta hai or baqi ke tools hata deta hai uski list mein nahi bhejta.

4. Ham khud ka MCP server bana kar usme apni E-commerce website ke tools bana kar unko rakh sakty hain or use kar sakty 
   hain but unhy manage ham khud kar rhy honge.
   But agr koi dosra platform hain jese facebook to wo khud ke MCP server pe tools bana kar rakhega jisko ham bhi use kar sakty
   hain but usy mantain rakhny ki zimma dari uski hogi hmari nahi.

5. Remote MCP Server -> Bahar ki Company`s jo tools bnati hain unko ham ye kehty hain.
6. Local MCP Server  -> Ye ham khud bnaty hain apni E-Commerce website ke liye.

7. Langraph, Crew Ai, N81, OpenAi Agent SDK -> 
   In Charo Frame work se bany Agents MCP Server ke tools Use kar sakty hain.

8. MCP server jsonRPC mein chalta hai or post ki request mangta hai ham se or isy ham browser se nahi postman se request 
   bhejenge check karne ke liye.

10. Clients:
    -postman ✔
    -request ✔
    -MCP Client
    -OpanAi Agent SDK Integration

tools/list -> Tool dekhna
tools/call tool use karna

---------------------------------------------------------------------------------------
Project setup:
1. uv ini
2. uv run main.py
3. uv add mcp  -> Write code in your file
4. active vertual envoirment
5. uv run uvicorn mcp_server:mcp_app --port 9000 --reload    -> run command for MCP server -> Not found -> becouse 
   browser get request karta hai or mcp ko post request chahiye.

6. Go to postman -> Post request -> url past with mcp endpoint-> http://127.0.0.1:8000/mcp

   Set postman header: Click Headers
   Accept          =          application/json, text/event-stream
   Content-Type    =          application/json

   Set Body: Click Body -> click -> raw -> click -> JSON
   fill box with jsonrpc request:
   {
    "jsonrpc" : "2.0",          -> model
    "method"  : "tools/list",   -> tools -> dekhna ya use karna
    "params"  : {},             -> empty
    "id"      : 1               -> request id -> jawab bhi isi id se aega.
   }
   

7. MCP response:
   {
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "tools": []  -> tools nahi hain hmare MCP server mein jabhi empty show kar rha hai.
    }
   }


8. Create tools in MCP server -> Write Function tool in file -> again post request from postman and get reponse:
   {                   => Tool Schema -> kiyun ke Agent first time tools manga kar dekhta hai abhi isme function ki return value nahi mili hamen.
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "tools": [                             => Now we get tool becouse we write in MCP server.
            {
                "name": "hello_function",      => tool name
                "description": "",             => description ham ne nahi di thi
                "inputSchema": {              
                    "properties": {},          => paramater nahi diyya tha ham ne.
                    "title": "hello_functionArguments",  => title mein function name ke sath Arguments laga dega.
                    "type": "object"                     => 
                }
            }
        ]
     }
   }
   

Jitne tools honge utne hamen yahn aa jaenge schema ban kar.


9. Ab tak ham sirf tools ki list manga kar dekh rhy thy but ab ham tools ko call kar ke unke return ki values lenge:
   Write again post request from postman everthing will be same but the input body schema will be changed:
   request body:

   {                                      -> dictionery
    "jsonrpc": "2.0",                     -> model
    "method" : "tools/call",              -> pichli bar tools/list likha tha ab tools/call likh kar function ka output ley rhy hain. 
    "params" : {                          -> parameter aik dictionery hai isme jo paraemter aya hai wo name ka hai.
        "name" : "hello_function",        ->  function name jiska paramter hai.
        "arguments" : {                   -> ye aik dict hai
            "name" : "shoaibbbbbbbbbbb"   -> name paramter ke liye value hamne khud se likh kar bheji.
        }
      },
      "id"     : 1                        -> id jis se request bheji thi or usi se response mila.
   }


10. tool call output response 200 successfull:
    {
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "Hellooooooooooooooooooooooooo shoaibbbbbbbbbbb"   -> tool ka return output mila name paramter value add kar ke.
            }
        ],
        "isError": false                                                   -> error bhi nahi aya.
    }
}
 

---------------------------------------------------------------------------------------
Client changes postman to -> request module

1. create mcp_client.py file 
2. install -> uv add requests
3. import in file -> import request 
4. write code in file same to same postman -> Url -> Headers -> Body -> body input data 
5. run file -> uv run mcp_client.py -> get output







