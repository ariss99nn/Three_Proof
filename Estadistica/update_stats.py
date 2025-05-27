from django.core.management.base import BaseCommand
from django.utils.timezone import now
from Siembra.models import Sowing
from Suelo.models import SoilAnalysis
from Estadistica.models import DailyStats

class Command(BaseCommand):
    help = 'Actualizar estadísticas diarias'

    def handle(self, *args, **kwargs):
        today = now().date()
        total_sowings = Sowing.objects.filter(created_at__date=today).count()
        total_soil_analyses = SoilAnalysis.objects.filter(created_at__date=today).count()

        stats, created = DailyStats.objects.update_or_create(
            date=today,
            defaults={
                'total_sowings': total_sowings,
                'total_soil_analyses': total_soil_analyses,
            }
        )
        self.stdout.write(f'Estadísticas actualizadas para {today}')
