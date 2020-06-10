from django.db import models


class Soundcloud(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    embed_src = models.URLField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.id}: {self.title}"
