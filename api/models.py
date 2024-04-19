from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default="")
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    release_window = models.CharField(max_length=100, blank=True)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=300)

    demo = models.BooleanField(default=False)
    earlyaccess = models.BooleanField(default=False)
    # kickstarter_upcoming = models.BooleanField(default=False)
    # kickstarter_live = models.BooleanField(default=False)
    kickstarter_page = models.CharField(max_length=200, default="", blank=True)
    kickstarter_status = models.CharField(max_length=100, default="", blank=True)
    trailer = models.CharField(max_length=100, default="")

    # Social Media Platforms of a Game
    twitter = models.CharField(max_length=100, default="", blank=True)
    facebook = models.CharField(max_length=100, default="", blank=True)
    instagram = models.CharField(max_length=100, default="", blank=True)
    tiktok = models.CharField(max_length=100, default="", blank=True)
    youtube = models.CharField(max_length=100, default="", blank=True)
    discord = models.CharField(max_length=100, default="", blank=True)
    homepage = models.CharField(max_length=100, default="", blank=True)

    #Platforms the Game is available on
    steam = models.CharField(max_length=100, default="", blank=True)
    epic = models.CharField(max_length=100, default="", blank=True)
    gog = models.CharField(max_length=100, default="", blank=True)
    playstation = models.CharField(max_length=100, default="", blank=True)
    xbox = models.CharField(max_length=100, default="", blank=True)
    nintendo = models.CharField(max_length=100, default="", blank=True)


    def __str__(self):
        return self.name
 

