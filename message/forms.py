from django import forms
from .models import NewMessage


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'placeholder': 'Write your message here ......'})

    class Meta:
        model = NewMessage
        fields = ['message', 'msg_status']


class DraftMessageSendForm(forms.ModelForm):
    class Meta:
        model = NewMessage
        fields = ['receiver', 'message']



class WriteNewMessage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WriteNewMessage, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'placeholder': 'Write your message here ....'})

    class Meta:
        model = NewMessage
        fields = ['receiver', 'message', 'msg_status']



class SendMessageForm(forms.ModelForm):
    class Meta:
        model = NewMessage
        fields = ['message', ]


class ReplyMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReplyMessageForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write your reply here....'})

    class Meta:
        model = NewMessage
        fields = ['message', ]