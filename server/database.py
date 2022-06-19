from passlib.hash import sha256_crypt
from app.models import User, Farm, AddOn, FarmAddOn
from app import app, db
from dotenv import load_dotenv
load_dotenv()


with app.app_context():
    db.drop_all()
    db.create_all()


    caitlin = User(email='coolcac@gmail.com', password=sha256_crypt.hash("caitlin"),            firstName="Caitlin", lastName="Conway", zipCode="53703")
    bob = User(email='guest@guest.com', password=sha256_crypt.hash("password"),        firstName="Bob", lastName="Smith", zipCode="53703")
    farm1 = Farm(name='Farm1', location="Milwaukee, WI")
    egg = AddOn(name='egg')
    farm1Egg = FarmAddOn(addOnId=1, farmId=1, price="3", frequency="biweekly")
    db.session.add(caitlin)
    db.session.add(bob)
    db.session.add(farm1)
    db.session.add(egg)
    db.session.add(farm1Egg)
    db.session.commit()
