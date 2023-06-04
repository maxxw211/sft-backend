from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.contracts.views import ContractView
from api.credit_applications.views import CreditApplicationView
from api.products.views import ProductView
from api.organizations.views import OrganizationView
from api.users.views import UserView

router = DefaultRouter()

router.register(r"users", UserView, basename="users")
router.register(r"organizations", OrganizationView, basename="organizations")
router.register(r"products", ProductView, basename="products")
router.register(r"contracts", ContractView, basename="contracts")
router.register(
    r"credit_application", CreditApplicationView, basename="credit_application"
)

urlpatterns = [
    path("", include(router.urls)),
]
