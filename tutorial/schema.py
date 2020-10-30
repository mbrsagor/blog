import graphene

import graph.schema


class Query(graph.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
