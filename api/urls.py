from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailView, ListView, ImportView

urlpatterns = {
    url(r'^ifsc/(?P<ifsc>[A-Za-z]{4}\w{7})$', DetailView.as_view()),
    url(r'^branches/(?P<city>.*)/(?P<bank>.*)$', ListView.as_view()),
    url('add_data/', ImportView.as_view(), name='add_data')
}

urlpatterns = format_suffix_patterns(urlpatterns)