from django.db import models


class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


    class Meta:
        ordering = ["id"]

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True,)
    product_name = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    client_name = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return(f"{self.product_name} {self.price} {self.client_name}")