from django.views.generic import DetailView
from .models import Meeting


class MeetingDetail(DetailView):
    model = Meeting
    template_name = 'meetings/detail.html'
    context_object_name = 'meeting'

    # TODO: filter meeting by company of the user


class MeetingDetailMarkdown(MeetingDetail):
    template_name = 'meetings/detail.md'

    def render_to_response(self, context, **kwargs):
        kwargs['content_type'] = 'text/plai; charset=utf-8'
        return super(MeetingDetailMarkdown, self).render_to_response(context, **kwargs)
