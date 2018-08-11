from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Post(models.Model):
    body = models.CharField(max_length=2000)
    category = models.CharField(max_length=45)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.body + ' #' + self.category


