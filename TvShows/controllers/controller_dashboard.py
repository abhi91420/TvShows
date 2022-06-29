from flask import session, flash, redirect, render_template

from TvShows import app
from TvShows.models.model_index import Index
from TvShows.models.model_show import Show


@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    user = Index.get_user_by_id(data)
    shows = Show.show_all()
    return render_template('dashboard.html', user=user, shows=shows)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
