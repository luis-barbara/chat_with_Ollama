import ollama

def chat_stream():
    """
    Function that allows a continuous conversation with the Llama model using streaming.
    The loop will accept input until the user types 'exit', 'quit' or 'quit'.
    """
    messages = []  # List to store conversation history

    print("Hello! How can I help you today? (Type 'exit', 'exit' or 'quit' to exit)")

    while True:
        # Receives user input
        user_input = input('User: ')
        
       # Check if the user wants to exit
        if user_input.lower() in ['exit','quit']:
            print("Leaving...")
            break

       # Add user message to history
        messages.append({'role': 'user', 'content': user_input})

        try:
            # Make the request to the model with streaming enabled
            stream = ollama.chat(
                model='llama3.2',  # Model in use
                messages=messages,
                stream=True  # Streaming mode activated
            )

            content_out = ""  # Variable to accumulate the response

            # Display the response as the model generates
            for chunk in stream:
                content_out += chunk['message']['content']
                print(chunk['message']['content'], end='', flush=True)

            print("\n")
            
        except ollama.ResponseError as e:
            print(f"Error generating response: {e.error}")
            if e.status_code == 404:
                print("The model was not found. Please make sure the model is available.")
            continue


if __name__ == "__main__":
    chat_stream()
