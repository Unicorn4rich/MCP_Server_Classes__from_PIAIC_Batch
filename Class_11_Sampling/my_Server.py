from mcp.server.fastmcp import FastMCP, Context
from mcp.types import SamplingMessage, TextContent
import rich

app = FastMCP()

#-------------------------------------------------
# Sampling:
# Client request karega MCP ko ke ye create_story() wala tool chla ke do or paramter mein topic mai dunga uspe jis tarhn ki story chahiye. 

@app.tool() #ctx -> llm se isme question pochenge or (topic) argument of story yahn aega.
async def create_story(ctx: Context, topic: str):  # ye sampling ka tool ulta client ko request karega ke apna llm use kar ke mujhe ye kaam kar ke do.
    # Client ke liye swal.
    response = await ctx.session.create_message(  # -> isme sampling ho rhi hai llm ke liye question request or uski settings bhi yahn se config ki jaa sakti hain.
        messages = [SamplingMessage(
            role="user", # user ka question jo client yahn aega.
            content = TextContent(type="text", text=f"write a short story of two lines on {topic}") # llm se swal kar rhy hain ke client ne (topic) mein jo argument likha hai uska result laa kar do mujhe
        )],
        max_tokens=100
    ) 
    
    
    rich.print("response: 😂", response.content.text)
    
    return response.content.text


#-------------------------------------------------
my_mcp = app.streamable_http_app()

#-------------------------------------------------
# Note

# 1. Sampling:
#    MCP Server Client ko request karega or Client mcp server ko response karega. Server request kar rha hai Client ko ke 
#    mujhe tumhara LLM use karna hai or Client keh rha hai chalo karlo or apna jawab ley lo jo tumhe mujh se chahiye tha.