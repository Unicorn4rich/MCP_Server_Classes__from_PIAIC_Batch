## Postman
## Python Request lib


1. MCP Server 3 Cheezen Note:
2. Tool     -> function -> API -> Database -> etc.
3. Resorces -> File ka hona Jese Ms Word ki file Picture ya PDF file jisme koi data rakha hua ho or wo file hamne Chatgpt ko
               dey di to ye Resorce hua ke hamne chatgpt ko resorce diyya hai.
4. Prompt   -> Pre defined Prompt jese -> Search OpenAi Agent SDK Latest Documentation -> hmari query


-------------------------------------------------------------------------------------
Tools:
 -tools/list => dekhny wala
 -tools/call => tool use karne wala

Resource:
 -resources/list => dekhny wala
 -resources/read => tool use karne wala

Prompt:
 -prompts/list => dekhny wala
 -prompts/get  => tool use karne wala


-------------------------------------------------------------------------------------
Project setup:
1. uv ini
2. uv run main.py
3. uv add mcp  -> Write code in your file
4. active vertual envoirment
5. uv run uvicorn mcp_server:mcp_app --port 9000 --reload    -> run command for MCP server -> Not found -> becouse browser get request karta hai or mcp ko post request chahiye.

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


-------------------------------------------------------------------------------------
Resources Code:

1. Write Resource function code:

   @mcp.resource("docs//documents")
   def my_resource():
      return "I am my_resource"


2. Start server -> Go to postman -> Set headers like tools watch example from top notes -> Write Json Raw body for request:

3.  Body code sirf resroce tools ki list mangwa kar dekh rhy hain ke kitne resouces hain or kon kon se hain:
    {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "resources/list",
    "params": {}
    }


4. Ger respnse of all resource tools to watch:
   Response:

{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "resources": [
      {
        "uri": ""docs//documents"",
        "name": "my_resource",
      }
    ],
    "isError": false
  }
}


Ab un resouces ke tools ka call karwa kar output ley rhy hain

5. write code for resource tool output:
   {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "resources/read",     -> list ki jagah yahn (read) aega.
    "params": {
        "name" : "my_resource",     -> resource function tool name likhenge.
        "arguments" : {},           -> paramters uske hain nahi to arguments empty hain.
        "uri" : "docs//documents"   -> uri bhi denge required -> uri aik card click pe jo shop ka route ata hai wo hai.
    }
}

successfully get (200) response


-------------------------------------------------------------------------------------
Prompt Code:

1. Write Prompt function code:

   @mcp.prompt()
   def my_prooompt():
      return "I am my Prompt"


2. Start server -> Go to postman -> Set headers like tools watch example from top notes -> Write Json Raw body for request:

3.  Body code sirf Prompt tools ki list mangwa kar dekh rhy hain ke kitne Prompt hain or kon kon se hain:
    {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "prompts/list",
    "params": {}
    }

successfully get response of (200) all prompts tools


4. Ab ham in prompts tools ko get kar ke output leny wala code likh rhy hain:
{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "prompts/get",
    "params": {
        "name" : "my_proopmt",
        "arguments" : {},
    }
}

successfully get response of (200) specific prompts tool



-------------------------------------------------------------------------------------
Client changes postman to -> request module

1. create mcp_client.py file 
2. install -> uv add requests
3. import in file -> import request 
4. write code in file same to same postman -> Url -> Headers -> Body -> body input data 
5. run file -> uv run mcp_client.py -> get output

