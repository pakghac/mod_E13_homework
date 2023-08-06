from django.forms import ModelForm

from message_board_app.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['category', 'title', 'content']
