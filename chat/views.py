import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as Login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from chat.forms import LoginForm
from chat.models import Chat, Message


class ChatListView(LoginRequiredMixin, generic.ListView):
    """ Отображение чата. """
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

    model = Chat
    context_object_name = 'chats'
    template_name = 'chat/chat.html'

    def get_queryset(self):
        return Chat.objects.filter(members=self.request.user).prefetch_related('messages')


class LoginView(Login):
    """Авторизация."""
    redirect_authenticated_user = True
    form_class = LoginForm
    template_name = 'login.html'


@login_required
def ajax_load_messages(request, pk):
    """ Получение/отправка сообщения. """
    chat = get_object_or_404(Chat, pk=pk)
    messages = Message.objects.filter(chat=chat).select_related('sender')
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "time": message.date_sending,
    } for message in messages]

    if request.method == "POST":
        message = json.loads(request.body)
        m = Message.objects.create(message=message, sender=request.user, chat=chat)
        message_list.append({
            "sender": request.user.username,
            "message": m.message,
            "time": m.date_sending,
        })
    return JsonResponse({
        "messages": message_list,
        "chat_title": chat.title,
    }, safe=False)
