from flask import Flask,render_template,request
import numpy as np
import pickle


model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('indexx.html',result=1)

#@app.route('/predict',methods=['POST'])
@app.route('/predict',methods=['POST'])
def predict_placement():
    intern = int(request.form.get('intern'))
    cgpa = float(request.form.get('cgpa'))
    hostel = int(request.form.get('hostel'))
    backlog = int(request.form.get('backlog'))

    result = model.predict(np.array([intern,cgpa,hostel,backlog]).reshape(1,4))

    if result[0]==1:
        result='Placed'
    else:
        result='Not Placed'
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)