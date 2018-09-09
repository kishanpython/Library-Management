from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/',views.register_views,name='register'),
    url(r'stureg/',views.student_views,name='student'),
    url(r'^login/',views.login_view,name='login'),
    url(r'^logout/',views.logout_view,name='logout'),
    #url(r'^stulogin',views.studentlogin_views,name="stulogin"),


]