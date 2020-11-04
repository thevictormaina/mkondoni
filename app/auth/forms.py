from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField
from wtforms.validators import Required, Email, EqualTo
import email_validator
# from ..models import 
from wtforms import ValidationError

class LoginForm(FlaskForm):
    passport = StringField('ID or Passport Number',validators=[Required()])
    fName = StringField('First Name',validators =[Required()])
    lName = StringField('Last Name',validators =[Required()])
    county = SelectField('County',choices=[("nairobi","Nairobi"),("mombasa","Mombasa"),("garissa","Garissa"),("kilifi","Kilifi"),("laikipia","Laikipia")],validators =[Required()])
    submit = SubmitField('Submit')     

    def validate_passport(self,data_filed):
        pass

            