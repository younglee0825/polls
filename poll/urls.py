from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('poll/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('poll/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('poll/<int:question_id>/vote/', views.vote, name='vote')]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)