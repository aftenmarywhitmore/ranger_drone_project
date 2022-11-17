import os
from dotenv import load_dotenv 

basedir = os.path.abspath(os.path.dirname(__file__))

#Give access to the projcect from an Operating System (os) we find ourselves in
# Allow outsode file/folders to be added to the project from base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set config variable for the Flask App.
    Using environment variables where available.
    Otherwise, create the config variable if not done already.
    
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'u cant catch me im the gingerbread man'
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') #hotspot for typos 
    #if something is being pushed to sqlite, that's not ideal (rather throw an error) 
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turns off updates from sqlalchemy
   

