from fastapi import FastAPI


app = FastAPI()

num = 0  # Iska example aisy ley sakty hain ke value hmesha dosri jagah se aa rhi hai but hmari request static hai jese weather API hmesha aik jesa mosam nahi btaegi dynamicly change hoga data.

@app.get("/") # Statless hai iska matlab har request new request hogi jo aegi.
async def get_function(): 
    # weather API
    # database
    # etc...
    
    global num
    num = num + 1 # Har request new hogi lekin ye variable ki increment hogi har new request pe kiyun ke ye bahar define hai iska request se koi lena dena nahi.
    
    return {
        "num": num,
        "message": "This is a get function request"
    }