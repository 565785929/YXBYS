from django.db import models

# Create your models here.

class studentdb(models.Model):
    XXMC = models.CharField(max_length=40)
    XM   = models.CharField(max_length=8)
    KSH  = models.CharField(max_length=18)
    XB   = models.CharField(max_length=2)
    MZ   = models.CharField(max_length=10)
    ZZMM = models.CharField(max_length=10)
    RXSJ = models.CharField(max_length=8)
    BYSJ = models.CharField(max_length=8)
    XZ   = models.CharField(max_length=4)
    XLCC = models.CharField(max_length=14)
    ZYMC = models.CharField(max_length=40)
    BZ   = models.CharField(max_length=40)

    class Meta: 
        ordering = ('XM', )

    def __unicode__(self):
        return self.XM