from flask import Flask, render_template, json, jsonify, request

import chats

app = Flask(__name__)


#------------- 

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/saturs')
def saturs():
    return render_template('saturs.html')

@app.route('/bilde')
def bilde():
    return render_template('bilde.html')

@app.route('/chats')
def index_lapa():
  return render_template('chats.html')


@app.route('/chats/lasi')
def ielasit_chatu():
  return chats.lasi()


@app.route('/chats/suuti', methods=['POST'])
def suutiit_zinju():
  dati = request.json
  
  chats.pieraksti_zinju(dati)

  return chats.lasi()

if __name__ == '__main__':
    app.run(debug=True)


