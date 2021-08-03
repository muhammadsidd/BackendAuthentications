from decimal import Decimal

from django.shortcuts import get_object_or_404

# from inventory_app.settings import SESSION_ID_CART
# from productapp.models import Product


# class Cart(object):
#     def __init__(self, request):
#         # 1. Get hold of session of request and response object
#         # 2. Assign Web Application level session Id to this object
#         # 3. If the object is not created yet, then create a object
#         self.session = request.session
#         if not self.session.get(SESSION_ID_CART):
#             self.session[SESSION_ID_CART] = {}
#             #create a dictionary of dictionaries
#         self.session_cart_obj = self.session[SESSION_ID_CART]

#     def addnew(self, product):
#         product_id = str(product.id)
#         if product_id not in self.session_cart_obj:
#             #key of the dictionary is the product id and the values are the quantity and prices
#             self.session_cart_obj[str(product_id)] = {'quantity': 0, 'price': str(product.price)}
#         self.session_cart_obj[str(product_id)]['quantity'] += 1
#         self.session[SESSION_ID_CART] = self.session_cart_obj
#         self.session.modified = True

#     def removeone(self, product_id):
#         if str(product_id) in self.session_cart_obj:
#             self.session_cart_obj[str(product_id)]['quantity'] -= 1
#             if self.session_cart_obj[str(product_id)]['quantity'] <= 0:
#                 del self.session_cart_obj[str(product_id)]
#         self.session[SESSION_ID_CART] = self.session_cart_obj
#         self.session.modified = True

#     def __iter__(self):
#         product_ids = self.session_cart_obj.keys()
#         # get the product objects and add them to the cart
#         products = Product.objects.filter(id__in=product_ids)
#         for product in products:
#             self.session_cart_obj[str(product.id)]['product'] = product
#         for item in self.session_cart_obj.values():
#             item['price'] = item['price']
#             item['total_price'] = Decimal(item['price']) * Decimal(item['quantity'])
#             yield item

#     def clearSession(self):
#         self.session_cart_obj = self.session[SESSION_ID_CART] = {}
#         self.session.modified = True

#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['quantity'] for item in self.session_cart_obj.values())

#     def __len__(self):
#         return sum(item['quantity'] for item in self.session_cart_obj.values())


