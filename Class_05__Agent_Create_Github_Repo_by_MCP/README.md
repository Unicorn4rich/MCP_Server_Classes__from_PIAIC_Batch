MCP Client ✔     -> Code in Class 05
MCP Inspector ✔
MCP Agent SDK ✔

1. MCP -> URL -> HTTP -> GET POST PATCH DELETE
2. jsonrpc aik standard hai jis se ham remotely Mcp se functions ko call karwaty hain.

--------------------------------------------
MCP Inspector ✔

1. install -> npx @modelcontextprotocol/inspector
2. Transport Type -> select -> Streamable HTTP
3. URl -> http://localhost:8000/mcp
4. click -> Connect button

5. Top pe tabs show honge -> Resources, Prompts, Tools, etc,
   unke neechy hi 3 box card show honge -> Resources, Prompts, Tools -> in cards ke andar ke buttons pe click karenge 
   jese (List Resource) to isi boc mein jitne resource waly tools honge show ho jaenge neechy or jis tool pe click karenge
   wo tool chal kar hamen result output laa kar dey dega.


--------------------------------------------
MCP Agent SDK ✔

1. Code in Class 05
2. local mcp server  -> Complete ✔  -> yani ham apna server bana ke jo use karte hain wo.
3. Remote mcp server -> Complete ✔  -> kisi platform ka mcp server use karty hain.
4. go to google search -> Github mcp server url -> get -> "https://api.githubcopilot.com/mcp/" -> replace with local server url.
5. got to your github -> right side apni dp pe click karen scrolll down kar ke neechy jaen left side bar ke end mein aik tab
   nazar aega (Developer Settings) uspe click karen.
6. Personal access tokens -> click -> Fine-grained tokens -> click -> Generate new token
7. Token name -> my_token
8. Description -> pata nahi kuch bhi likh do
9. Resource owner -> apni shakal ani chahiye yahn
10. Expiration -> jitna marzi set karen -> 30 days
11. Repository access -> All repositories
12. Add Permission -> Tik marl all -> total 29
13. Read-Only ko -> Read and write kar den -> totaly 29 sab ko
14. got to second tab -> Account -> click -> Add permission -> tik mark all -> total 19
15. Read-Only ko -> Read and write kar den -> totaly 19 sab ko 
16. Generate Token -> click again -> genrate token -> copy token -> GITHUB_PAT=*****************************
17. past in (.env) file that api key
18. in Agent SDK code -> import os -> copy envoirment varibale of that github key and -> GITHUB_PAT=os.getenv("GITHUB_PAT") 
19. give prompt to agent -> input="make a new repo of name 'Shoaib_MCP_Testing_Repo'"
20 another prompt -> input="make a new repo with readme.md file. repo named will be 'AGENT_REPO_CREATE_From MCP' and write a text in readme.md file of 'Hello i am shoaib now i create This repo from my Agent in One command readme.md file'"






















