from django.db import models
from common.models import CommonModel
# Create your models here.





class Room(CommonModel):

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="부산")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_frinedly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20,
        default="아파트",
        choices=RoomKindChoices.choices,
    )
    
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    amenties = models.ManyToManyField("rooms.Amenity")
    created = models.DateTimeField(auto_now_add=True) # 오브젝트 생성됬을때 날짜
    updated = models.DateTimeField(auto_now=True) # 오브젝트 업데이트 됬을때 날짜

class Amenity(CommonModel):

    """ Amenity Model Definition """
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)
    