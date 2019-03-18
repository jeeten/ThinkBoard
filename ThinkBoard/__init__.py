# app.py or app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import ThinkBoard.logging as dictConfig
from flask_marshmallow import Marshmallow



app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
#To load configuration variables from an instance folder
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
ms = Marshmallow(app)
#db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
#app.config.from_envvar('APP_CONFIG_FILE')

# Now we can access the configuration variables via app.config["VAR_NAME"].

from product.product import product
app.register_blueprint(product,url_prefix='/api/product')

import ThinkBoard.index
import ThinkBoard.views
import ThinkBoard.pages
