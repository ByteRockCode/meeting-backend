from django.urls import path

from .views import MeetingDetail
from .views import MeetingDetailMarkdown


urlpatterns = [
    path('<int:pk>/detail', MeetingDetail.as_view(), name='meetings__detail'),
    path('<int:pk>/detail.md', MeetingDetailMarkdown.as_view(), name='meetings__detail--markdown'),
]
