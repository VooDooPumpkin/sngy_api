import graphene
from graphene_django import DjangoObjectType

from.models import Post


class OccupationType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("__all__")


class Query(graphene.ObjectType):
    get_occupations = graphene.List(OccupationType)
    get_occupation = graphene.Field(OccupationType, occupationId=graphene.Int())

    def resolve_get_occupations(root, info, **kwargs):
        return Post.objects.all()

    def resolve_get_occupation(root, info, occupationId):
        return Post.objects.get(id=occupationId)


class CreateOccupation(graphene.Mutation):
    occupation = graphene.Field(OccupationType)

    class Arguments:
        name = graphene.String(required=True)
        company_name = graphene.String(required=True)
        position_name = graphene.String(required=True)
        hire_date = graphene.Date(required=True)
        fire_date = graphene.Date(required=True)
        salary = graphene.Int(required=True)
        fraction = graphene.Int(required=True)
        base = graphene.Int(required=True)
        advance = graphene.Int(required=True)
        by_hours = graphene.Boolean(required=True)

    def mutate(self, info, **kwargs):
        occupation = Post(**kwargs)
        occupation.save()
        return CreateOccupation(occupation=occupation)


class Mutation(graphene.ObjectType):
    add_occupation = CreateOccupation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
