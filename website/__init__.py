from flask import Flask


#Initializes starter elements/object when first run
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '4d4cd87hy3d8g6d187'
    
     
    #Import our blueprints
    from .views import views
    
    #Register our blueprints
    app.register_blueprint(views, url_prefix='/')
   
    
    return app

