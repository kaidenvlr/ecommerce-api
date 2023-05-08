from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from main.models import Buyer


class OrderStatusChoice(models.IntegerChoices):
    NEW = 0, 'новый'
    PAYED = 1, 'Оплачен'
    DELIVERY = 2, 'На доставке'
    FINISHED = 3, 'Завершен'


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category', null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='subcategory', null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Brand(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='brand', null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField(default=-1.0)

    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    image = models.ManyToManyField('ProductImage', related_name='product')
    review = models.ManyToManyField('Review')

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product', null=True, blank=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'


class Review(models.Model):
    content = models.TextField()
    star = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:10] + '...' if len(self.content) > 10 else self.content

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Order(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='orders', null=True)
    total_price = models.FloatField()
    promo = models.ForeignKey('Promo', on_delete=models.CASCADE, null=True, blank=True)

    delivery = models.BooleanField(default=False)  # Если False - самовывоз, True - доставка
    city = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    status = models.IntegerField(default=OrderStatusChoice.NEW, choices=OrderStatusChoice.choices)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
    product = models.ManyToManyField('CartProduct')

    def __str__(self):
        return self.buyer.user.username

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.product.title} - {self.qty} шт.'

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


class Promo(models.Model):
    name = models.CharField(max_length=50)
    discount_percent = models.IntegerField(help_text='Enter percent of discount')

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
