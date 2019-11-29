from flask import Flask, render_template, request
from sklearn.externals import joblib
app = Flask(__name__)

@app.route("/")
def index():
    # return "Welcome to flask"
    return render_template('employee.html')

def employed(exp, emp):
    model=joblib.load('model_6.sav')
    value=model.predict([[exp, emp]])
    return value

@app.route("/prediction",methods=['GET','POST'])
def prediction_webpage():
    if request.method == 'POST':
        data=request.form
        exp = data['Years Experience']
        exp = int(exp)
        emp=data['Employed?']
        emp = int(emp)
        hired = employed(exp, emp)
        message = "Years of experience: " + str(exp)\
                  + ".\nEmployed status: "+ str(emp)\
                  +"\nShould you hire or not? "\
                  +str(hired)
        return message

    return render_template('employee.html')

if __name__=="__main__":
    app.run()
