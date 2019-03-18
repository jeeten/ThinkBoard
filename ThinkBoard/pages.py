from ThinkBoard import app
from flask import jsonify, abort, make_response, render_template
from .models import Engine, db
@app.route('/about-us')
def about():
    return 'We welcomes new inovative ideas and implementing them'

@app.route('/contuct-us')
def contuct():
    return 'Call me @9930335502'

@app.route('/what-we-do')
def whatwedo():
    return 'will tell you'

@app.route('/all-product')
def productList():
    #data = dir(Engine)
    data = [{"Ford",2},{"Google",6}]
    NewRecord = Engine(data)
    db.session.add(NewRecord)
    db.session.commit()
    #return 'will tell you'
    return jsonify({'task': NewRecord.id})
    # return render_template('employees.html', result=res, content_type='application/json')