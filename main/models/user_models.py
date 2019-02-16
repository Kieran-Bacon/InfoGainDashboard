from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    avatar = models.ImageField()


    def countDocumentCollections(self):
        """ Count the number of document collections this owns """
        pass

    def countOntologies(self):
        """ Count the number of ontologies owned by this user """
        pass

class Notifications(models.Model):
    """ Store user notifications to be displayed to the user """


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    level = models.CharField(
        choices=(
            ()  # TODO: Add notification levels
        )
    )

    isSeen = models.BooleanField(default=False)