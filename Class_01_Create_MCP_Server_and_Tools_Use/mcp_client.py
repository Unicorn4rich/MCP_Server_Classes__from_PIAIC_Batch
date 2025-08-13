# Ye file Client hai hmara or ye braber wali server file ko hi request bhej kar us se tools ley rhi hai 😂.
import requests
import rich


#---------------------------------------------------------------------------------------------tool/list
# MCP Server se tools mmanga kar dekhny wala code ke kon kon se tools hain: -> Basic concept ye hai ke jab hmara 
# Agent tools[] mein function tools rakh kar LLM ko dikhata hai ke mere pass ye tools hain.
# Ye jo code hai usi cheez ko represent kar rha hai.


url = "http://127.0.0.1:8000/mcp"  # url of the MCP server -> jese hamne postman me diya tha.

headers = {  # ye headers jese hamne postman me diya tha uski values ke sath.
    "Accept" : "application/json, text/event-stream",
    "Content-Type" : "application/json"
}

body = {  # ye body jese hamne postman me di thi dict mein.
    "jsonrpc": "2.0",
    "method" : "tools/list",   # tools manga kar dekhna chahta hai Agent.
    "params" : {},
    "id"     : 1
}

result = requests.post(url=url,   headers=headers,    json=body) # json -> body ko represent kar rha hai postman ki.

# result streaming mein aa rha hai isliye ham loop laga kar lenge data.
for data in result.iter_lines():
    rich.print(data) 
    
#---------------------------------------------------------    
# result:  -> from terminal

# b'event: message'
# b'data: {"jsonrpc":"2.0","id":1,"result":{"tools":[{"name":"hello_function","description":"This function says 
# hello.","inputSchema":{"properties":{"name":{"title":"Name","type":"string"}},"required":["name"],"title":"hello_functionArguments","type":"object"}},{"name":"bye_function","description":"This function says 
# goodbye.","inputSchema":{"properties":{},"title":"bye_functionArguments","type":"object"}}]}}'  
    
    
    
    
    
#---------------------------------------------------------------------------------------------tool/call
# MCP Server se tools ko chala kar unka return result leny wala code: -> Iska Basic Concept aisy samjh sakty hain ke jab
# sary tools llm ke pass jaty hain schema ki form mein or llm requirment ke mutabik jo tool call karne ke liye kehta or agr
# tool mein parameter hoty hain to un parameter ke liye values deta hai as a argument ke is tool ko chala do. 


# url = "http://127.0.0.1:8000/mcp"  # -. opar wala url utha lega.

# headers = {  # ye header bhi opar wala utha lege isme bhi koi changes nahi karte tool call karte waqt.
#     "Accept" : "application/json, text/event-stream",
#     "Content-Type" : "application/json"
# }


body2 = {  # ye body jese hamne postman me di thi dict mein.
    "jsonrpc": "2.0",
    "method" : "tools/call",   # tools manga kar dekhna chahta hai Agent.
    "params" : {
        "name" : "hello_function",
        "arguments" : {
            "name" : "shoaibbbbbbbbbbbbbbbbb"
        }
    },
    "id"     : 1
}

result2 = requests.post(url=url,   headers=headers,    json=body2) # json -> body ko represent kar rha hai postman ki.

# result streaming mein aa rha hai isliye ham loop laga kar lenge data.
for data in result2.iter_lines():
    rich.print(data)     
    
    
#------------------------------------------------------------------------------------------------------    
# result output:   

# {
#     "jsonrpc": "2.0",
#     "id": 1,
#     "result": {
#         "content": [
#             {
#                 "type": "text",
#                 "text": "Hellooooooooooooooooooooooooo shoaibbbbbbbbbbbbbbbbb"   -> tool ka return output mila name paramter value add kar ke.
#             }
#         ],
#         "isError": false                                                   -> error bhi nahi aya.
#     }
# } 