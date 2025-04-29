from django.db import models


class modelTeam(models.Model):
    title = models.CharField("Название", max_length=100)
    liga = models.IntegerField("Лига", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'teams'