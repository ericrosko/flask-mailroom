#!/usr/bin/env python3

import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()

@app.route('/')
def home():
    return redirect(url_for('all_donations'))

@app.route('/donations/')
def all_donations():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/add', methods=['GET', 'POST'])
def add_donation():

    # for key in request.session.keys():
    #     del request.session[key]

    if request.method == 'GET':
        return render_template('add.jinja2')


    input_donor_name = str(request.form['donorname'])
    input_amount = int(request.form['amount'])

    user = None
    msg = ""
    success = False
    error = ""

    try:
        # the line below appears to return a User type not an instance,
        # you must use get()
        # user = User.select().where(User.name == username)
        # user2 = User.select().where(User.name == username).get()
        # user = User.get(User.name == input_name)

        donor = Donor(name=input_donor_name)
        donor.save()
        donation = Donation(donor=donor, value=input_amount)
        donation.save()

        # msg = "add successful"
        success = True

    except Exception as e:
        msg = e
        # msg = "user does not exist"
        donor = Donor.get(name=input_donor_name)
        donation = Donation(donor=donor, value=input_amount)
        donation.save()
        success = True


    if success == True:
        return redirect(url_for('all_donations'))

    return render_template('add.jinja2', msg=msg)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

