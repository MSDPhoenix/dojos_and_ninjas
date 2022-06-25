from flask_app import app	
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/new_ninja/')
def new_ninja():
    dojos=Dojo.get_all_dojos()
    return render_template('new_ninja.html',dojos=dojos)

@app.route('/save_ninja/',methods=['POST'])
def save_ninja():
    print('C'*50)
    print(request.form)
    Ninja.save_ninja(request.form)
    return redirect('/show_dojo/'+request.form['dojo_id'])

