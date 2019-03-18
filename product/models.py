from ThinkBoard import db,ms
from sqlalchemy import create_engine, MetaData, Table,orm
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base

engine = db.get_engine()
Base = declarative_base()
Base.metadata.reflect(engine)

#engine = db.get_engine()
#metadata = MetaData(bind=engine)
class Users(db.Model):
    db.reflect()
    __tablename__ = 'Users'

class UsersSchema(ms.ModelSchema):
    class Meta:
        modle = Users
        fields = ("UsersId","Email", "FirstName", "LastName")


class ProductBarcode(Base):
    __table__ = Base.metadata.tables['ProductBarcode']
    #ProductBarcodeId = db.Column("productbarcodeid",db.Integer,primary_key=True)

class ProductBarcodeSchema(ms.ModelSchema):
    class Meta:
        model = ProductBarcode
        fields = ("ProductBarcodeId","ProductSKUId","Barcode","AddedDate","LastUpdatedDate","source","sourceinfo")
