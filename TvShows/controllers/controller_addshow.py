from TvShows import app
from TvShows.models.model_addshow import AddShow
from flask import render_template, redirect, session, request, flash


@app.route('/add/show', methods=['POST'])
def create_recipe():
    if not AddShow.validate_recipe(request.form):
        return redirect('/show/form')
    data = {
        'id': request.form['id'],
        'title': request.form['title'],
        'network': request.form['network'],
        'release_date': request.form['release_date'],
        'desc': request.form['desc']
    }
    AddShow.create_recipe(data)
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
