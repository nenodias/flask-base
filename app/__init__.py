from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_assets import Environment, Bundle, ManageAssets


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
assets = Environment(app)


js = Bundle('js/jquery.js', 'js/bootstrap.js', 'js/bootbox.js','js/search.js',
             filters='jsmin', output='gen/packed.js')
assets.register('js_all', js)


manager = Manager(app)
manager.add_command('db', MigrateCommand)
#assets
manager.add_command("assets", ManageAssets(assets))

from app.controllers import *