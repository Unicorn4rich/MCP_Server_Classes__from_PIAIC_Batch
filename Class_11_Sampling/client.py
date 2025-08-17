from mcp.client.streamable_http import streamablehttp_client
from mcp.client.session import ClientSession
import asyncio
from mcp.shared.context import RequestContext
from typing import Any
from mcp.types import CreateMessageRequestParams, CreateMessageResult, ErrorData, TextContent
import rich
from openai import OpenAI



client = OpenAI()


# llm ko question dey kar us se jawab leny wala method
async def llm_call(context = RequestContext["ClientSession", Any], params = CreateMessageRequestParams)-> CreateMessageResult | ErrorData:
    rich.print("params: ", params.messages[0].content.text)
    
    return CreateMessageResult(
        role = "assistant",
        content = TextContent(type="text", text="I am shoaib and shoaib is not n8n Agent"),
        model = "gpt-4.1-mini"
    )


# Server se connection bnany wala sara logic is function mein likha hai.
async def main():
    
    async with streamablehttp_client(url="http://127.0.0.1:8000/mcp/") as (read_stream, write_stream, _): # instance of 3 propertys ka
        
        async with ClientSession(read_stream, write_stream, sampling_callback=llm_call) as session: # instance of class  + sampling_callback -> ye server ko response bhejega uski query ka llm ko call kar ke.
            await session.initialize() #  ready to use
            
            tool_result = await session.call_tool(
                name="create_story", # tool name jo server mein hai.
                arguments={
                    "topic": "story on n8n agents"  # us tool ko argument ki value di jaa rhi hai.
                }
            )
            
            rich.print("tool_result: ",tool_result)
            



asyncio.run(main())