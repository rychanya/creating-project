from django.db import models

# Create your models here.

class Columns(models.Model):
    name = models.CharField(max_length=50)
    width = models.IntegerField()
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f'#{self.number} {self.name}'

    @classmethod
    def get_all_order_by_number(cls):
        return cls.objects.order_by('number').all()
    

class CSVPath(models.Model):
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.path
    @classmethod
    def get_path(cls):
        path = cls.objects.first()
        if path:
            return path.path
        else:
            return None

    @classmethod
    def set_path(cls, path_to_csv):
        path = cls.objects.first()
        if not path:
            path = cls.objects.create(path=path_to_csv)
        else:
            path.path = path_to_csv
            path.save()
    
