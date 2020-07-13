from django.db import models

class Fraga(models.Model):
    fraga_text = models.CharField(max_length=200)

    def __str__(self):
        return self.fraga_text

class Val(models.Model):
    fraga = models.ForeignKey(Fraga, on_delete=models.CASCADE)
    val_text = models.CharField(max_length=200)
    roster = models.IntegerField(default=0)

    def __str__(self):
        return self.val_text
