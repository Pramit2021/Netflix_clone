from django.urls import path
from .views import Home, ProfileLIst, ProfileCreate, Watch, ShowMovieDetail, Showmovie

app_name ='core'

urlpatterns = [
    path('',Home.as_view()),
    path('profile/',ProfileCreate.as_view(), name='profile_list'),
    path('profile/create/',ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/',Watch.as_view(), name='watch'),
    path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='show_det'),
    path('movie/play/<str:movie_id>',Showmovie.as_view(),name='play')
]