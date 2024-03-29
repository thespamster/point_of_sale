# import the database object
from pointofsale import db


class Menus(db.Model):
    # schema for the Menus model 
    id = db.Column(db.Integer, primary_key=True)
    menus_name = db.Column(db.String(25), nullable=False)
    menus_description = db.Column(db.String(29), nullable=False)
    submenus = db.relationship("Submenus", backref="menus", cascade="all, delete", lazy=True)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.menus_name


class Submenus(db.Model):
    # schema for the Submenus model
    id = db.Column(db.Integer, primary_key=True)
    submenus_name = db.Column(db.String(25), nullable=False)
    submenus_description = db.Column(db.String(29), nullable=False)
    items = db.relationship("Items", backref="submenus", cascade="all, delete", lazy=True)
    menus_id = db.Column(db.Integer, db.ForeignKey("menus.id"), nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.submenus_name
    

class Items(db.Model):
    # schema for the Items model
    id = db.Column(db.Integer, primary_key=True)
    items_name = db.Column(db.String(25), nullable=False)
    items_description = db.Column(db.String(29), nullable=False)
    items_price = db.Column(db.Float, nullable=False)
    items_costprice = db.Column(db.Float, nullable=False)
    submenus_id = db.Column(db.Integer, db.ForeignKey("submenus.id"), nullable=False)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.items_name
    

class Currentorder(db.Model):
    # schema for the Currentorder model
    id = db.Column(db.Integer, primary_key=True)
    currentorder_name = db.Column(db.String(25), nullable=False)
    currentorder_price = db.Column(db.Float, nullable=False)
    currentorder_costprice = db.Column(db.Float, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.currentorder_name
    

class Transactions(db.Model):
    # schema for the Transactions model
    id = db.Column(db.Integer, primary_key=True)
    transactions_name = db.Column(db.String(25), nullable=False)
    transactions_price = db.Column(db.Float, nullable=False)
    transactions_costprice = db.Column(db.Float, nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.transactions_name


    