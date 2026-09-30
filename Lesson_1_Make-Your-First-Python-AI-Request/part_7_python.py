question = "Explain photosynthesis in one sentence."

response = client.chat.completions.create(

    model="gpt-3.5-turbo",

    messages=[{"role": "user", "content": question}],

 )
