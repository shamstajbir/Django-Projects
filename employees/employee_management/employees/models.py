from django.db import ((models))

class Employee(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=100)
    short_description = models.TextField()

    def __str__(self):
        return self.name