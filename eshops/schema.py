import graphene
import plumule.schema

class Query(plumule.schema.Query, graphene.ObjectType):
    pass

class Mutation(plumule.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)