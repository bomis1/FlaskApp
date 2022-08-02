from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import os
# from flask_wtf import FlaskForm 
# from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:toimeme@localhost:3306/flaskmysql3"
app.config['SECRET_KEY'] = "shhh it's a secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    team_name = db.Column(db.String(30), nullable=False)
    players = db.relationship('Player', backref='team')

    def __repr__(self):
        return f'<Team "{self.title}">'

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))

db.create_all()

# display all teams
@app.route('/')
def index():
    teams = Team.query.all()
    return render_template('index.html', teams=teams)

# Displaying a player and his team and add New Players 
@app.route('/<int:team_id>/', methods=('GET', 'POST'))
def team(team_id):
    team = Team.query.get_or_404(team_id)
    if request.method == 'POST':
        player = Player(name=request.form['content'], team=team)
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('team', team_id=team.id))   
    return render_template('team.html', team=team)

# Display All Players
@app.route('/players/')
def players():
    players = Player.query.order_by(Player.id.desc()).all()
    return render_template('players.html', players=players)

# Delete Players
@app.post('/players/<int:player_id>/delete')
def delete_player(player_id):
    player = Player.query.get_or_404(player_id)
    team_id = player.team.id
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('team', team_id=team_id))

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')