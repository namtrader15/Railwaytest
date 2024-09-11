from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your Flask app on Railway!"

# python web server
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
