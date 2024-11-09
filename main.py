import ollama

response = ollama.chat(
    model='llama3.2',  # llama 3.2 3B model
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}]
)

print(response['message']['content'])



