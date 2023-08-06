from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class Category(models.Model):
    TANKS = 'TA'
    HEALERS = 'HE'
    DD = 'DD'
    MERCHANTS = 'ME'
    GUILD_MASTERS = 'GM'
    QUEST_GIVERS = 'QG'
    BLACKSMITHS = 'BL'
    TANNERS = 'TN'
    POTION_MAKERS = 'PM'
    SPELL_MASTERS = 'SM'
    CATEGORY_NAME_CHOICES = [
        (TANKS, 'Танки'),
        (HEALERS, 'Хилы'),
        (DD, 'ДД'),
        (MERCHANTS, 'Торговцы'),
        (GUILD_MASTERS, 'Гилдмастеры'),
        (QUEST_GIVERS, 'Квестгиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (TANNERS, 'Кожевники'),
        (POTION_MAKERS, 'Зельевары'),
        (SPELL_MASTERS, 'Мастера заклинаний'),
    ]
    categoryName = models.CharField(max_length=2, choices=CATEGORY_NAME_CHOICES)


class Message(models.Model):
    dateTimeCreation = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = giRichTextUploadingField()

    def __str__(self):
        return self.title


class Response(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    isAccepted = models.BooleanField(null=True)
