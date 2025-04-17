from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='event_thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.event.title}"
    
class EventVideo(models.Model):
    event = models.ForeignKey(Event, related_name='videos', on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='event_videos/')  # Store the video file
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video for {self.event.title}"