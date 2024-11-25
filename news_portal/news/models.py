from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.user}'

    def update_rating(self):
        rating_posts = 0
        rating_comments = 0
        post_comments_rating = 0
        posts = Post.objects.filter(author=self)
        for post in posts:
            rating_posts += post.ratint_post
        comments = Comment.objects.filter(user=self.user)
        for comment in comments:
            rating_posts += comment.comment_rating
        posts_comments = Comment.objects.filter(post__author=self)
        for commentrating in comment:
            post_comments_rating += commentrating.commen_trating

        self.author_rating = rating_posts * 3 + rating_comments + post_comments_rating
        self.save()


class Categories(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return f'{self.category_name}'


class Comment(models.Model):
    comment_title  = models.CharField(max_length=255)
    comment_content = models.TextField(default="Оставьте ваш комментарий")
    comment_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_date_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)


class Post(models.Model):
    post = 'Pb'
    news = 'Nw'

    POSITIONS = [
        (post, 'Публикация'),
        (news, 'Новость')
    ]
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POSITIONS, default=post)
    post_date_time = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_category = models.ManyToManyField(Categories, through='PostCategory')
    ratint_post = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.post_title}'

    def like(self):
        self.ratint_post += 1
        self.save()

    def dislike(self):
        self.ratint_post -= 1
        self.save()

    def preview(self):
        return self.post_content[:124] + '...'



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
