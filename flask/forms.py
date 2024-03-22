from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Email
from wtforms import SelectMultipleField
from wtforms import widgets

class DataCollectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    pnumber = StringField('Your Pnumber')
    email = StringField('Your email', validators=[DataRequired(), Email()])
    degree = SelectField('Which degree are you in?', choices=[('undergraduate', 'Undergraduate'), ('postgraduate', 'Postgraduate'), ('phd', 'PhD')])
    study_feeling = SelectField('How did you feel about your study?', choices=[('very_bad', 'Very Bad'), ('not_good', 'Not Good'), ('not_bad', 'Not Bad'), ('very_good', 'Very Good')])
    grade_last_exam = SelectField('What is your grade in the last exam?', choices=[('fail', 'Fail'), ('pass', 'Pass'), ('good_pass', 'Good Pass')])
    improvement = SelectMultipleField('How do you feel you can improve?(Multiple choice)', choices=[
        ('more_courses', 'Have more courses'),
        ('more_self_study', 'Have more self-study'),
        ('more_tutors', 'Have more tutors'),
        ('more_sources', 'Have more sources to study'),
        ('skillful_students', 'Meet more skillful students'),
        ('work_with_students', 'Work with other students'),
        ('change_exam_style', 'Change exam style')],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False),
        coerce=str
        )
    differences = TextAreaField('How do you think of the differences between university and high school?')
    changes = TextAreaField('What changes can you do now?')