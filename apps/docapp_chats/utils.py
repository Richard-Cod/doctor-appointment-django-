

from apps.docapp_chats.models import Message
from django.db.models import Q


def getMessagesOfConversation(user1,user2):
    messages =  Message.objects.filter(Q(sender=user1,receiver=user2) | Q(sender=user2,receiver=user1))
    return messages