from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField
from wtforms.validators import Required, Email, EqualTo
import email_validator
from ..models import Voter
from wtforms import ValidationError

class LoginForm(FlaskForm):
    passport = StringField('ID or Passport Number',validators=[Required()])
    first_name = StringField('First Name',validators =[Required()])
    last_name = StringField('Last Name',validators =[Required()])
    location = SelectField('County',choices=[("","Pick an Option"),("nairobi","Nairobi"),("mombasa","Mombasa"),("garissa","Garissa"),("kilifi","Kilifi"),("laikipia","Laikipia")],validators =[Required()])
    submit = SubmitField('Submit')     

    def validate_passport(self,data_field):
        if Voter.query.filter_by(passport=data_field.data).first():
            raise ValidationError('There is an account with that ID number')
        

            