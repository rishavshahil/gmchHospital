from django.db import models

# Create your models here.
class HospitalTender(models.Model):
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=255)
    document = models.FileField(upload_to='tender_documents/')
    publishing_date = models.DateField()
    closing_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HospitalNotice(models.Model):
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=255)
    document = models.FileField(upload_to='notice_documents/')
    notice_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title