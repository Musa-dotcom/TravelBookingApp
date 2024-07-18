from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerViewSet, BookingViewSet, HotelViewSet, FlightViewSet,
    CarRentalViewSet, DestinationViewSet, ActivityViewSet, PaymentDetailsViewSet
)

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'carrentals', CarRentalViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'paymentdetails', PaymentDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
