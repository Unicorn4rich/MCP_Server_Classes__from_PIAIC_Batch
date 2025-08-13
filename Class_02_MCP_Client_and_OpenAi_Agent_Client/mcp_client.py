# Ye file Client hai hmara or ye braber wali server file ko hi request bhej kar us se tools ley rhi hai 😂.
import asyncio
from mcp.client.session import ClientSession 
from mcp.client.streamable_http import streamablehttp_client
import rich

#---------------------------------------------------------------------------------------------tool/list
# MCP Server se tools manga kar dekhny wala code ke kon kon se tools hain: -> Basic concept ye hai ke jab hmara 
# Agent tools[] mein function tools rakh kar LLM ko dikhata hai ke mere pass ye tools hain.
# Ye jo code hai usi cheez ko represent kar rha hai.


async def  main():
    # streamablehttp_client -> te chunks mein jawab laega jabhi async kar ke wait ka rhy hain or ye 3 cheezen return karta hai.
    async with streamablehttp_client(url="http://127.0.0.1:9000/mcp") as (read_stream, write_stream, _): # 2 cheezen hamne destructure karli teesri cheez hmare kaam ki nahi isliye usy ignore kar diyya.
        # class ki property dey kar instance create kar liya hamne -> session
        async with ClientSession(read_stream, write_stream) as session:
            
    #----------------------------------------------------------------------------------------------        
            await session.initialize() # session ko initialize kar liya.
    #----------------------------------------------------------------------------------------------     
            
            all_tools = await session.list_tools() # tools ko list mein lany wala function call kiya.
            # rich.print("all_tools: ", all_tools)            
            for tool in all_tools.tools:
                rich.print(tool.name) # only get tools name -> hello_function + bye_function
                
                
            print("\n\n")                
#---------------------------------------------------------------------------------------------tool/call
# MCP Server se tools ko chala kar unka return result leny wala code: -> Iska Basic Concept aisy samjh sakty hain ke jab
# sary tools llm ke pass jaty hain schema ki form mein or llm requirment ke mutabik jo tool call karne ke liye kehta or agr
# tool mein parameter hoty hain to un parameter ke liye values deta hai as a argument ke is tool ko chala do. 

            tool_result = await session.call_tool(
                name="hello_function",  # tool ka naam
                arguments={
                    "name" : "Shoaibbbbbbbbbbbbbbbbbbbbbbbb"  # tool ke parameter ke liye value
                }
            )
            # tool ka result -> content mein text hota hai jawab toolka jawab yani return.
            rich.print(tool_result.content[0].text)  #  Hellooooooooooooooooooooooooo Shoaibbbbbbbbbbbbbbbbbbbbbbbb





asyncio.run(main())

# is Client wali file ko chlany ki command -> uv run mcp_client.py 



    
    


