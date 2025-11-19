from django.db import models

# Create your models here.
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)   # Yangilik sarlavhasi
    image = models.ImageField(blank=True, null=True)  # Rasm
    content = models.TextField()               # Yangilik matni
    created_at = models.DateTimeField(auto_now_add=True)  # Qo'shilgan vaqti
    updated_at = models.DateTimeField(auto_now=True)      # Yangilangan vaqti
    is_published = models.BooleanField(default=True)      # Aktiv / Noaktiv

    def __str__(self):
        return self.title

class Media(models.Model):
    title = models.CharField(max_length=255)  # Video sarlavhasi
    youtube_url = models.URLField()           # YouTube linki
    description = models.TextField(blank=True, null=True)  # Tavsif (ixtiyoriy)
    thumbnail = models.ImageField(upload_to='media_thumbs/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)   # Qo‘shilgan sana
    is_published = models.BooleanField(default=True)       # Aktiv / Noaktiv

    def __str__(self):
        return self.title

    # ✅ YouTube Embed link qaytaruvchi funksiya
    def embed_url(self):
        """
        YouTube URL → embed formatga aylantiradi
        Masalan:
        https://youtu.be/abc123 → https://www.youtube.com/embed/abc123
        """
        import re
        patterns = [
            r'youtu\.be\/([^\?]+)',
            r'youtube\.com\/watch\?v=([^\&]+)',
            r'youtube\.com\/embed\/([^\?]+)'
        ]

        for p in patterns:
            match = re.search(p, self.youtube_url)
            if match:
                return f"https://www.youtube.com/embed/{match.group(1)}"

        return self.youtube_url  # Agar topilmasa oddiy link qaytariladi
