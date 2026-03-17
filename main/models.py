from django.db import models


class Performance(models.Model):
    title = models.CharField(max_length=200, verbose_name='שם ההופעה')
    venue = models.CharField(max_length=200, verbose_name='מקום')
    date = models.DateField(verbose_name='תאריך')
    description = models.TextField(blank=True, verbose_name='תיאור')
    ticket_url = models.URLField(blank=True, verbose_name='קישור לכרטיסים')

    class Meta:
        ordering = ['date']
        verbose_name = 'הופעה'
        verbose_name_plural = 'הופעות'

    def __str__(self):
        return f'{self.title} - {self.venue}'


def validate_audio(file):
    from django.core.exceptions import ValidationError
    import os
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ['.mp3', '.wav']:
        raise ValidationError('ניתן להעלות קבצי MP3 או WAV בלבד.')


class Track(models.Model):
    title = models.CharField(max_length=200, verbose_name='שם השיר')
    audio_file = models.FileField(
        upload_to='audio/',
        validators=[validate_audio],
        blank=True,
        verbose_name='קובץ אודיו (MP3/WAV)',
    )
    description = models.TextField(blank=True, verbose_name='תיאור')
    year = models.IntegerField(verbose_name='שנה')

    class Meta:
        ordering = ['-year']
        verbose_name = 'יצירה'
        verbose_name_plural = 'יצירות'

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='שם')
    email = models.EmailField(verbose_name='אימייל')
    message = models.TextField(verbose_name='הודעה')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'הודעת יצירת קשר'
        verbose_name_plural = 'הודעות יצירת קשר'

    def __str__(self):
        return f'{self.name} - {self.email}'
