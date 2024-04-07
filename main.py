from flask import Flask, render_template, request, redirect, url_for , flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import bcrypt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = '@dsfdsghsaw2436edgrq'
db=SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName =db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    hashed_password = db.Column(db.String(120), nullable=False)

@app.route("/")
def regAcc():
    return render_template("RegAccount.html")
@app.route('/registration', methods=['POST'])
def Home():
    firstName=request.form["firstName"]
    lastName = request.form["lastName"]
    email = request.form["email"]
    password = request.form["password"]
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    user=User(firstName=firstName,lastName=lastName,
                     email=email,hashed_password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('зарегистрировались')
    return redirect('/')
if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
