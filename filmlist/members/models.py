from django.db import models


class Member(models.Model):
    nazev = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    rok = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nazev} {self.autor}"
