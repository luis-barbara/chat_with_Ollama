# Steps to Create a Chat on a Web Page Using an Ollama Model (In this case, the Llama 3.2 3B model), through a Docker Container:
![chat_with_Ollama_pic](https://github.com/user-attachments/assets/eccc0074-7f6e-40fd-8b10-7bc71e09fa22)


**1-** Visit the Ollama Documentation: Visit the official Ollama website: https://ollama.com

**2-** Install Docker: Install Docker on your system by following the installation guide for your operating system.

**3-** Go to Docker Hub (Ollama): Visit the Ollama Docker page on Docker Hub: https://hub.docker.com/r/ollama/ollama and read the documentation to download the image to Docker.

**4-** Download the Ollama Image: From the Docker terminal, you can run the following command to download the latest Ollama image:
```bash
docker pull ollama/ollama
```  

**5-** Run the Ollama Container: After downloading the Ollama image, the next step is to create and run a container using that image. The container is where the Ollama model will run.

**6-** Steps to Run the Ollama Container:
To start the Ollama container, execute the following command:
```bash
docker run -d -p 11434:11434 --name Ollama ollama/ollama
```  

This command does the following:
docker run: Creates and runs a new container from an image.
"-d": Runs the container in "detached" mode (in the background).
"-p 11434:11434": Maps port 11434 of the container to port 11434 on your computer, allowing you to connect to the service.
"--name Ollama": Names the container "Ollama".
"ollama/ollama": Specifies the image to use to create the container.

**7-** Verify the Container is Running:
To confirm that the container was created and is running properly, use the command:
```bash
docker ps
```
The Ollama container should appear in the list of active containers.

**8-** Download the Llama3.2 Model Inside the Container:
Now that the container is running, pull the Llama3.2 model into the container using the following command:
```bash
docker exec -it Ollama ollama pull llama3.2
```
This command downloads the Llama3.2 model (or another desired model) directly into the Ollama container.

**9-** Verify if the Model Was Successfully Downloaded:
To confirm that the model was downloaded correctly, use the command:
```bash
docker exec -it Ollama ollama list models
```
This will display a list of available models, including Llama3.2.

**10-** Open VS Code and Create a Folder (e.g., ‘chat_with_Ollama’)

**app.py:**
This Python script allows for a continuous conversation with the Llama model, where the user interacts with the model, and the responses are displayed in real-time via the terminal, until the user types "exit" or "quit" to stop.

**main.py:**
This script sends a question to the Llama 3.2 model ("Why is the sky blue?") and prints the model's generated response.

**server.py:**
This script creates a Flask API that receives a prompt via POST, generates a response (simulated for now), and returns the generated text in JSON format.

**chat_app.py:**
This file uses the following languages and libraries:
Python: The primary language used for backend logic, handling HTTP requests, and interacting with the Ollama model.
Flask: A micro web framework in Python, used to create the server and define HTTP routes. In chat_app.py, Flask is used to:
The / route renders the homepage (index.html).
The /chat route receives user messages, interacts with the Ollama model, and sends the responses back to the frontend.
JSON: Flask uses JSON format for data exchange between the backend and frontend. User messages are sent as JSON objects, and the model's response is also returned in JSON format. Summary: chat_app.py is a Python backend using Flask to create a web server that receives requests, interacts with the Ollama model, and sends responses back to the user interface.

**index.html:**
This file creates a simple chat interface where the user can send messages to the backend, and the model's responses are displayed in the chatbox, allowing continuous interaction with the Flask application.
The following languages are used:
HTML (HyperText Markup Language): For structuring the webpage content, such as the title, chatbox, message input field, and send button.
CSS (Cascading Style Sheets): For styling the page, defining colors, sizes, fonts, borders, and layout of elements (e.g., chatbox and input fields).
JavaScript: For implementing interactive functionality, such as sending user messages to the backend via fetch, displaying the responses in the chatbox, and enabling automatic scrolling to the latest message.

**11-** Prepare the Python Environment to Run Flask:
Activate the Python virtual environment (if using one):

On Windows:
```bash
.\venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

**12-** Install Dependencies:
Ensure Flask and the Ollama library are installed in your Python environment:
```bash
pip install Flask ollama
```

**13-** Use the Command in VS Code Terminal to Interact with the Docker Container:
To interact with the running Docker container and pull the Llama3.2 model:
```bash
docker exec -it Ollama ollama pull llama3.2
```

**14-** Run the chat_app.py Script:
Execute the script by running:
```bash
python chat_app.py
```

**15-** Open the Web Browser and Test the Chat:
Open your browser and go to the web application, then test the chat by asking questions, for example, "Why is the sky blue?".


## Notes:
Model: Llama 3.2 (3B)
- Parameters: 3 billion
- Size: 2.0GB	
- Hardware Requirements:
  - CPU: Multicore processor
  - RAM: Minimum of 16 GB recommended
  - GPU	NVIDIA RTX series (for optimal performance), at least 8 GB VRAM
  - Storage	Disk Space: Sufficient for model files 

Model: Llama 3.2 (1B)
- Parameters:	1 billion	
- Size: 1.3GB	
- Hardware Requirements:
  - CPU: Multicore processor
  - RAM: Minimum of 16 GB recommended
  - GPU	NVIDIA RTX series (for optimal performance), at least 4 GB VRAM
  - Storage	Disk Space: Sufficient for model files 

For this case I run the Llama 3.2 3B model on a machine with an Intel Core i7-6700HQ and 8GB of RAM, which is under the recommended specifications for optimal performance. While the model may still work, the response from the chat was very slow.

![7](https://github.com/user-attachments/assets/15d497de-7d29-414b-92db-59edcc8fac82)
![8](https://github.com/user-attachments/assets/3bacb801-c485-4689-87eb-fdabe1ec8290)
![9](https://github.com/user-attachments/assets/c2650f9e-2fd7-4b70-8d45-b6f606912f2c)


