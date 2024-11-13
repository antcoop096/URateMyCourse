from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("search/outcome", views.outcome, name="outcome"),
    # ex: /polls/5/
    path("search/outcome/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("search/outcome/<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("search/outcome/<int:question_id>/vote/", views.vote, name="vote"),
    path("search/outcome/<int:question_id>/add_rating/", views.add_rating, name='add_rating'),
]