from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length = 255)
  body = models.TextField()
  pub_date = models.DateField(auto_now_add = True)
  image = models.ImageField(upload_to='images/')



