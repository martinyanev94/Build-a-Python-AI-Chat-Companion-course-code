@app.route("/get")

def get_bot_response():

    user_text = request.args.get("msg", "")

    conversation_history.append({

        "role": "user",

        "content": user_text

    })

    print("messages sent:", conversation_history)

    response = client.chat.completions.create(

        model=model_engine,

        messages=conversation_history

    )
