import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from .models import Agreement
from .models import Compromise
from .models import Meeting


class AgreementObjectType(DjangoObjectType):
    class Meta:
        model = Agreement


class CompromiseObjectType(DjangoObjectType):
    class Meta:
        model = Compromise


class MeetingObjectType(DjangoObjectType):
    # agreements = graphene.List(AgreementObjectType)
    # compromises = graphene.List(CompromiseObjectType)

    class Meta:
        model = Meeting
        interfaces = (
            relay.Node,
        )


class Query(graphene.ObjectType):

    meeting = graphene.Field(
        MeetingObjectType,
        id=graphene.Int(),
        slug=graphene.String(),
    )
    meetings = graphene.List(MeetingObjectType)

    def resolve_meetings(self, info):
        return Meeting.objects.order_by('-from_datetime')

    def resolve_meeting(self, info, **kwargs):
        if 'id' in kwargs:
            return Meeting.objects.get(id=kwargs['id'])

        if 'slug' in kwargs:
            return Meeting.objects.get(slug=kwargs['slug'])

        return None


schema = graphene.Schema(query=Query)
