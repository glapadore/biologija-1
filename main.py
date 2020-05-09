from flask import Flask, render_template, request
import pusher
app = Flask(__name__)

pusher_client = pusher.Pusher(
  app_id='998247',
  key='5f0e6caa364c3b0742a0',
  secret='df2bba74bcab836741be',
  cluster='eu',
  ssl=True
)
@app.route('/chat')
def chat():
    pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
    return render_template('chat.html')


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


