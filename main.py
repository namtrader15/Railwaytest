from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your Flask app on Railway!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Lấy giá trị PORT từ biến môi trường, mặc định là 5000 nếu không có
    app.run(host='0.0.0.0', port=port)
