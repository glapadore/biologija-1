import pusher
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'

pusher_client = pusher.Pusher(
  app_id='APP_ID',
  key='APP_KEY',
  secret='APP_SECRET',
  cluster='us2',
  ssl=True
)

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    message = db.Column(db.String(500))

@app.route('/')
def index():

    messages = Message.query.all()
    
    return render_template('index.html', messages=messages)


@app.route('/message', methods=['POST'])
def message():

    try:

        username = request.form.get('username')
        message = request.form.get('message')

        new_message = Message(username=username, message=message)
        db.session.add(new_message)
        db.session.commit()

        pusher_client.trigger('chat-channel', 'new-message', {'username' : username, 'message': message})

        return jsonify({'result' : 'success'})
    
    except:

        return jsonify({'result' : 'failure'})

   
#-----------------------------------------------------------------------------------------------

@app.route('/')
def home():
    return render_template('virslapa.html')


@app.route('/saturs')
def saturs():
    return render_template('saturs.html')

@app.route('/bilde')
def bilde():
    return render_template('bilde.html')


if __name__ == '__main__':
    app.run(debug=True)


