# Initialize the database
from app import Player, Team, db

team1 = Team(title='First Team', team_name='Arsenal')
team2 = Team(title='Second Team', team_name='Manchester United')
team3 = Team(title='Third Team', team_name='Chelsea')
team4 = Team(title='Fourth Team', team_name='Manchester City')

player1 = Player(name='Hector Bellerin', team=team1)
player2 = Player(name='Cristiano Ronaldo', team=team2)
player4 = Player(name='Gabriel Jesus', team_id=1)
player5 = Player(name='Marcus Rashford', team_id=2)

db.session.add_all([team1, team2, team3, team4])
db.session.add_all([player1, player2])

db.session.commit()