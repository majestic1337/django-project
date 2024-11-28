from django.db import models

class Filling(models.Model):
    name = models.CharField(max_length=100)
    # Додайте інші поля, які вам потрібні для країни
    def __str__(self):
        return self.name

class Desert(models.Model):
    name = models.CharField(max_length=100)
    filling= models.ForeignKey(Filling, on_delete=models.CASCADE)
    price=models.FloatField()
    img_path=models.CharField(max_length=200)
    composition=models.TextField()
    description=models.TextField()

    def get_absolute_url(self):
        return f'/deserts/candy/{self.id}'
    # Додайте інші поля для товару
    def __str__(self):
        return self.name