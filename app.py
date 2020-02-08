from flask import Flask,jsonify,request,redirect,url_for,render_template,session
import pandas as pd
from matplotlib import pyplot as plt

from sqlalchemy import create_engine
import mysql.connector

# import pymysql

# from flask_wtf.csrf import CSRFProtect
# from flask_sqlalchemy import SQLAlchemy
# from modules.admin.view import admin
# from db import db

# from flask_wtf import csrf

app = Flask(__name__)
# csrf = CSRFProtect(app)
# csrf.exempt("register")
# app.config['FLASK_ENV'] = "development"
# app.config['WTF_CSRF_CHECK_DEFAULT'] = False
# FLASK_ENV=development
app.debug = True
app.secret_key = "sljkdfksdfklsjdbnfsdfsdfk98123798123jsdkasdjf"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://mahmoud:12345@localhost/music"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#tamrin 1
@app.route("/")
def index():
    # titanic = "titanic.csv"
    # airbase = "airbase_data.csv"
    # flow = "flowdata.csv"
    # melb = "melb_data"
    # file_name = "static/data/titanic.csv"
    # data_set_name = "titanic.csv"

    name = request.args.get("name")

    if name == "titanic" :
        file_name = "static/data/titanic.csv"
        data_set_name = "titanic.csv"
    elif name == "airbase":
        file_name = "static/data/airbase_data.csv"
        data_set_name = "airbase_data.csv"
    elif name ==   "flow":
        file_name = "static/data/flowdata.csv"
        data_set_name = "flowdata.csv"
    elif name ==   "melb":
        file_name = "static/data/melb_data.csv"
        data_set_name = "melb_data.csv"
    else:
        return "Not Found"

    df = pd.read_csv(file_name)
    head_data = df.head()
    columns = list(df.columns)
    print(df.head())
    print()
    data = []
    # for key, row in head_data.iteritems():
    #     print(row)
    #     print("--------------------------")

    for i in head_data.itertuples():
        print(i)
        data.append(list(i))


        # for v in list(row):
        #     print(v)
    # for ind,value in cols.iteritems():
    #     print(ind,value)
    # print(data)
    return render_template("data.html", data = {"data_set_name":data_set_name,"rows":data,"columns":columns})


if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=8088,debug=True)

