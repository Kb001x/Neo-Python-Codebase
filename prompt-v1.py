from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an AI assistant, skilled in explaining complex programming, physics & engineering concepts succinctly in 100 words or less where possible,"},
    {"role": "user", "content": "Hey, do you know kotlin?"}
  ]
)

print(completion.choices[0].message)