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


class ProductSKU(Base):
    __table__ = Base.metadata.tables['ProductSKU']
    #ProductBarcodeId = db.Column("productbarcodeid",db.Integer,primary_key=True)

class ProductSKUShema(ms.ModelSchema):
    class Meta:
        model = ProductSKU
        fields = ("ProductSKUId","ProductId","ProductSKU","ProductSKUUQCId","ProductImage","Status","AddedDate","LastUpdatedDate","IsRecommended","hsnc")

class Product(db.Model):
    __tablename__ = 'Product'

class ProductSchema(ms.ModelSchema):
    class Meta:
        model = Product
        fields = ("ProductId","BrandId","CategoryId","ProductName","Status","AddedDate","LastUpdatedDate","SubSubCategoryId","Source")
