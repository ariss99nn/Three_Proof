from celery import shared_task
from Productos.models import Product
from Inventario.models import Input
from Ventas.models import Sale
from Economia.models import EconomicIndicator

@shared_task
def update_product_prices():
    try:
        rate = EconomicIndicator.objects.get(name="USD-COP").value
    except EconomicIndicator.DoesNotExist:
        rate = 1

    products = Product.objects.all()
    for product in products:
        if product.usd_price:
            product.market_price = product.usd_price * rate
            product.save()

@shared_task
def update_input_prices():
    try:
        rate = EconomicIndicator.objects.get(name="USD-COP").value
    except EconomicIndicator.DoesNotExist:
        rate = 1

    inputs = Input.objects.all()
    for item in inputs:
        if item.usd_price:
            item.local_price = item.usd_price * rate
            item.save()

@shared_task
def update_sales_data():
    sales = Sale.objects.all()
    for sale in sales:
        sale.balance = sale.sale_price - sale.investment
        sale.profitability = sale.balance / sale.investment if sale.investment else 0
        sale.save()