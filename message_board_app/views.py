from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from message_board_app.forms import MessageForm
from message_board_app.models import Message


# Create your views here.
class MessageList(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MessageDetail(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'


class MessageCreate(LoginRequiredMixin, CreateView):
    template_name = 'message_create.html'
    form_class = MessageForm
