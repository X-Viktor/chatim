from django.urls import path

from chat.views import ChatListView, LoginView, ajax_load_messages

urlpatterns = [
    path('chat/', ChatListView.as_view(), name='chat'),
    path("ajax/<int:pk>/", ajax_load_messages, name="chat-ajax"),

    path('login/', LoginView.as_view(), name='login'),
]
