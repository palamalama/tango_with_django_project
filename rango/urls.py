from django.contrib import admin
from rango import views
from django.conf.urls import url, include

app_name = "rango"
urlpatterns = [
	url(r"^$",views.index,name="index"),
	url(r"^about/",views.about,name="about"),
	url(r"^category/(?P<category_name_slug>[\w\-]+)/$",views.show_category,name="show_category"),
	url(r"admin/",admin.site.urls),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r"^category/(?P<category_name_slug>[\w\-]+)/add_page/$", views.add_page, name="add_page"),

]
