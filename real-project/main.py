from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from form import AddTeamForm, RegisterForm, PreviewsForm

app = Flask(__name__)
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sport.db"
app.config["SECRET_KEY"] = "ISLLKDLL5657LDLDRFF"
db = SQLAlchemy(app)


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    team_name = db.Column(db.String(234), nullable=False)
    P = db.Column(db.Integer)
    W = db.Column(db.Integer)
    D = db.Column(db.Integer)
    L = db.Column(db.Integer)
    GD = db.Column(db.Integer)
    points = db.Column(db.Integer)
    pos = db.Column(db.Integer)


class TeamName(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    team_name = db.Column(db.String(120), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(345))
    email = db.Column(db.String(453), unique=True, nullable=False)
    password = db.Column(db.String(345), unique=True, nullable=False)


class PreviousMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    your_club = db.Column(db.String(124))
    opponent_club = db.Column(db.String(1253))
    your_score = db.Column(db.String(3453))
    opponent_score = db.Column(db.String(3453))
    your_image = db.Column(db.String(34553))
    opponent_image = db.Column(db.String(3455))
    date = db.Column(db.String(3455))


db.create_all()


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/show_league")
def all_league():
    all_league_data = Sport.query.all()

    return render_template("league-table.html", data=all_league_data)


@app.route("/previous-matches")
def previous_matches():
    prev_data = PreviousMatch.query.all()
    return render_template("all-matches.html", previous=prev_data)


@app.route("/matches")
def all_matches():
    return render_template("matches.html")


@app.route("/add_team", methods=["POST", "GET"])
def new_team():
    add_form = AddTeamForm()
    if request.method == "POST":
        add_form_data = request.form
        print(add_form_data)
        add_data_sport = Sport(
            pos=add_form_data["Pos"],
            team_name=add_form_data["CLUBS"],
            P=add_form_data["P"],
            W=add_form_data["W"],
            D=add_form_data["D"],
            L=add_form_data["L"],
            GD=add_form_data["GD"],
            points=add_form_data["POINTS"]
        )
        db.session.add(add_data_sport)
        db.session.commit()
        return redirect(url_for('all_league'))
    return render_template("add_team.html", form=add_form)


@app.route("/edit")
def edit_table():
    edit_form = AddTeamForm()
    return render_template("add_team.html", form=edit_form)


@app.route("/register", methods=["POST", "GET"])
def register_admin():
    register_form = RegisterForm()
    user_form_data = request.form
    print(user_form_data)
    if request.method == "POST" and register_form.validate_on_submit():
        new_user = User(
            name=user_form_data["Name"],
            password=user_form_data["password"],
            email=user_form_data["email"]
        )
        db.session.add(new_user)
        db.session.commit()

    return render_template("register.html", form=register_form)


@app.route("/add-previous-match", methods=["POST", "GET"])
def add_previous_match():
    add_previous = PreviewsForm()
    prev_data = request.form
    print(prev_data)
    if request.method == "POST" and add_previous.validate_on_submit():
        add_prev_match = PreviousMatch(your_club=prev_data["your_club"],
                                       opponent_club=prev_data["opponent_club"],
                                       your_score=prev_data["your_score"],
                                       opponent_score=prev_data["opponent_score"],
                                       your_image=prev_data["your_image"],
                                       opponent_image=prev_data["opponent_image"],
                                       date=prev_data["date"]
                                       )
        db.session.add(add_prev_match)
        db.session.commit()
        return redirect(url_for('previous_matches'))
    return render_template("add_previous_match.html", form=add_previous)


@app.route("/remover/<int:prev_id>")
def delete_prev(prev_id):
    to_go = PreviousMatch.query.get(prev_id)
    db.session.delete(to_go)
    db.session.commit()
    return redirect(url_for('previous_matches'))


if __name__ == "__main__":
    app.run(debug=True)
