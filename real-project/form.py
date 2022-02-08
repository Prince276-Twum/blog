from wtforms import SubmitField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, URL


class AddTeamForm(FlaskForm):
    CLUBS = StringField("Club Name", validators=[DataRequired()])
    Pos = StringField("Pos")
    P = StringField("P")
    W = StringField("W")
    D = StringField()
    L = StringField()
    GD = StringField()
    POINTS = StringField()
    submit = SubmitField("Done")


class RegisterForm(FlaskForm):
    Name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class PreviewsForm(FlaskForm):
    your_club = StringField("Your Club", validators=[DataRequired()])
    opponent_club = StringField("Opponent Club", validators=[DataRequired()])
    your_score = StringField("Your Score", validators=[DataRequired()])
    opponent_score = StringField("Opponent Score", validators=[DataRequired()])
    your_image = StringField("Your Image", validators=[DataRequired(), ])
    opponent_image = StringField("Opponent Image", validators=[DataRequired(), ])
    date = StringField("Date eg(05/Feburary/2022)", validators=[DataRequired(), ])
    submit = SubmitField("Done")
