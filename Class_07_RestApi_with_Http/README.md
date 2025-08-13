What is -> HTTP + FastApi + RestApi


1. HTTP Protocol -> internet par aik jagah se dosri jagah data ko pohnchana/travel krwana.
   http aik messagehai jo client karta hai server ko -> "janu data dey do" 

2. REST API:
   Methods correct use -> GET / Post / Patch / Delete jo inka kaam hai ye sirf wahi karenge statless resource identifier.
   RestApi http method mein hi kaam karta hai lekin ye pora architecture hai API ko design karne ka   

3. Server load
   Vertical Scalling -> aik hi server manage karega Or Horizental scalling mein ala alag servers manage karte hain. 
   3 alag alag servers par same websote ko host kiyya hua hai taky traffic manage kar saken but unka url bhi hamen alag alag milea 3eena ka iska solution ye hai ke ham aik or server laga dety hain (Load Balancer) isme 3eeno url aty hain or ye hamen single url deta hai or traffic ko alag alag url servers pe redirect ye khud karta rehta hai.
   Horizental scalling mein statless rakhna parta hai user requests ko or agr memory manage karni hai to database laga do.

4. HTTP         -> The protocol (rules) for communication.
5. HTTP Request -> A single message that follows HTTP rules
6. REST API     -> A design style for APIs that use HTTP requests in a structure way.