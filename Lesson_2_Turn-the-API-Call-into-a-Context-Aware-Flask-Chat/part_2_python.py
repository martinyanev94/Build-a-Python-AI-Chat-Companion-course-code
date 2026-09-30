from flask import Flask, request, render_template

from openai import OpenAI

import os



app = Flask(__name__)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

model_engine = "gpt-3.5-turbo"

conversation_history = []



@app.route("/")

def index():

    return render_template("index.html", history=conversation_history)
