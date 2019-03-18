# ThinkBoard/product/product.py
from flask import Blueprint, render_template, abort, jsonify, json, request
#from flask_api import status
from jinja2 import TemplateNotFound
from .models import *
from constants import LTM
from common import validation as check,log

import time
logging = log.logging
#log = logging.getLogger("my-logger")
#logging.basicConfig(filename='error.log',level=logging.DEBUG)
product = Blueprint('product', __name__,template_folder='templates')

@product.route('/all',methods=['GET', 'POST'])
def timeline():
    # Do some stuff
    session = orm.Session(engine)
    users = session.query(Users).all()
    userSchema = UsersSchema(many=True)
    outPut = userSchema.dump(users).data
    #app.logger.info('%s logged in successfully', 'Dasarathi')

    return jsonify({"User":outPut})
    #return json.dumps([dict(r) for r in User])
    #return render_template('product.html',{"UserList" : User })

@product.route('/', defaults={'page': 'index'})
@product.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)

@product.route('/getProductDetails',methods={"POST"})
def getProductDetails():
    '''
        getting product details
        Request : {Request:{"Header":{"DeviceId", "RequestTime", "Version", "Product"},"Body":{"StoreId", "SPBarcodeId"}}}
        Response :
    '''

    try:
        #data = request.get_data()

        headers = request.headers
        datas = None
        datas = request.get_json(silent=True, force=True)
        # Logging request
        logging.debug("Request: {}".format(datas))

        if not request.is_json or datas is None:
            raise Exception("Invalid json!")

        #Checking key exist
        check.checkKey(datas,"Request")
        check.checkKey(datas['Request'], ["Header","Body"])
        check.checkKey(datas['Request']['Header'],["DeviceId", "RequestTime", "Version", "Product"])
        check.checkKey(datas['Request']['Body'], ["StoreId", "SPBarcodeId"])

        session = orm.Session(engine)
        users = session.query(Users).all()
        userSchema = UsersSchema(many=True)
        outPut = userSchema.dump(users).data

        #Product = ProductBarcode.query.all();
        #logging.debug(dir(ProductBarcode))

        allProduct = session.query(ProductBarcode).limit(10).all()
        #logging.debug("all Poroduct {}".format(allProduct))
        ProductSchema = ProductBarcodeSchema(many=True)
        outPut = ProductSchema.dump(allProduct).data

        Response = {
            'Control': {'Status': 1, 'Message': "Product Detals", 'TimeTaken': ' Second', 'MessageCode': 200},
            'Data': {"Products":outPut,"LTM":LTM}
        }

    except Exception as E:
        Response = {
            'Control':{'Status':0,'Message':E.message,'TimeTaken':' Second','MessageCode' :200},
            'Data': {"Products": [], "LTM": LTM}
        }
        logging.debug(E.message)
        # Logging error
        logging.error("Response : {}".format(Response))

    #Logging response
    #logging.info("Response : {}".format(Response))
    return jsonify(Response)
