from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return {'status': 'running', 'app': 'Python Frontend'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
