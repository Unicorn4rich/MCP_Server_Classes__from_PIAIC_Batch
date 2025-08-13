# Ye file Client hai hmara or ye braber wali server file ko hi request bhej kar us se tools ley rhi hai 😂.
import asyncio
from mcp.client.session import ClientSession 
from mcp.client.streamable_http import streamablehttp_client
import rich


async def  main():
    # streamablehttp_client -> te chunks mein jawab laega jabhi async kar ke wait ka rhy hain or ye 3 cheezen return karta hai.
    async with streamablehttp_client(url="http://127.0.0.1:9000/mcp") as (read_stream, write_stream, _): # 2 cheezen hamne destructure karli teesri cheez hmare kaam ki nahi isliye usy ignore kar diyya.
        
        # class ki property dey kar instance create kar liya hamne -> session
        async with ClientSession(read_stream, write_stream) as session: # instance
            await session.initialize() # session ko initialize kar liya.
            
            all_res = await session.list_resources() # ye list dikhaega resources ki jo server par available hain.
            rich.print(all_res) # resources dekhi.
            
            read_res = await session.read_resource("docs://document") # ye resource hamne mcp_server.py mein bnaya hua hai or isy ham us server se get kar ke chala rhy hain.
            rich.print(read_res) # resources chala di.



asyncio.run(main())
# is Client wali file ko chlany ki command -> uv run client_res.py


#--------------------------------------------------------resource show
# all_res = await session.list_resources() # ye list dikhaega resources ki jo server par available hain.
# rich.print(all_res)
            
            
# ListResourcesResult(  -> ye resouce hamne mcp_server.py mein bnaya hua hai or isy ham us server se get kar ke dekh rhy hain.
#     meta=None,      
#     nextCursor=None,
#     resources=[     
#         Resource(   
#             name='show_docs',
#             title=None,
#             uri=AnyUrl('docs://document'),
#             description='Show all available documents.',
#             mimeType='text/plain',
#             size=None,
#             annotations=None,
#             meta=None
#         )
#     ]
# )

    
 
 #--------------------------------------------------------resource show
# read_res = await session.read_resource("docs://document") # ye resource hamne mcp_server.py mein bnaya hua hai or isy ham us server se get kar ke chala rhy hain.
# rich.print(read_res)   


# ReadResourceResult(
#     meta=None,
#     contents=[
#         TextResourceContents(uri=AnyUrl('docs://document'), mimeType='text/plain', meta=None, text='{\n  "student_name": "Shoaib"\n}')
#     ]
# )
