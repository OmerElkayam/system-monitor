from flask import Flask
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    # דף בית פשוט עם לינק לבדיקה
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
    # קבלת אחוז השימוש בזיכרון
    memory_percent = psutil.virtual_memory().percent
    
    # הלוגיקה המלאה
    if memory_percent > 80:
        # מחזיר הודעה אדומה אם יש עומס
        return f'<h1 style="color:red;">⚠️ WARNING: High Memory Usage! ({memory_percent}%)</h1>'
    else:
        # מחזיר הודעה ירוקה אם הכל תקין
        return f'<h1 style="color:green;">✅ System OK. Memory usage: {memory_percent}%</h1>'

if __name__ == '__main__':
    # הרצה על כל הממשקים כדי שדוקר יוכל לגשת
    app.run(host='0.0.0.0', port=5000)
    
