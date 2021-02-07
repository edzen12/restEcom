from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=150)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=150)
    category = models.ForeignKey(Category, verbose_name="Категории", related_name='books', on_delete=models.CASCADE)
    author = models.CharField(verbose_name="Автор", max_length=250)
    pages = models.IntegerField(verbose_name="Стр")
    price = models.FloatField(verbose_name="Цена", default=0)
    stock = models.IntegerField(verbose_name="Акции")
    description = models.TextField(verbose_name="Описание")
    imageUrl = models.ImageField(upload_to="uploads", blank=True, null=True)
    status = models.BooleanField(verbose_name="статус", default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name="заголовок", max_length=150)
    category = models.ForeignKey(Category, verbose_name="категории", related_name='products', on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="цена", default=0)
    quantity = models.IntegerField(verbose_name="количество", default=0)
    description = models.TextField(verbose_name="описание")
    imageUrl = models.ImageField(upload_to="uploads", blank=True, null=True)
    status = models.BooleanField(verbose_name="статус", default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.title)


