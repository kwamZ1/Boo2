# Import necessary libraries
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
import openai
import os

openai.api_key = "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"

# Create a Flask app instance
app = Flask(__name__)
# Enable CORS (Cross-Origin Resource Sharing) for the Flask app
CORS(app)
# Create a SocketIO instance for real-time communication and allow all origins
socketio = SocketIO(app, cors_allowed_origins='*')

# Define the route for the main page, which will render the 'index.html' template
@app.route('/')
def index():
    return render_template('index.html')

# This function listens for 'message' events on the SocketIO instance
@socketio.on('message')
def handle_message(data):
    # Print the received message data
    print(f'Received message: {data}')

    if "ship" in data['data'].lower():
        # Send the user's message to the ChatGPT API
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"User: {data}\nChatbot:",
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["User:"]
        )

        # Extract the generated response from the API result
        chatbot_response = response.choices[0].text.strip()

    else:
        chatbot_response = "Please include the keyword 'ship' in your message for more information."

    # Emit a 'response' event with the chatbot's response to all connected clients
    socketio.emit('response', {'data': chatbot_response})


# Run the Flask app with the SocketIO instance
if __name__ == '__main__':
    socketio.run(app)
