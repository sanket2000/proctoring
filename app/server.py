from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This should contain your WebRTC implementation

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
