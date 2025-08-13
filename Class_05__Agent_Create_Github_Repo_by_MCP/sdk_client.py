import os  # only for ithub mcp server remotely use.
from dotenv import load_dotenv
from agents import Agent, Runner, enable_verbose_stdout_logging
from agents.mcp import MCPServerStreamableHttp, MCPServerStreamableHttpParams
import rich
import asyncio

#-------------------------------
load_dotenv()
GITHUB_PAT=os.getenv("GITHUB_PAT") # ye sirf Github mcp server use karne ke liye line likhi hai.
# enable_verbose_stdout_logging()
# set_tracing_disabled(disabled=True)

#------------------------------------
async def main():
    http_server = MCPServerStreamableHttp(params=MCPServerStreamableHttpParams(
        url="https://api.githubcopilot.com/mcp/",
        headers={"Authorization": f"Bearer {GITHUB_PAT}"} # ye sirf github ka MCP server use karne ke liye line likhi hai.
    ))
    
    async with http_server: # Agent ka MCP server se connection ho rha hai
        agent = Agent( 
                      name="My_agent",
                      instructions="You are a helpful assistant",
                      model="gpt-4.1-mini",
                      mcp_servers=[http_server] # mcp server se tools get.
        ) 

#---------------------------------
        result = await Runner.run(agent, input="make a new repo with readme.md file. repo named will be 'AGENT_REPO_CREATE_From MCP' and write a text in readme.md file of 'Hello i am shoaib now i create This repo from my Agent in One command readme.md file'") 
        rich.print("🙂", result.final_output)
  
asyncio.run(main())  


