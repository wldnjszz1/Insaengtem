from django.db import models


class Post(models.Model):
    user_id = models.ForeignKey('Auth.User', null=False, related_name="posts", on_delete=models.CASCADE)
    image = models.ImageField(default='', null=False)
    description = models.TextField()
    category1 = models.IntegerField(null=True)
    category2 = models.IntegerField(null=True)
    category3 = models.IntegerField(null=True)
    category4 = models.IntegerField(null=True)
    category5 = models.IntegerField(null=True)
    category6 = models.IntegerField(null=True)
    category7 = models.IntegerField(null=True)
    category8 = models.IntegerField(null=True)
    category9 = models.IntegerField(null=True)
    category10 = models.IntegerField(null=True)

    def __str__(self):
        self.id, self.user_id



