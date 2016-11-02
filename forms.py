# from flask_wtf import Form
from wtforms import Form, TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, SelectMultipleField, BooleanField, StringField, validators, ValidationError

from gen_sniper import get_requirement_titles

class Requirement_Lookup_Form(Form):

    quantitative = BooleanField('Quantitative Literacy')
    writing_intensive = BooleanField('Writing Intensive')
    off_campus = BooleanField('Off Campus Experience')
    diversity_us = BooleanField('Diversity US')
    diversity_international = BooleanField('Diversity International')
    natural_sci = BooleanField('Natural Sciences')
    # Social Sciences goes here
    humanities = BooleanField('Humanities')
    breadth_arts = BooleanField('Breadth/Arts')
    interdisc_breadth = BooleanField('Interdisciplinary Breadth')
