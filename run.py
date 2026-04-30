from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Dominik! HabitMind Backend is running.'

if __name__ == '__main__':
    # Bind to 0.0.0.0 to allow access from outside the Docker container.
    app.run(host='0.0.0.0', port=5000)
    