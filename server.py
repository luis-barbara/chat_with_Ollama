from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v1/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')
    # Logic to generate text using the model
    generated_text = f"Texto gerado a partir do prompt: {prompt}"  # Replace with model logic
    return jsonify({"generated_text": generated_text})

if __name__ == '__main__':
    app.run(port=11434)

