1. Protocol             => Rule (follow http methods)
2. http                 => Transport
3. RestApi              => Web http request transport
4. Jsonrpc              => message format
5. MCP Stdio            => Standard input/output (local mcp development)
6. MCP sse (deprecated) => server sent event (double http request open -> POST/listen, GET/response)
7. MCP streamable_http  => (single http request open -> POST)

----------------------------------------------------------------------------------------------
Notes

1. Protocol  => Rule:
   rules regulations kaam ko karne ka sahi tariqa.

2. http => Transport:
   (Client) se aik gari jaa rhi hai (Server) tak wo gari jo road use kar rhi hai wo hai hmara internet or jo gari hai wo khud http ki request hai or jab server ke pass jati hai to server usme json/response/Web/HTML ka code rakh kar wapas bhejta hai jo ke hmare browser par aa kar render hota hai or show hota hai.

3. POST request materials:
   URL(www.xyz.com), headers(application/json), body(jsonRpc).

4. MCP => POST: 
   methods -> (GET/POST/DELETE/PUT) -> MCP mein POST ki request use hogi witth (URL, headers, body)
   headers matlab additional information ke request mein data json/text ya kisi or form mein bhej rhy hain server ko taky
   usy idea ho data kis form mein aa rha hai. or jo data hai wo body/payload hota hai jo ke json mein hota hai aksar
   headers mein ham btaty hain data kis form mein bhej rhy hain or body mein us form ka data rakh kar server ko bhej dety hain.
   MCP Server ke pass hmari POST ki request hmesha (jsonrpc) message ki format mein hoga wrap kar ke yahi rule hai

5. DNS -> URL -> (187.00.32.3434)
   Hamne ai website bnai jisko browser pe open kiyya or uska jo url hai wo hai url(187.00.32.3434) ye numbers wala ab hamne DNS se kaha ke wo hmari is website ko koi naam dey taky ham apni website ko numbers se nahi naam se pehchan paen jese -> shoaib portfolio website. or DNS alag alag names provide karta hai sab ko unique jo ye naam deta hai unhy ham domain kehty hain.   

6.    