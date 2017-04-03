
from django.db import models


class Article(models.Model):
    title = models.CharField(u'Title', max_length=256)
    created_at = models.DateTimeField(u'Created date', auto_now_add=True)
    announce_text = models.TextField(u'Announce', blank=True)
    text = models.TextField(u'Text')


    def __unicode__(self):
        return self.title


    @property
    def announce(self):
        return self.announce_text or self.text[:512].rsplit(' ', 1)[0]


    class Meta:
        ordering = ['-created_at']
