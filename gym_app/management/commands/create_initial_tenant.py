from django.core.management.base import BaseCommand
from gym_app.models import Client, Domain
import datetime

class Command(BaseCommand):
    help = 'Creates a tenant'

    def handle(self, *args, **kwargs):
        schema_name = input('schema name: ')
        tenant_name = input('name: ')
        paid_until = input('paid until (YYYY-MM-DD): ')
        on_trial = input('on trial (True/False): ')

        try:
            paid_until_date = datetime.datetime.strptime(paid_until, '%Y-%m-%d').date()
        except ValueError:
            self.stdout.write(self.style.ERROR('Invalid date format. Use YYYY-MM-DD.'))
            return

        on_trial_bool = on_trial.lower() in ['true', 't', 'yes', 'y']

        tenant = Client(schema_name=schema_name, name=tenant_name, paid_until=paid_until_date, on_trial=on_trial_bool)
        tenant.save()

        domain_name = f"{schema_name}.localhost"
        domain = Domain(domain=domain_name, tenant=tenant)
        domain.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created tenant {tenant_name} with schema {schema_name} and domain {domain_name}'))
