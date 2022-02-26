# Create your models here.
from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey("core.User",related_name="messages_sent", on_delete=models.SET_NULL , null=True)
    receiver = models.ForeignKey("core.User",related_name="messages_received", on_delete=models.SET_NULL , null=True)

    senderID = models.CharField(max_length=255)
    receiverID = models.CharField(max_length=255)

    content = models.CharField(max_length=255 , blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.sender.first_name} - {self.receiver.first_name} - {self.content[0:5]}" 
