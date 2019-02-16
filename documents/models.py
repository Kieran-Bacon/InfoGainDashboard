from django.db import models
from django.contrib.auth.models import User

import uuid

class DocumentCollections(models.Model):
    """ Form the structure to hold documents together formally """

    PUBLIC = "public"  # A public document collection can be read by any user
    COLLABORATORS = "collaborators"  # seen only by users that has worked with the owner on other projects
    PRIVATE = "private"  # A private document collection can only be read by users that have been given access

    dcid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # We do not want the Document to be deleted

    name = models.CharField(max_length=100)
    visibility = models.CharField(
        max_length=10,
        choices = (
            (PUBLIC, "public"),
            (COLLABORATORS, "collaborators only"),
            (PRIVATE, "private")
        ),
        default = PRIVATE
    )

    # Whether the document collection can be searched for, if collection is public
    isSearchable = models.BooleanField(default=False)

class DocumentCollectionPermissions(models.Model):
    """ Links users to document collections and describes their permissions """

    # Permissions
    READ = 10
    FORK = 20
    WRITE = 30
    ADMIN = 40

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ForeignKey(DocumentCollections, on_delete=models.CASCADE)
    permission = models.IntegerField(
        choices = (
            (READ, "Can view the document collection, and read its documents"),
            (FORK, "Can fork the document collection, equivalently copying and become owner of the new collection"),
            (WRITE, "Can add documents/annotations along with editting previous documents"),
            (ADMIN, "Can do everything including changing the properties/settings of the document collection")
        ),
        default=READ
    )

class Document(models.Model):
    dig = models.UUIDField(primary_key=True)
    dcid = models.ForeignKey(DocumentCollections, on_delete=models.CASCADE)