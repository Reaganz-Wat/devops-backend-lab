import graphene
from graphene_django import DjangoObjectType
from .models import Products, Orders
from django.contrib.auth.models import User

class ProductsType(DjangoObjectType):
    class Meta:
        model = Products
        fields = ("id", "name", "price")

class OrdersType(DjangoObjectType):
    class Meta:
        model = Orders
        fields = ("id", "user", "product", "order_date")
        
class UsersType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username")


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductsType)
    all_orders = graphene.List(OrdersType)
    all_users = graphene.List(UsersType)

    product = graphene.Field(ProductsType, id=graphene.Int(required=True))
    order = graphene.Field(OrdersType, id=graphene.Int(required=True))
    user = graphene.Field(UsersType, id=graphene.Int(required=True))

    def resolve_all_products(root, info):
        return Products.objects.all()

    def resolve_all_orders(root, info):
        return Orders.objects.all()

    def resolve_product(root, info, id):
        return Products.objects.get(pk=id)

    def resolve_order(root, info, id):
        return Orders.objects.get(pk=id)
    
    def resolve_all_users(root, info, id):
        return Orders.objects.get(pk=id)


class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        price = graphene.Float(required=True)

    product = graphene.Field(ProductsType)

    def mutate(self, info, name, price):
        product = Products(name=name, price=price)
        product.save()
        return CreateProduct(product=product)


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
