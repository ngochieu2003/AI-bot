from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

# response =client.chat.completions.create(
#   model="gemma2:9b",
#   messages=[
#       {"role": "user", "content": "Hello, bot!"}
      
#   ]
# )
# reply = response.choices[0].message.content
# print(reply)
messages = []  
while True:
    print(messages)
    user_input = input("You:" )
    if user_input == "exit":
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model = "gemma2:9b",
        stream=True,
        messages=messages
    )
    bot_reply = ""
    for chunk in response:
        bot_reply += chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "", end = "", flush = True)
    messages.append({"role": "assistant", "content": bot_reply})