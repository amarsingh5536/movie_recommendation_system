from . import app
from .api import RecommendMovieView

app.add_url_rule('/recommend/movie/', 
    view_func=RecommendMovieView.as_view('recommend_movie'))
