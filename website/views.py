from flask import Blueprint, render_template

#Create blueprint for home 
views = Blueprint('views', __name__)

#Define route for home URL (just / in this case)
#Whenever route is hit, the home function is called
@views.route('/')
def home():
    return render_template("home.html")