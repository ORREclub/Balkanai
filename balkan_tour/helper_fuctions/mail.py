# import os
# from flask import Flask, render_template, request, redirect, url_for
# from flask_mail import Mail, Message
# from main import Session
# from models import Tour, Client
#
# app = Flask(__name__)
#
# čia jau reks kai įserverį įsikelsiu pasidaryti
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
#
# mail = Mail(app)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)