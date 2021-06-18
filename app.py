from flask import Flask,render_template,request
import os
from flask.json import jsonify
import openai
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.


openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template("index.html")




@app.route("/openaiAPI",methods=['post'])
def openaiAPI():
    
    prompt = "slack is the"
    engine = "curie"
    temprature = 0.6,
    max_token = 20,
    jsonData = request.json

    try:
        prompt = jsonData['prompt']
        engine = jsonData['engine']
        temprature = jsonData['temprature']
        max_token = jsonData['max_token']


    except Exception as e:
        print(e)
        

    print(prompt,engine,temprature,max_token)

    # response = openai.Completion.create(
    # engine=engine,
    # prompt=prompt,
    # temperature=temprature,
    # max_tokens=max_token,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0)

    

    return jsonify({"response":"response"})