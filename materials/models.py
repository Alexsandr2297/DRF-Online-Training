from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    avatar = models.ImageField(
        upload_to="avatars/",
        verbose_name="Картинка",
        blank=True,
        null=True,
        help_text="Загрузите картинку",
    )
    description = models.TextField(verbose_name="Описание урока", blank=True, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока", blank=True, null=True)
    avatar = models.ImageField(
        upload_to="avatars/",
        verbose_name="Картинка",
        blank=True,
        null=True,
        help_text="Загрузите картинку",
    )
    video_url = models.URLField(max_length=500, verbose_name="Ссылка на видео")
    # СВЯЗЬ С КУРСОМ (один ко многим)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,  
        related_name="lesson",
        verbose_name="Курс",
        help_text="Выберите курс, к которому относится урок",
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.title
