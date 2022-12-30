from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=750)
    hirdetesleirasa =models.TextField(max_length=200)
    price =models.IntegerField()
    evjarat = models.CharField(max_length=7) #lehetne jobb is
    allapot=models.CharField(max_length=20)
    kivitel=models.CharField(max_length=20)
    kmora = models.IntegerField()
    szemelyek= models.IntegerField()
    ajtok = models.IntegerField()
    szin = models.CharField(max_length=20)
    karpit=models.CharField(max_length=40)
    sajattomeg=models.IntegerField()
    teljestomeg =models.IntegerField()
    csomagtarto = models.IntegerField()
    klima=models.CharField(max_length=50)
    uzemanyag = models.CharField(max_length=25)
    kobcenti = models.IntegerField()
    kw=models.IntegerField()
    le=models.IntegerField()
    henger = models.CharField(max_length=20)
    hajtas=models.CharField(max_length=25)
    sebessegvalto =models.CharField(max_length=40)
    okmanyok =models.CharField(max_length=80)
    muszaki = models.CharField(max_length=7)
    gumimeret = models.CharField(max_length=15)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title