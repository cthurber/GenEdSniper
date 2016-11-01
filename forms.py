# from flask_wtf import Form
from wtforms import Form, TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, SelectMultipleField, BooleanField, StringField, validators, ValidationError

from gen_sniper import get_requirement_titles

class ContactForm(Form):

    diversity_us = BooleanField('Diversity US')
    writing_intensive = BooleanField('Writing Intensive')
    interdisc_breadth = BooleanField('Interdisciplinary Breadth')
    natural_sci = BooleanField('Natural Sciences')
    humanities = BooleanField('Humanities')
