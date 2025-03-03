from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, TransactionViewSet, InvoiceViewSet, TaxViewSet, BudgetViewSet, FinancialReportViewSet

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'taxes', TaxViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'financial-reports', FinancialReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]