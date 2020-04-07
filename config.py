#this is a configuration file
import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = 'veryfast299792458' 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database/app.db') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


    

