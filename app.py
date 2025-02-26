from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_mail import Mail, Message
import random
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'enter your email address'
app.config['MAIL_PASSWORD'] = 'enter yot password'  # Use App Password if needed
app.config['MAIL_DEFAULT_SENDER'] = 'enter your email address'

mail = Mail(app)

# Store OTPs temporarily
otp_storage = {}

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    email = request.form['email']
    
    # Generate OTP
    otp = random.randint(100000, 999999)
    otp_storage[email] = otp
    
    # Send Email
    msg = Message('Your OTP Code', recipients=[email])
    msg.body = f'Your OTP is: {otp}'
    mail.send(msg)
    
    flash("OTP sent successfully! Check your email.", "success")
    return render_template('verify.html', email=email)

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    email = request.form['email']
    user_otp = request.form['otp']

    if email in otp_storage and otp_storage[email] == int(user_otp):
        flash("OTP verified successfully!", "success")
        return redirect(url_for('home'))  # Redirect to the home page
    else:
        flash("Invalid OTP! Try again.", "danger")
        return render_template('verify.html', email=email)
    
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
