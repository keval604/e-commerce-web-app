from django.urls import path
from . import views

from user.views import (
    createNewUser, log_in_view, showProduct
)

# urlpatterns =[
#     path('',log_in_view),
#     path('products',showProduct),
#     path('createNewUser',createNewUser),
# ]