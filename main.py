from flask import Flask, request, jsonify
import fbchat
from fbchat import ThreadType

app = Flask(__name__)

# Create Facebook session
session = fbchat.Session()

# Flask Route to send message
@app.route('/send_message', methods=['POST'])
def send_message_route():
    data = request.get_json()
    thread_id = data.get('thread_id')
    message = data.get('message')
    app_state = data.get('app_state')
    session.set_app_state(app_state)
    try:
        sent = session.sendMessage(message, thread_id=thread_id, thread_type=ThreadType.USER)
        if sent:
            return jsonify({'response': 'Message sent successfully!'})
        else:
            return jsonify({'response': 'Failed to send message'})
    except fbchat.FBchatException as e:
        return jsonify({'response': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
