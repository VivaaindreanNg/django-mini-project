from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
# Create your models here.


class ClaimsModel(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=SET_NULL)

    # Basic insured and driver details:
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("Email", null=True, blank=True)
    mobileNo = models.IntegerField("Mobile No.", null=True, blank=True)

    # Vehicle details:
    vehicleYearMake = models.IntegerField(
        "Vehicle Year Make", null=True, blank=True)
    vehicleModel = models.CharField(
        "Vehicle Model", max_length=100, null=True, blank=True)
    vehicleNo = models.CharField(
        "Vehicle No.", max_length=10, null=True, blank=True)

    # Loss details:
    date = models.DateField("Date", null=True, blank=True)
    time = models.TimeField("Time", null=True, blank=True)
    location = models.CharField(
        "Location", null=True, blank=True, max_length=400)
    typeOfLoss = models.CharField(
        "Type of Loss:", default="Own Damage", max_length=20)
    description = models.CharField(
        "Description of Loss", null=True, blank=True, max_length=2000)
    isPoliceReported = models.CharField(
        "Police Report Lodged?", default="No", max_length=3)
    isInjured = models.CharField(
        "Anybody Injured?", default="No", max_length=3)

    #    Documents required for claims
    photo = models.ImageField("Photo", blank=True, upload_to='media/images/')
    pdf = models.FileField(
        "PDF document of Insurance cover:", blank=True, upload_to='pdf/')

    UPDATE_STATUS_CHOICES = [
        ("In Progress", "In Progress"),
        ("Accepted", "Accepted")
    ]
    updateStatus = models.CharField("Update Status",
                                    max_length=20,
                                    default="In Progress",
                                    choices=UPDATE_STATUS_CHOICES)

    def __str__(self):
        return self.name
