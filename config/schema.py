import companies.schema
import meetings.schema
import graphene

from graphene_django.debug import DjangoDebug


class Query(meetings.schema.Query, companies.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(query=Query)
