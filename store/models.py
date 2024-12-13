from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    UZ = 'sum'
    RU = 'rub'
    USD = '$'
    type_money = (
        (UZ, 'sum'),
        (RU, 'rub'),
        (USD, '$')
    )
    price_type = models.CharField(max_length=10,
                                  choices=type_money,
                                  default='sum')
    price = models.PositiveIntegerField()
    image = models.ImageField()


class Buy(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=40)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    All_size=(
        ('36', '36'),
        ('37', '37'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
    )


    size= models.CharField(max_length=100, choices=All_size)

    All_values=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    how = models.CharField(max_length=100, choices=All_values)
    map= models.TextField()
    email = models. EmailField (blank=True)

    def __str__(self):
        return f"{self.name} - {self.product}"