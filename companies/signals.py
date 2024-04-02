from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company, ExtendCompanyModel

@receiver(post_save, sender=Company) # this signal is called when a new company is created
def create_extend_company(sender, instance, created, **kwargs):
    if created:
        ExtendCompanyModel.objects.create(extend_company_info=instance)