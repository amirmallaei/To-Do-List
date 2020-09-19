from django.urls import path
from todo_list.views import home, about, delete, cross, uncross

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name='about'),
    path('delete/<list_id>', delete, name='delete'),
    path('cross/<list_id>', cross, name='cross'),
    path('uncross/<list_id>', uncross, name='uncross'),
]
