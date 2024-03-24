from django.db import models

class State(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    country_name = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



class Area(models.Model):
    name = models.CharField(max_length=300)
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

