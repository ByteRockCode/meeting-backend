import graphene
from graphene_django import DjangoObjectType

from .models import Meeting


class MeetingObjectType(DjangoObjectType):
    class Meta:
        model = Meeting


class Query(graphene.ObjectType):

    meeting = graphene.Field(
        MeetingObjectType,
        id=graphene.Int(),
        slug=graphene.String(),
    )
    meetings = graphene.List(MeetingObjectType)

    def resolve_meetings(self, info):
        return Meeting.objects.all()

    def resolve_meeting(self, info, **kwargs):
        if 'id' in kwargs:
            return Meeting.objects.get(id=kwargs['id'])

        if 'slug' in kwargs:
            return Meeting.objects.get(slug=kwargs['slug'])

        return None


schema = graphene.Schema(query=Query)
