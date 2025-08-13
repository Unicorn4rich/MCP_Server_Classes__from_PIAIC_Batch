
1. protocol = rule (follow internet protocol e.g" http , https , ftp , sftp , websocket , ssh , dns ")

2. http = hypertext tranfer protocol    -> Internet par data ko travel krwany ke liye aik protocol http bhi hai. 
     - Methods
     - path/address/url
     - Headers           -> kis type ka data ham samny waly ko send kar rhy hain body mein rakh kar.
     - Body (optional)

3. Internet = Global Road

4. RestApi = structure way to design APIs for websites on HTTP requests.   -> RestApi http ka hi aik structure form hai.
     - rules for using method
     - always return json response
     - stateless                    -> har request new request hogi purani request yad nahi rakhega.

MCP Server    -> POST request mein (version, method, params, id) ye sari data or types lazim denge sirf jsonrpc mein.
     - less server load 
     - MCPserver owner will do maintanance
     - open source -> tool (free of cost)

MCP CLient
     - always use http POST method
     - always use jsonRpc message structure

MCPStdio ✅                      -> For development Run in Local laptop envoirment -> Standard Input + Standard Output
     - No need of network to run
     - used for local development

MCPsse ❌    -> MCP server-sent-event 
     - stateless / stateful
     - HTTP request -> POST (foran close ho jata he, from client)
     - HTTP request -> GET (jab tak close nahi hota jab tak kam complete na ho jaye from client)

MCPstreamable_http:
 -User/client ne POST request ki or wo isme recived karli or request khatam sttless hony ki wajah se.
 -Server ne Pipline create ki or kaha ab Mai GET ki request mein tumhe streaming ki form mein data deta jaonga.     

MCPstreamable_http ✅ ( (stateless) , (stateful -> sessionId) ) -> statefull option light ya net band to ye sab save.
     - can run on network
     - can revive by the help of session    
     - HTTP request -> POST (foran close ho jata he) 
     - HTTP request -> GET (jab tak close nahi hota jab tak kam complete na ho jaye.)


Websocket  -> Aik hi request mein data aa jaa rha hai isme
     - bi-directional handles request & responce


http request status code:
   - 200 = OK hai sab or data return bhi lata hai.
   - 201 = POST request kar ke data Create kiyya jo client ne bheja successfully mil gaya or return mein kuch nahi dunga.