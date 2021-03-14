from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# where db is located using sqlite (can use postres, mysql, etc.)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# creating db model 
class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id #function returns string anytime new element is created

# route to homepage
@app.route('/')
def index():
    return render_template('index.html')

# running built-in debugger
if __name__ == '__main__':
    app.run(debug=True)