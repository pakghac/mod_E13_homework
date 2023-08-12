from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from message_board_app.models import Message, Response
from message_board_app.filters import ResponseFilter

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
    model = Message
    template_name = 'message_create.html'
    fields = ['category', 'title', 'content']

    def form_valid(self, form):
        form.instance.messageAuthor = self.request.user
        return super().form_valid(form)


class ResponseCreate(LoginRequiredMixin, CreateView):
    model = Response
    template_name = 'response_create.html'
    fields = ['text']

    def form_valid(self, form):
        form.instance.responseAuthor = self.request.user
        form.instance.message = Message.objects.get(pk=self.request.GET.get('message_id'))
        return super().form_valid(form)


class ResponseList(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'response_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        return Response.objects.filter(message__messageAuthor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        return context


