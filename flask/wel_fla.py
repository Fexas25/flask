from flask import Flask, render_template, redirect, request
from forms import DataCollectForm

wel_fla = Flask(__name__)

wel_fla.config['SECRET_KEY'] = 'your_secret_key_here'

@wel_fla.route('/')
def welcome_flask():
    return render_template('welcome_flask.html')

@wel_fla.route('/information')
def information():
    return render_template('information_flask.html')

@wel_fla.route('/success')
def success():
    return render_template('success.html')

@wel_fla.route('/datacollect', methods=['GET', 'POST'])
def datacollect():
    form = DataCollectForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('datacollect.html', form=form)

if __name__ == '__main__':
    wel_fla.run(debug=True)