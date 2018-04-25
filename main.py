from flask import Flask, request, render_template
from distances import hamming, euclidean, manhattan
# from nlp import similarity

class DistanceCalculator(object):
	def __init__(self, sentence1, sentence2):
		self.ham = hamming(sentence1, sentence2)
		self.euc = euclidean(sentence1, sentence2)
		self.man = manhattan(sentence1, sentence2)
		self.res = [self.ham, self.euc, self.man]

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def splash():
	sentence1 = request.args.get('sentence1')
	sentence2 = request.args.get('sentence2')
	temp = DistanceCalculator(sentence1, sentence2)
	res = temp.res
	return render_template("index.html", sentence1=sentence1, sentence2=sentence2, res=res)


if __name__ == "__main__":
  app.run(debug=True)