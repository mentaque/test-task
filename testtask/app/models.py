from django.core.validators import RegexValidator
from django.db import models


class UserProfile(models.Model):
    phone_number = models.CharField(
        max_length=11,
        validators=[
        RegexValidator(
            regex=r'^7\d{10}$',
            message='Phone number must start with 7 and have a total length of 11 characters.',
            code='invalid_phone_number'
        )
    ])
    auth_code = models.CharField(max_length=4, default='0000')
    is_authenticated = models.BooleanField(default=False)
    invite_code = models.CharField(max_length=6, blank=True, null=True)
    inviter = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.phone_number
