from openai import OpenAI


#  pip install openai 
#client = OpenAI()
# defaults to getting the key using os.environ.get("OPEN_API_KEY"
# if you saved the key under a differnt environment variable name, you can do something like: 
client = OpenAI(api_key="Open_API_KEY")

completion = client.chat.completions.create(
    model="gpt-40-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant skilled in general tasks."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)
