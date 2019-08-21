#!/usr/bin/python
print('Content-type: text/html\r\n\r')

from flask_frozen import Freezer
from flask import Flask
from flask_mail import Mail, Message
from flask import render_template, current_app
from flask import request, jsonify, redirect, Response
import json


app = Flask(__name__)
freezer = Freezer(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'gk.gurmeet1998',
    "MAIL_PASSWORD": 'gurmeetkaur01'
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sendName', methods=['POST'])
def sendEmail():
    if request.method == "POST":
        data = request.get_json()
        print('working')
        msg = Message(subject="Random Name",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["<steffykaur@gmail.com>"],
                      body=data)
        mail.send(msg)
        print(data)
        return data
        

if __name__ == '__main__':
    freezer.freeze()
    
    

