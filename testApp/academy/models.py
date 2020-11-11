from django.db import models


class Lesson(models.Model):

    title = models.CharField('title', max_length=50)
    description = models.TextField('description')
    image = models.ImageField('image', upload_to='./lessons_image')

    class Meta:
        db_table = "Lesson"
