from django.db.models.signals import post_save
from django.dispatch import receiver
from Siembra.models import Sowing
from .models import EconomicCalculation
from .services import EconomicCalculator

@receiver(post_save, sender=Sowing)
def calcular_automaticamente(sender, instance, created, **kwargs):
    calc = EconomicCalculator(instance)
    result = calc.run_all()
    EconomicCalculation.objects.update_or_create(
        sowing=instance,
        defaults=result
    )