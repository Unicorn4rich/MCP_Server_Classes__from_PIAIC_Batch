from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams
import rich
import asyncio


#-----------------------------------
load_dotenv()
enable_verbose_stdout_logging()
#-----------------------------------

# Is file mein hamne Agent SDK ke zariye MCP server se tools ko get kiyya or call kiyya.
async def main():
    server_response = MCPServerStreamableHttp(params=MCPServerStreamableHttpParams(url="http://127.0.0.1:9000/mcp"))
    
    async with server_response:
        agent = Agent(
            name="agent",
            # instructions="when user tells you name you use hello_function tool to greet user, when user says bye you use bye_function tool to say goodbye.",
            instructions="you are a helpful assistant",
            model="gpt-4.1-mini",
            mcp_servers=[server_response]
      )

#-----------------------------------
        result = await Runner.run(agent, input="show me the list of tools, call hello tool and hello to me, my name is shoaib")
        rich.print(result.final_output)


asyncio.run(main())



#---------------------------------------------------------------------------------get/tools/from agent by prompt
# result = await Runner.run(agent, input="show me the list of tools")
# rich.print(result.final_output) Output will be:

# (New folder) PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_MCP_CLASSES\New folder> uv run app.py
# Here is the list of available tools:

# 1. hello_function: This function is used to say hello. It requires a parameter "name" (string).

# 2. bye_function: This function is used to say goodbye. It does not require any parameters.

# 3. multi_tool_use.parallel: This tool allows running multiple tools simultaneously (in parallel). Only functions tools are permitted to be    
# used with this.

# If you would like to use any of these tools or need more information, please let me know!



#---------------------------------------------------------------------------------calls/tools/from agent by prompt
# Tools output will be:

# result = await Runner.run(agent, input="show me the list of tools, call hello tool and hello to me, my name is shoaib")
# rich.print(result.final_output)



# I have called the hello tool for you. It says: "Hellooooooooooooooooooooooooo shoaib".

# Here is the list of available tools:
# 1. hello_function - This tool says hello.
# 2. bye_function - This tool says goodbye.

# Is there anything else you would like to do?




#---------------------------------------------------------------------------------verbose

# (New folder) PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_MCP_CLASSES\New folder> uv run app.py
# Creating trace Agent workflow with id trace_76e5a82b710e4115b526e1bbdd5173bd
# Setting current trace: trace_76e5a82b710e4115b526e1bbdd5173bd
# Creating span <agents.tracing.span_data.MCPListToolsSpanData object at 0x00000200B4429F10> with id None
# Creating span <agents.tracing.span_data.AgentSpanData object at 0x00000200B3AADCC0> with id None
# Running agent agent (turn 1)
# Creating span <agents.tracing.span_data.ResponseSpanData object at 0x00000200B4447B10> with id None
# Calling LLM gpt-4.1-mini with input:
# [
#   {
#     "content": "show me the list of tools, call hello tool and hello to me, my name is shoaib",
#     "role": "user"
#   }
# ]
# Tools:
# [
#   {
#     "name": "hello_function",
#     "parameters": {
#       "properties": {
#         "name": {
#           "title": "Name",
#           "type": "string"
#         }
#       },
#       "required": [
#         "name"
#       ],
#       "title": "hello_functionArguments",
#       "type": "object"
#     },
#     "strict": false,
#     "type": "function",
#     "description": "This function says hello."
#   },
#   {
#     "name": "bye_function",
#     "parameters": {
#       "properties": {},
#       "title": "bye_functionArguments",
#       "type": "object"
#     },
#     "strict": false,
#     "type": "function",
#     "description": "This function says goodbye."
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN
# Previous response id: None

# LLM resp:
# [
#   {
#     "arguments": "{\"name\":\"shoaib\"}",
#     "call_id": "call_3C3Nc7sXUcfX5DFzN21NdhiI",
#     "name": "hello_function",
#     "type": "function_call",
#     "id": "fc_688b8ef6a51c819b9666328aded2a0ca021773d1a0d3f1f8",
#     "status": "completed"
#   }
# ]

# Creating span <agents.tracing.span_data.FunctionSpanData object at 0x00000200B29BDEA0> with id None
# Invoking MCP tool hello_function with input {"name":"shoaib"}
# MCP tool hello_function returned meta=None content=[TextContent(type='text', text='Hellooooooooooooooooooooooooo shoaib', annotations=None, meta=None)] structuredContent=None isError=False
# Creating span <agents.tracing.span_data.MCPListToolsSpanData object at 0x00000200B4983AD0> with id None
# Running agent agent (turn 2)
# Creating span <agents.tracing.span_data.ResponseSpanData object at 0x00000200B4967B10> with id None
# Calling LLM gpt-4.1-mini with input:
# [
#   {
#     "content": "show me the list of tools, call hello tool and hello to me, my name is shoaib",
#     "role": "user"
#   },
#   {
#     "arguments": "{\"name\":\"shoaib\"}",
#     "call_id": "call_3C3Nc7sXUcfX5DFzN21NdhiI",
#     "name": "hello_function",
#     "type": "function_call",
#     "id": "fc_688b8ef6a51c819b9666328aded2a0ca021773d1a0d3f1f8",
#     "status": "completed"
#   },
#   {
#     "call_id": "call_3C3Nc7sXUcfX5DFzN21NdhiI",
#     "output": "{\"type\":\"text\",\"text\":\"Hellooooooooooooooooooooooooo shoaib\",\"annotations\":null,\"meta\":null}",
#     "type": "function_call_output"
#   }
# ]
# Tools:
# [
#   {
#     "name": "hello_function",
#     "parameters": {
#       "properties": {
#         "name": {
#           "title": "Name",
#           "type": "string"
#         }
#       },
#       "required": [
#         "name"
#       ],
#       "title": "hello_functionArguments",
#       "type": "object"
#     },
#     "strict": false,
#     "type": "function",
#     "description": "This function says hello."
#   },
#   {
#     "name": "bye_function",
#     "parameters": {
#       "properties": {},
#       "title": "bye_functionArguments",
#       "type": "object"
#     },
#     "strict": false,
#     "type": "function",
#     "description": "This function says goodbye."
#   }
# ]
# Stream: False
# Tool choice: NOT_GIVEN
# Response format: NOT_GIVEN
# Previous response id: None

# Exported 2 items
# Exported 3 items
# LLM resp:
# [
#   {
#     "id": "msg_688b8ef7f0d4819bb1eca238754f5070021773d1a0d3f1f8",
#     "content": [
#       {
#         "annotations": [],
#         "text": "I have called the hello tool for you. It says: \"Hellooooooooooooooooooooooooo shoaib\".\n\nHere is the list of available tools:\n1. hello_function - This tool says hello.\n2. bye_function - This tool says goodbye.\n\nIs there anything else you would like to do?",   
#         "type": "output_text",
#         "logprobs": []
#       }
#     ],
#     "role": "assistant",
#     "status": "completed",
#     "type": "message"
#   }
# ]

# Resetting current trace
# I have called the hello tool for you. It says: "Hellooooooooooooooooooooooooo shoaib".

# Here is the list of available tools:
# 1. hello_function - This tool says hello.
# 2. bye_function - This tool says goodbye.

# Is there anything else you would like to do?
# Shutting down trace provider
# Shutting down trace processor <agents.tracing.processors.BatchTraceProcessor object at 0x00000200B2881BE0>
# Exported 2 items
# (New folder) PS D:\GOVERNER HOUSE\SIR TAHA CLASSES\PIAIC_MCP_CLASSES\New folder> 
