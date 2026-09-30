    assistant_text = response.choices[0].message.content

    conversation_history.append({

        "role": "assistant",

        "content": assistant_text

    })

    return render_template(

        "index.html",

        history=conversation_history

    )
