from flask import Flask, request, render_template, session, flash
from distances import hamming, euclidean, manhattan

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def splash():
	if request.method == 'POST':
		s1 = request.args.get('sentence1')
		s2 = request.args.get('sentence2')
		return render_template("index.html", s1=s1, s2=s2)
	return render_template("index.html")

@app.route('/similarity')
def research():
  	return render_template("similarity.html", sentence1=session['sentence1'], sentence2=session['sentence2'])

if __name__ == "__main__":
  	app.run(debug=True)