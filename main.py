import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session
from model import Donation, Donor 

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()


@app.route('/')
def home():
    """Returns the homepage for mailroom"""
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    """Gets all donation from database
       and return page with donation"""
    donations = Donation.select()    
    return render_template('donations.jinja2', donations=donations)


@app.route('/new_donation', methods=['POST', 'GET'])
def create():
    """Add new donation to database"""
    if request.method == 'POST': 
        donor = request.form['donor'] 
        amount = int(request.form['amount']) 
        saved_donor = Donor.select().where(Donor.name == donor).get() 
        Donation(donor=saved_donor, value=amount).save() 
        return redirect(url_for('all')) 
    return render_template('new_donation.jinja2') 

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    host = os.environ.get("HOST", "127.0.0.1")
    app.run(host=host, port=port)
    
#    app.run(host='0.0.0.0', port=port)

