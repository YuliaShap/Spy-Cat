from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Mission(models.Model):
    spy_cat = models.ForeignKey(SpyCat, on_delete=models.SET_NULL, null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    targets = models.ManyToManyField(Target)

    def __str__(self):
        return f"Mission {self.id}"
