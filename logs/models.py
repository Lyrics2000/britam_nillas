from django.db import models

class Logs(models.Model):
    LOG_TYPE_CHOICES = [
        ('INFO', 'Info'),
        ('ERROR', 'Error'),
        ('WARNING', 'Warning'),
    ]
    application =  models.CharField(max_length=255, default="api_nilas")
    log_type = models.CharField(max_length=10, choices=LOG_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    api_url = models.URLField(blank=True,null=True)
    request_data = models.TextField(blank=True,null=True)
    response_data = models.TextField(blank=True,null=True)
    status_code = models.IntegerField(blank=True,null=True)
    log_message = models.TextField()

    def __str__(self):
        return f"{self.log_type} - {self.timestamp}"