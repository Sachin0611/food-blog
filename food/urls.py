from django.contrib import admin
from django.urls import path
from . import views
app_name = 'food'
urlpatterns = [
    # path('',views.index,name="index"),
    path('',views.IndexClassView.as_view(),name='index'),
    path('<int:pk>/',views.foodDetail.as_view(),name="detail"),
    path('add/',views.createview.as_view(),name="create_item"),
    path('item/',views.item,name="item"),
    # path('add/',views.create_item,name="create_item"),
    path('update/<int:item_id>/',views.update_item,name="update_item"),
    path('delete/<int:item_id>/',views.delete_item,name="delete_item"),

]
