from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import pusher

pusher_client = pusher.Pusher(
  app_id='998247',
  key='5f0e6caa364c3b0742a0',
  secret='df2bba74bcab836741be',
  cluster='eu',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})

#------------- 

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


