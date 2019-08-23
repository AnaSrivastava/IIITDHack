from flask import Flask,jsonify,request,make_response
import json
import os
import pickle
from flask_cors import CORS, cross_origin

def someFun(gender,Age,Height,blo):
    if gender=="Male":
        hh="Male.pkl"
    elif gender=="Female":
        hh="Female.pkl"
    print("ststs")
    clf = pickle.load(open(hh,"rb"))
    print("clfclf")
    y_pred=clf.predict([[float(Age),float(Height),float(blo)]])
    return(float(y_pred))


app = Flask(__name__)
cors = CORS(app)
@app.route('/psp', methods=['POST'])
def getReviewDetails():
    try:
        gender = request.json['value']
        Age=request.json['age']
        Height=request.json['Height']
        blo=request.json['Weight']
        print(gender)
    except:
        return make_response(jsonify({'error' :'bad request'}),400)
    try:
        cl=someFun(gender,Age,Height,blo)
    except:
        return make_response(jsonify({'error' :'internal server error'}),500)
        
    return make_response(jsonify({"cl": cl}),200)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=5004,debug=True)

