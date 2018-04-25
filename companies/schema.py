import graphene
from graphene_django import DjangoObjectType

from .models import Company


class CompanyObjectType(DjangoObjectType):
    class Meta:
        model = Company


class Query(graphene.ObjectType):

    company = graphene.Field(
        CompanyObjectType,
        id=graphene.Int(),
        slug=graphene.String(),
    )
    companies = graphene.List(CompanyObjectType)

    def resolve_companies(self, info):
        return Company.objects.all()

    def resolve_company(self, info, **kwargs):
        if 'id' in kwargs:
            return Company.objects.get(id=kwargs['id'])

        if 'slug' in kwargs:
            return Company.objects.get(slug=kwargs['slug'])

        return None


schema = graphene.Schema(query=Query)
