from django.db import models
import uuid
from user.models import CustomUser

class Foodballfield(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    owner = models.ForeignKey(CustomUser, related_name="CostomUser", on_delete=models.CASCADE)
    address = models.CharField(max_length=200, blank=False, null=False)
    contact = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    booking_an_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

class Bron(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    foodballfield_id = models.ForeignKey(Foodballfield, related_name ="Foodballfield", on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, related_name="Costomuseer", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self) -> str:
        return self.user_id.username


