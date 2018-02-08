from django.db import models
from django.utils import timezone


class Post(models.Model):
        author = models.ForeignKey('auth.User',on_delete= models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
                self.published_date = timezone.now()
                self.save()

        def __str__(self):
                return self.title

class Comment(models.Model):
        post = models.ForeignKey("cinema.Post", related_name="comments",on_delete= models.CASCADE)
        author = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        approved_comment = models.BooleanField(default=False)

        def approve(self):
                self.approved_comment = True
                self.save()

        def __str__(self):
                return self.text

class Cinema(models.Model):
        name = models.CharField(max_length=200)

        def __str__(self):              
                return self.name

        class Meta:
            ordering = ('name',)


class Movies (models.Model):  
        cinema_name = models.ManyToManyField(Cinema)
        movie_name_id = models.ForeignKey(Cinema, on_delete=models.CASCADE, blank = True, null=True)
        name = models.CharField(max_length=200)

        def __str__ (self):
                return self.name
        
        class Meta:
                ordering = ('name',)

