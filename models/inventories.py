from app import db
#create a class of the inventories table that'll house all the models of that table
#from db instance of SQLAlchemy,get the model class


class InventoryModel(db.Model):
    __tablename__ = 'inventories'
    __table_args__ = {'extend_existing': True}
    #to add columns,use your sqlalchemy object to get the column class that'll help you define your columns
    id = db.Column(db.Integer,primary_key=True)#research on additional objects you can pass in the column id
    inv_name = db.Column(db.String, nullable=False)
    inv_type = db.Column(db.String, nullable=False)
    buyingPrice = db.Column(db.Float, nullable=False)