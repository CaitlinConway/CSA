from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(255), nullable = False, unique = True)
  firstName = db.Column(db.String(255), nullable= False)
  lastName = db.Column(db.String(255), nullable= False)
  zipCode = db.Column(db.Integer, nullable= False)
  password = db.Column(db.String(255), nullable= False)

  def to_dict(self):
    return {
      "id": self.id,
      "email": self.email,
      "firstName": self.firstName,
      "lastName": self.lastName,
      "zipCode": self.zipCode
    }

class Console(db.Model):
  __tablename__ = "farms"

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255), nullable=False, unique=True)
  location = db.Column(db.String(255), nullable=False)

class Game(db.Model):
  __tablename__ = "addOns"

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255), nullable=False, unique=True)


class Library(db.Model):
  __tablename__ = "farmAddOns"

  id = db.Column(db.Integer, primary_key = True)
  addOnId = db.Column(db.Integer, db.ForeignKey("addOns.id"))
  addOn = db.relationship("AddOn")
  farmId = db.Column(db.Integer, db.ForeignKey("farms.id"))
  farm = db.relationship("Farm")
  price = db.Column(db.Integer)
  frequency = db.Column(db.String(50))
