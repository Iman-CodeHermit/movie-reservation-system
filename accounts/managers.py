from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password, full_name):
        if not phone_number:
            raise ValueError('user must have phone number')

        if not email:
            raise ValueError('user must have email')

        if not full_name:
            raise ValueError('user must have full name')

        user = self.model(phone_number=phone_number,
                          email=self.normalize_email(email),
                          full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, phone_number, email, password, full_name):
        user = self.create_user(phone_number, email, password, full_name)
        user.is_admin = True
        user.save(using=self.db)
        return user