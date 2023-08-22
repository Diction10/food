from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime
from PIL import Image

# Create your models here.
# class Customer(AbstractUser):
#     pass

class User(AbstractUser):
    pass
    

class Food(models.Model):
    FOOD_NAME = (
        ('default', 'Select Food Type'),
        ('Pizza', 'Pizza',),
        ('Burger', 'Burger',),
        ('Rice', 'Rice',),
        ('Coffee', 'Coffee'),
        ('Chicken & Chips', 'Chicken & Chips'),
        ('Ice-Cream', 'Ice-Cream'),
    )

    name = models.CharField(max_length=100, choices=FOOD_NAME, default='')
    image = models.ImageField(upload_to='food_pics')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500)
    date_created = models.DateField(default=datetime.now, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        # return self.item_name
        return f'{self.user} created {self.name}'

    # to resize the images
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Cart(models.Model):
    food_name = models.ManyToManyField(Food, blank=True, related_name='added')
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ManyToManyField(User, blank=True, related_name='user')

    def __str__(self):
        # return self.item_name
        return f'{self.user} has added {self.food_name} to their cart'

  


  