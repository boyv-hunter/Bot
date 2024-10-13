from flask import Flask, request, jsonify, render_template
from fbchat import Client, ThreadType

app = Flask(__name__)

# Flask Route to send message
@app.route('/send_message', methods=['POST'])
def send_message_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    thread_id = data.get('thread_id')
    message = data.get('message')
    
    # Create Facebook session
    session = Client(username, password)
    
    try:
        sent = session.sendMessage(message, thread_id=thread_id, thread_type=ThreadType.USER)
        if sent:
            return jsonify({'response': 'Message sent successfully!'})
        else:
            return jsonify({'response': 'Failed to send message'})
    except Exception as e:
        return jsonify({'response': str(e)})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        thread_id = request.form['thread_id']
        message = request.form['message']
        
        # Create Facebook session
        session = Client(username, password)
        
        try:
            sent = session.sendMessage(message, thread_id=thread_id, thread_type=ThreadType.USER)
            if sent:
                return 'Message sent successfully!'
            else:
                return 'Failed to send message'
        except Exception as e:
            return str(e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
