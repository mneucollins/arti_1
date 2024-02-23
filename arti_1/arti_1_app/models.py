from django.db import models

# Create your models here.
class dialog(models.Model):
    dlg_id = models.AutoField(primary_key=True)
    dlg_name = models.CharField(verbose_name = "dialog name", max_length = 255)
    dlg_create = models.DateTimeField(auto_now_add=True)
    dlg_modified = (models.DateTimeField(auto_now=True))

