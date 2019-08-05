from django.db import models


class RecentlyViewd(models.Model):
    user_id = models.ForeignKey('Auth.User', null=False, related_name="posts", on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post', null=False, related_name="posts", on_delete=models.CASCADE)
    lastTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.user_id, self.post_id, self.lastTime