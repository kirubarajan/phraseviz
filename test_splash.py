from flask import Flask, request, render_template
from distances import hamming, euclidean, manhattan

app = Flask(__name__, static_folder='static')

@app.route('/')
def splash():
  return render_template("index.html")

@app.route('/similarity', methods=['GET', 'POST'])
def research():
  sentence1 = request.args.get('sentence1')
  sentence2 = request.args.get('sentence2')
  return render_template("similarity.html", sentence1=sentence1, sentence2=sentence2)

if __name__ == "__main__":
  app.run(debug=True)