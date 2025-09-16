from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import os

app = Flask(__name__)

CORS(app, resources={r"/send_email": {"origins": "http://localhost:5173"}})

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message_body = data.get('message')

        if not name or not email or not message_body:
            return jsonify({'success': False, 'message': 'All fields are required.'}), 400

        msg = Message('Portfolio Contact Form Submission',
                      recipients=['your_email@example.com'])
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"

        mail.send(msg)

        return jsonify({'success': True, 'message': 'Message sent successfully!'}), 200

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)