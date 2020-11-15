from django.urls import path

from student import views

urlpatterns = [
    path('', views.home),
    path('reg', views.f1, name='reg'),
    path('log', views.f2, name='log'),
    path('registration', views.registrationfunction),
    path('show', views.showfunction, name='show'),
    path('loginaction', views.loginfunction),
    path('updateurl/<int:id>',views.updatefunction, name='update'),
    path('deleteurl/<int:id>',views.deletefunction, name='delete'),
]