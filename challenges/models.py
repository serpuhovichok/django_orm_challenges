from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    author_full_name = models.CharField(max_length=256)
    isbn = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Laptop(models.Model):
    BRANDS = {
        ("DELL", "DELL"),
        ("Lenovo", "Lenovo"),
        ("MacBook", "MacBook"),
    }
    brand = models.CharField(max_length=256, choices=BRANDS)
    year = models.SmallIntegerField()
    RAM = models.SmallIntegerField()
    HDD = models.SmallIntegerField()
    price = models.FloatField()
    count_available = models.SmallIntegerField()
    added_date = models.DateField()

    def to_json(self):
        return {
            'brand': self.brand,
            'year': self.year,
            'RAM': self.RAM,
            'HDD': self.HDD,
            'price': self.price,
            'count_available': self.count_available,
            'added_date': self.added_date
        }


class BlogPost(models.Model):
    STATUSES = {
        ("published", "опубликован"),
        ("not_published", "не опубликован"),
        ("banned", "забанен"),
    }
    CATEGORIES = {
        ('computers', 'Компьютеры'),
        ('soft', 'Софт'),
        ('coding', 'Кодинг'),
    }
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.CharField(max_length=256)
    status = models.CharField(max_length=20, choices=STATUSES)
    create_date = models.DateField()
    publish_date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORIES)

    def to_json(self):
        return {
            'title': self.title,
            'text': self.text,
            'author': self.author,
            'status': self.status,
            'create_date': self.create_date,
            'publish_date': self.publish_date,
            'category': self.category
        }