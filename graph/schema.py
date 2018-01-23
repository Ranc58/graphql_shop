import graphene

import products.schema as products_schema


class Query(products_schema.Query, graphene.ObjectType):
    pass


class MyMutations(graphene.ObjectType):
    create_category = products_schema.CreateCategory.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)
