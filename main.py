from flask import Flask, render_template, request 
import joblib

app=Flask(__name__)

#load the model
model=joblib.load('model/diabitic_80.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['post'])
def data():
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')

    print(type(preg))

    result=model.predict([[preg , plas , pres, skin , test, mass , pedi, age]])

    

    if result[0]==1:
        data= 'Person is diabetic'
    else:
        data = 'Person is not diabetic'

    return render_template('predict.html', data=data) #sending the method from front end to back end. Always define the method.

# @app.route('/images')
# def image():
#     return 'This is the image page'

# @app.route('/contact')
# def contact():
#     return 'Contact us'

# @app.route('/aboutus')
# def aboutus():
#     return 'About us'


app.run(debug=True)#debug is used to avoid loading the page again and again