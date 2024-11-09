from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # HTML web page

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if user_message:
        messages = [
            {'role': 'user', 'content': user_message},
        ]
        
        # model Call
        response = ollama.chat(model='llama3.2', messages=messages)
        return jsonify({'response': response['message']['content']})
    return jsonify({'error': 'No message provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
