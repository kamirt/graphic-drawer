from django.db import models

# Create your models here.
class Upload(models.Model):
	x = models.CharField(max_length=200, default="1", verbose_name="Координата Х")
	y = models.CharField(max_length=200, default="1", verbose_name="Координата У")
	class Meta:
		verbose_name = 'Файл'
		verbose_name_plural = 'Файлы'