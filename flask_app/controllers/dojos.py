from flask_app import app	
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos/')
def dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template('dojos.html',all_dojos=all_dojos)

@app.route('/show_dojo/<dojo_id>')
def show_dojo(dojo_id):
    data = {
        'dojo_id':dojo_id
    }
    dojo = Dojo.get_dojo(data)
    print("A"*50)
    print(dojo)
    return render_template('show_dojo.html',dojo=dojo)

@app.route('/add_dojo/',methods=['POST'])
def add_dojo():
    print(request.form)
    Dojo.save_dojo(request.form)
    return redirect('/dojos/')







