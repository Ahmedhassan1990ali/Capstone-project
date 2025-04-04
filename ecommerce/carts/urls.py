"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from carts.views import ( UserCartsModelViewSet, UserCartItemsModelViewSet,
                         AdminCartsModelViewSet, AdminCartItemsModelViewSet
)

router = routers.DefaultRouter()
router.register(r'user/carts',UserCartsModelViewSet,basename="usercarts")
router.register(r'user/cartitems',UserCartItemsModelViewSet,basename="usercartitems")
router.register(r'admin/carts',AdminCartsModelViewSet,basename="admincarts")
router.register(r'admin/cartitems',AdminCartItemsModelViewSet,basename="admincartitems")


urlpatterns = [
    path('',include(router.urls))
]