from flask import flash, session, redirect, render_template

from TvShows import app
from TvShows.models.model_index import Index
from TvShows.models.model_show import Show


@app.route('/show/<int:id>')
def show_one_tvshow(id):
    if not 'user_id' in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    data = {
        'id': id
    }
    show = Show.show_info(data)
    user = Index.get_user_by_id({'id': session['user_id']})
    return render_template('show.html', recipe=show, user=user)