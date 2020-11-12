from django.db import models


class Lesson(models.Model):
    """
    Lesson is entity of DB table, which has content title, description and image
    'title' is title of lesson
    'description' is lesson text
    'image' is field which content image for the lesson.It's may file .png,.jpeg, etc.
    """

    title = models.CharField('title', max_length=50)
    description = models.TextField('description')
    image = models.ImageField('image', upload_to='./lessons_image')

    class Meta:
        db_table = "Lesson"
        verbose_name = "Lesson"
