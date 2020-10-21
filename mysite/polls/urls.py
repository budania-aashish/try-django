from django.urls import path, include
from django.contrib import admin
from . import views
urlpatterns = [
    # to tell the application to include polls
    path('polls/', include('polls.urls')),

    # for the admin page
    path('admin/', admin.site.urls),

    # ex /polls/
    path('', views.index, name='index'),

    # ex /polls/5
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

