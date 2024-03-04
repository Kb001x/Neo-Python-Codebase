from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an AI assistant, skilled in explaining complex programming, physics & engineering concepts succinctly."},
    {"role": "user", "content": "tell me how electricity works."}
  ]
)

print(completion.choices[0].message)