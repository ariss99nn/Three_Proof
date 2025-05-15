from .models import EconomicIndicator
from decimal import Decimal

class EconomicCalculator:
    def __init__(self, sowing):
        self.sowing = sowing

    def get_exchange_rate(self):
        try:
            usd = EconomicIndicator.objects.get(name='USD-COP')
            return usd.value
        except EconomicIndicator.DoesNotExist:
            return 1  # Default if no exchange rate found

    def estimate_investment(self):
        # Aquí podrías sumar insumos, multiplicar por área, etc.
        base_cost_per_m2 = 1000  # Ejemplo en COP
        area = self.sowing.area
        return Decimal(base_cost_per_m2 * area)

    def estimate_income(self):
        # Precio estimado por kg x producción esperada
        price_per_unit = 5000  # COP por kg
        production = self.sowing.cantidad  # Producción esperada
        return Decimal(price_per_unit * production)

    def run_all(self):
        investment = self.estimate_investment()
        income = self.estimate_income()

        # VAN y TIR simulados
        npv = float(income - investment)
        irr = float((income - investment) / investment) if investment else 0

        return {
            'estimated_investment': investment,
            'projected_income': income,
            'npv': npv,
            'irr': irr
        }