from django.db import models

class Config(models.Model):
    root_folder = models.CharField(max_length=255)
    # add any additional fields you need

    def __str__(self):
        return f"Config: {self.root_folder}"
