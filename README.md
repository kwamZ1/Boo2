# Boo2
Expert Shippers doc 
Cue Column	Notes
Libraries Imported	Flask, socketio, and eventlet
Flask App Creation	app is initialized as a Flask application
Socket.IO Server Init	Socket.IO server is initialized using the Flask app instance
HTML Structure	Heading, Input field, Enter and Reset buttons, Display area for messages
JavaScript Events	connect event logs connection status; message event appends received message to display area
Button Event Listeners	"Enter" button emits 'message' event with input data; "Reset" button clears input field
Message Event Handler	Checks if data contains "ship" (ignores case); emits custom message if true
Server Execution	Application runs using eventlet WSGI server
