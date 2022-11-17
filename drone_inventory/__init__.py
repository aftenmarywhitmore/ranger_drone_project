#information in our flask project about how we're starting this project up
#don't panic about squiggles- VS code slow sometimes

#local imports
from flask import Flask 
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from .models import db as root_db, login_manager, ma
from config import Config
from drone_inventory.helpers import JSONEncoder
from flask_migrate import Migrate

from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.config.from_object(Config)

root_db.init_app(app) #instantiating our database and getting our application ready to work with database 
migrate = Migrate(app, root_db)

login_manager.init_app(app)
login_manager.login_view = "auth.signin" #if they're not signed in, this is what they will see 

ma.init_app(app)
app.json_encoder = JSONEncoder
CORS(app)