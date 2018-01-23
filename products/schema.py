import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from .models import Category, Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node, )


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'title': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node,)


class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, title):
        Category(title=title).save()
        ok = True
        return CreateCategory(ok=ok)


class Query(graphene.AbstractType):
    products = DjangoFilterConnectionField(ProductType)
    categories = DjangoFilterConnectionField(CategoryType)

    def resolve_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()
