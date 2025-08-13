# FastAPI se import kar rahe hain, taaki hum API bana sakein
from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI ka ek instance bana rahe hain
app = FastAPI()


class GetData(BaseModel):
    name: str
    

# Yeh ek GET request ka endpoint define kar raha hai jo root ("/") pe chalega
@app.get("/{age}")  # request url -> http://127.0.0.1:8000/20 -> last 20 is age query paramter value.
def get_function(name: GetData, age: int):  # Ek function define kiya jo execute hoga jab yeh endpoint hit hoga
    return f"name I am {name} and my age is {age}."  # Yeh function ek JSON response return karega



# GET request mein bhi ham body or header bhej sakty hain 
# hamne isko get request karty huy body mein is function paramter ki value bhej di to ye ley leta hai.
# browsers GET request mein data bhejna ccept nahi karte but iska matlab ye nahi ke bheja nahi jaa sakta ham bhej sakty hain
# jese postman support karta hai is cheez ko.


#NOTES
# uv init
# uv run main.py
# uv add fastapi[standard]
# write code
# active vertual envoiment
# run code -> fastapi dev main.py