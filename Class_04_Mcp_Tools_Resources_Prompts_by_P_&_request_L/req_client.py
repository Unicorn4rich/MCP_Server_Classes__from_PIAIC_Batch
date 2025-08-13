import requests
import rich

#------------------------------------------------------------------

headers = {
    "Accept": "application/json, text/event-stream",
    "Content-Type": "application/json"
}

#-------------------------------------
# tools list watch:

body = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list", # -> for tools list
    "params": {}
}


# tools call get return output result form tools:
body = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call", # -> for tools call
    "params": {
        "name": "hello",    # function name jis naam se tools ka function bnaya.
        "arguments": {}     # arguments tab denge jab function paramter ley rha hoga.
    }
}


#-------------------------------------
# Resrouce list watch:

body = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "resources/list", # -> for get resources tools list
    "params": {}  # paramter hain nahi
}


# tools call get return output result form tools:
body = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "resources/read", # -> for get resources tools output
    "params": {
        "name": "my_resource",    # function name jis naam se tools ka function bnaya.
        "arguments": {},          # arguments tab denge jab function paramter ley rha hoga.
        "uri" : "docs//documents" # requred this is route path?
    }
}


#-------------------------------------
# Prompts list watch:

body = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "prompts/list", # -> for get prompts tools list
    "params": {}  # paramter hain nahi
}


# tools call get return output result from tools:
body = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "prompts/get", # -> for get prompts tools output
    "params": {
        "name": "my_prooompt",    # function name jis naam se tools ka function bnaya.
        "arguments": {},          # arguments tab denge jab function paramter ley rha hoga.
    }
}

#------------------------------------------------------------------

response = requests.post(
    url="http://127.0.0.1:8000/mcp",
    headers=headers,
    json=body
)

for value in response.iter_lines(): # chunks mein jawab ata hai isliye ham loop laga kar dekh rhy hain.
    rich.print(value)