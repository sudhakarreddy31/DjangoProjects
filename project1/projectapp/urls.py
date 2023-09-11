from django.urls import path
from projectapp import views

urlpatterns = [
    path("listview/",views.BookListView.as_view(),name='listview'),
    path("detailview/<int:pk>/",views.BookDetailView.as_view(),name='details'),
    path("createview/",views.BookCreateView.as_view()),
    path("updateview/<int:pk>/",views.BookDetailView.as_view()),
    path("deleteview/<int:pk>/",views.BookDeleteView.as_view())



]