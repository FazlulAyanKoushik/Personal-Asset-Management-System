from .models import InboxMessage, NewMessage
from accounts.models import CustomUser


def unread_messages(request):
    if request.user.is_authenticated:
        unread_msgs = InboxMessage.objects.filter(receiver_id=request.user, delete_status=True,
                                                  new_msg_active=True)[0:5]
        total_unread_msgs = InboxMessage.objects.filter(receiver_id=request.user,
                                                        delete_status=True, new_msg_active=True).count()
        total_draft_msgs = NewMessage.objects.filter(sender_id=request.user,
                                                     delete_status=True, new_msg_active=True,
                                                     msg_status='Draft').count()
        return {'unread_msgs': unread_msgs, 'total_unread_msgs': total_unread_msgs,
                'total_draft_msgs': total_draft_msgs}
    else:
        return {'total_unread_msgs': 0, 'total_draft_msgs': 0}


def online_active_user(request):
    active_users = CustomUser.objects.all()
    return {'active_users': active_users}
