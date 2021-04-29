from django.urls import path

from . import views

urlpatterns = [
    path('',views.showbill, name='showbill'),
    path('insert',views.insertbill,name='insertbill'),
    path('edit/<int:id>',views.updatebill,name="updatebill"),
    path('update/<int:id>',views.editbutton, name="editbutton"),
    path('delete/<int:id>',views.delbill, name="delbill"),
]