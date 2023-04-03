from django.db import models
from myapp.encryptor import encrypt

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    encrypted_password = models.CharField(max_length=255)

    def set_password(self, password):
        encryptor = encrypt()
        self.encrypted_password = encryptor.encrypt(password)

    def check_password(self, password):
        encryptor = encrypt()
        return encryptor.decrypt(self.encrypted_password) == password

    def save(self, *args, **kwargs):
        self.set_password(self.user.password)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username