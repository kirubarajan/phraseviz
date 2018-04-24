from flask import Flask, request, render_template, session, flash
from distances import hamming, euclidean, manhattan

app = Flask(__name__, static_folder='static')

app.secret_key = 'You Will Never Guess'

@app.route('/', methods=['GET', 'POST'])
def splash():
	session['sentence1'] = request.args.get('sentence1')
	session['sentence2'] = request.args.get('sentence2')
	return render_template("index.html", sentence1=session['sentence1'], sentence2=session['sentence2'])

@app.route('/similarity')
def research():
  	return render_template("similarity.html", sentence1=session['sentence1'], sentence2=session['sentence2'])

if __name__ == "__main__":
  	app.run(debug=True)