from django.db import models

#Defining model containing BANK details!
class Bank(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

#Defining Model contaning all branch details with foreign key associated with the bank.
class Branch(models.Model):
    name = models.CharField(max_length=256)  # branch 
    ifsc = models.CharField(max_length=500, unique=True)
    bank = models.ForeignKey(Bank, on_delete = models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)

#Piece of code for Model header name when more than one branch is inserted.
    class Meta:
        ordering = ('name',)
        verbose_name = 'Branch'
        verbose_name_plural = 'Branch'
    
    def __str__(self):
        return "{} - {} - {}".format(self.name, self.city, self.bank)