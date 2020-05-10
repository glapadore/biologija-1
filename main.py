from flask import Flask, render_template

app = Flask(__name__)


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

@app.route('/cats.html')
def cats():
    return render_template('cats.html')

if __name__ == '__main__':
    app.run(debug=True)


