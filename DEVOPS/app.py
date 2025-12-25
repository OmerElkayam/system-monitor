from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <body>
            <h1>CTRTech System Monitor</h1>
            <p>Click here to check status: <a href="/status">/status</a></p>
        </body>
    </html>
    """

@app.route('/status')
def check_status():
    memory_percent = psutil.virtual_memory().percent
    
    if memory_percent > 80:
        return f'<h1 style="color:red;">⚠️ WARNING: High Memory Usage! ({memory_percent}%)</h1>'
    else:
        return f'<h1 style="color:green;">✅ System OK. Memory usage: {memory_percent}%</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

