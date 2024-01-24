from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/predict', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
      sepal_length = float(request.form['SL'])
      sepal_width = float(request.form['SW'])
      petal_length = float(request.form['PL'])
      petal_width = float(request.form['PW'])
      result = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
      
    return render_template('index.html', **locals())



if __name__ == '__main__':
    app.run()