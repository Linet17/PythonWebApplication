from app import db


class SalesModel(db.Model):
    __tablename__ = 'sales'
    # __table_args__ = {'extend_existing': True}
    # to add columns,use your sqlalchemy object to get the column class that'll help you define your columns
    id = db.Column(db.Integer, primary_key=True)  # research on additional objects you can pass in the column id
    quantity = db.Column(db.Integer, nullable=False)
    inv_id = db.Column(db.Integer, db.ForeignKey('inventories.id'))
