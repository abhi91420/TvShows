from flask import session, flash, redirect, render_template, request
from TvShows import app
from TvShows.models.model_editshow import EditShow


@app.route('/show/form')
def show_show_form():
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')

    return render_template('addshow.html')


@app.route('/update/show/<int:id>', methods=['POST'])
def update_recipe(id):
    if not EditShow.validate_recipe(request.form):
        return redirect(f"/edit/form/{id}")
    data = {
        'id': request.form['id'],
        'title': request.form['title'],
        'network': request.form['network'],
        'release_date': request.form['release_date'],
        'desc': request.form['desc']
    }
    EditShow.update_recipe(data)
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
