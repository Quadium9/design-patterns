from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length


class AddNoteForms(FlaskForm):
    title = StringField('Note title', validators=[InputRequired(), Length(1, 32)])
    description = TextAreaField('Description', validators=[InputRequired(), Length(1, 256)])
    date_field = DateField('Date')
    submit = SubmitField('Save')


class EditNoteForms(FlaskForm):
    title = StringField('Note name', validators=[InputRequired(), Length(1, 32)])
    description = TextAreaField('Description', validators=[InputRequired(), Length(1, 256)])
    date_field = DateField('Date')
    submit = SubmitField('Save')


class SearchNoteForms(FlaskForm):
    title = StringField('Note name', validators=[InputRequired(), Length(1, 32)])
    date_field = DateField('Date')
    submit = SubmitField('Search')
