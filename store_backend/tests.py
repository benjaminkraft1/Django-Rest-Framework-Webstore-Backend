from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models.products_model import Products
from .models.categories_model import Categories
from .models.orders_model import Orders, OrderItem
from .views.productsviewset import ProductsViewSet
# Model Tests

class ProductsModelTestCase(TestCase):
    def setUp(self):
        Products.objects.create(name="Test Products 1", price="1.30")
        Products.objects.create(name="Test Products 2", price="2")

    def test_products(self):
        """Products are correctly created"""
        p1 = Products.objects.get(name="Test Products 1")
        p2 = Products.objects.get(name="Test Products 2")
        self.assertAlmostEqual(p1.price, Decimal(1.30))
        self.assertAlmostEqual(p2.price, Decimal(2.00))

class CategoriesModelTestCase(TestCase):
    def setUp(self):
        Categories.objects.create(category="Test Category 1")

    def test_products(self):
        """Products are correctly created"""
        c1 = Categories.objects.get(id=1)
        self.assertEqual(c1.category, "Test Category 1")


class OrdersModelTestCase(TestCase):
    def setUp(self):
        p1 = Products.objects.create(name="Test Products 2", price="1")
        oi = OrderItem.objects.create(product_id=p1, quantity=1)
        user = User.objects.create(username="Test", password="test")
        orders = Orders.objects.create(user=user)
        orders.items.add(oi)

    def test_products(self):
        """Products are correctly created"""
        o1 = Orders.objects.get(id=1)
        self.assertEqual(o1.user.username, "Test")

from rest_framework.test import force_authenticate
# Endpoint Tests
class ProductsAPITests(APITestCase):
    def setUp(self):
        # Staff User
        self.staff_user = User.objects.create(username="staff", password="test")
        self.staff_user.is_staff=True
        self.staff_user.is_superuser=True
        
        # Customer User
        self.customeruser = User.objects.create(username="customer", password="test")


    def test_create_products_permitted(self):
        """
        Ensure staff can create a new Product object.
        """
        data = {'name': 'Test', 'price':1.40}
        self.client.login(user=self.staff_user)
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.post('/api/products/', data, format='json')
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Products.objects.get().name, 'Test')

    def test_create_products_notpermitted(self):
        """
        Ensure customer cannot create a new Product object.
        """
        data = {'name': 'Test1', 'price':1.40}
        self.client.login(user=self.customeruser)
        response = self.client.post('/api/products/', data, format='json')
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_products(self):
        """
        Ensure we can get Product objects.
        """
        p1 = Products.objects.create(name="Test Product", price="1")

        response = self.client.get('/api/products/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductsAPITests(APITestCase):
    def setUp(self):
        self.p1 = User.objects.create(username="Test_user")

        # Staff User
        self.staff_user = User.objects.create(username="staff", password="test")
        self.staff_user.is_staff=True
        self.staff_user.is_superuser=True
        
        # Customer User
        self.customeruser = User.objects.create(username="customer", password="test")


    def test_create_user_permitted(self):
        """
        Ensure staff can create a new user object.
        """
        data = {'username': 'Test_user2'}
        self.client.login(user=self.staff_user)
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.post('/api/users/', data, format='json')
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_user_notpermitted(self):
        """
        Ensure customer cannot create a new user object.
        """
        data = {'username': 'Test_user2'}
        self.client.login(user=self.customeruser)
        response = self.client.post('/api/users/', data, format='json')
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_permitted(self):
        """
        Ensure we can get user objects.
        """
        self.client.login(user=self.staff_user)
        self.client.force_authenticate(user=self.staff_user)
        response = self.client.get('/api/users/', format='json')
        self.client.logout()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_users_notpermitted(self):
        """
        Ensure we cannot get user objects.
        """
        response = self.client.get('/api/users/', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
