from openai import OpenAI

client = OpenAI(
  api_key="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"
)

prompt = "How is the weather in Klagenfurt?"

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  max_tokens=100,
  store=True,
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message);
