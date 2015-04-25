from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email

class SignUpForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email', validators=[InputRequired(message="This field is required"), Email(message="Not a valid email address")])
    submit = SubmitField("Signup")