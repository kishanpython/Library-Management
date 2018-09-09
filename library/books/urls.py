from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^entry/',views.book,name="entry"),
    url(r'^show/',views.show,name="show"),
    url(r'^edit/(?P<id>\d+)/',views.edit,name="edit"),
    url(r'^update/(?P<id>\d+)/',views.update,name="update"),
    url(r'^delete/(?P<id>\d+)/',views.delete,name="delete"),
    url(r'^searchbk/',views.search_book,name="searchbk"),
    url(r'^allocate/',views.allocate_book,name="allocate"),
    url(r'^det/',views.details,name="details"),
    url(r'^search/',views.search,name="search"),
    url(r'^stsearch/',views.stu_search,name="stsearch"),
    url(r'^return/(?P<id>\d+)/(?P<proid>\d+)/$',views.deallocate_views,name="return"),

]