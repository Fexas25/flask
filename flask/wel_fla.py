from flask import Flask, render_template, redirect, request
from forms import DataCollectForm
import os

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
        name = form.name.data
        pnumber = form.pnumber.data
        email = form.email.data
        degree = form.degree.data
        study_feeling = form.study_feeling.data
        grade_last_exam = form.grade_last_exam.data
        improvement = ', '.join(form.improvement.data)
        differences = form.differences.data
        changes = form.changes.data

        # Store the form data in the data.txt file
        with open('data.txt', 'a') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Pnumber: {pnumber}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Degree: {degree}\n")
            file.write(f"Study Feeling: {study_feeling}\n")
            file.write(f"Grade Last Exam: {grade_last_exam}\n")
            file.write(f"Improvement: {improvement}\n")
            file.write(f"Differences: {differences}\n")
            file.write(f"Changes: {changes}\n")
            file.write("\n")

        return redirect('/success')
    return render_template('datacollect.html', form=form)

if __name__ == '__main__':
    wel_fla.run(debug=True)
