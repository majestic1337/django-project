from django.db import models

# Create your models here.
class Order(models.Model):
    status=models.CharField(max_length=20,default="NEW")
    username=models.CharField(max_length=200)
    adress=models.TextField()
    product=models.CharField(max_length=50,default="")
    phone_num=models.CharField(max_length=30,default="+380")

    def get_absolute_url(self):
        return f'/order/{self.id}'
    # Додайте інші поля для товару
    def __str__(self):
        return self.status