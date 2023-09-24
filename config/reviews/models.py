from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    name_book = models.CharField(max_length=25)
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f"Review by {self.name} <{self.email}>"