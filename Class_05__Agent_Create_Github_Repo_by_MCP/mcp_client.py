from mcp.client.streamable_http import streamablehttp_client  # 
from mcp.client.session import ClientSession
import asyncio
import rich


async def main():
    #  streamble ka method 3 cheezen return karta hai jisko hamne as kar ke destructre kar liya or 3sri value nahi chahiye to underscrore laga diyya.
    async with streamablehttp_client(url="http://127.0.0.1:8000/mcp") as (read_stream, write_stream, _): # destructre
        
        async with ClientSession(read_stream, write_stream) as session: # -> this is instance
            await session.initialize() # open close karna ye manages karega.
            
            
            tool_result = await session.list_tools() # tools ki list dekh rhy hain ham.
            # rich.print("🤬: ", tool_result) # tools ka schema show hoga.
            
            hello_tool_call = await session.call_tool(name="hello") # tools ko call krwa ke output ley rhy hain.
            # rich.print("😘", hello_tool_call) # tools ka schema show hoga.
            
            
            res_result = await session.list_resources()  # resources ki list dekh rhy hain ham.
            # rich.print("🤬", res_result)  # resources ka schema show hoga.
            
            read_result = await session.read_resource(uri="docs://documents")  # resources ko call krwa ke output ley rhy hain.
            # rich.print("😘", read_res_result) # resources ka schema show hoga.
            
            
            prompt_result = await session.list_prompts()  # prompts ki list dekh rhy hain ham.
            rich.print("🤬", prompt_result)  # prompts ka schema show hoga.
            
            get_prompt_result = await session.get_prompt(name="my_prooompt")  # prompts ko call krwa ke output ley rhy hain.
            rich.print("😘", get_prompt_result) # prompts ka schema show hoga.
            
            

asyncio.run(main())







#----------------------------------------------------------------------------------------------------------------
# Notes

# tools/list and tools/call -> terminal outputs:

# 🤬:  -> tool list dekhny wala
# ListToolsResult(
#     meta=None,
#     nextCursor=None,
#     tools=[
#         Tool(
#             name='hello',
#             title=None,
#             description='function return greeting message',
#             inputSchema={'properties': {}, 'title': 'helloArguments', 'type': 'object'},
#             outputSchema=None,
#             annotations=None,
#             meta=None
#         )
#     ]
# )


# 😘  -> tool/call karne wala
# CallToolResult(
#     meta=None,
#     content=[TextContent(type='text', text='helloooooooooooooooooooooooooooooooooo', annotations=None, meta=None)],
#     structuredContent=None,
#     isError=False
# )



#------------------------------------------------------------------
# resources/list and resources/read -> terminal outputs:

# 🤬
# ListResourcesResult(
#     meta=None,
#     nextCursor=None,
#     resources=[
#         Resource(
#             name='my_resource',
#             title=None,
#             uri=AnyUrl('docs://documents'),
#             description='',
#             mimeType='text/plain',
#             size=None,
#             annotations=None,
#             meta=None
#         )
#     ]
# )


# 😘
# ReadResourceResult(
#     meta=None,
#     contents=[TextResourceContents(uri=AnyUrl('docs://documents'), mimeType='text/plain', meta=None, text='I am my_resource')]
# )



#------------------------------------------------------------------
# prompts/list and prompts/get -> terminal outputs:


# 🤬 -> prompts list dekhny wala
# ListPromptsResult(meta=None, nextCursor=None, prompts=[Prompt(name='my_prooompt', title=None, description='', arguments=[], meta=None)])

# 😘 -> prompts list get karne wala
# GetPromptResult(
#     meta=None,
#     description='',
#     messages=[PromptMessage(role='user', content=TextContent(type='text', text='I am my Prompt', annotations=None, meta=None))]
# )