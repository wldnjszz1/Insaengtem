from django.db import models


class BookMark(models.Model):
    user_id = models.ForeignKey('Auth.User', null=False, related_name="posts", on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post', null=False, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        self.user_id, self.post_id