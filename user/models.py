from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    book_count = models.IntegerField()
    
    def __str__(self):
        return self.book_name
    
class BorrowBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    