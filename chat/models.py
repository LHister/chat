from django.db import models

from django.db import models

class Names(models.Model):
    name = models.TextField(
        null=True
    )
    
    ip = models.TextField(
        max_length=50,
        null=True,
        blank=False
    )

    def __str__(self):
        if self.name:
            return self.name  
        else: 
            return self.ip

class Fchat(models.Model):
    message = models.TextField(
        null=True
    )
    
    sender = models.ForeignKey(
        Names,
        on_delete=models.CASCADE
    )
    
    created = models.DateTimeField(
        null=True
    )

    def __str__(self):
        return self.message if self.message else ""

class Files(models.Model):
    file = models.FileField(
        null=True
    )
    
    sender = models.ForeignKey(
        Names,
        on_delete=models.CASCADE
    )
    
    created = models.DateTimeField(
        null=True
    )
    
    def __str__(self):
        return self.file.file if self.file else ""