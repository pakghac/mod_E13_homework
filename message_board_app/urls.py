from django.urls import path

from message_board_app.views import MessageList, MessageDetail, MessageCreate

urlpatterns = [
    path('', MessageList.as_view()),
    path('<int:pk>', MessageDetail.as_view()),
    path('create', MessageCreate.as_view()),
]