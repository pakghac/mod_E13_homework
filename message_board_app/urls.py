from django.urls import path

from message_board_app.views import MessageList, MessageDetail, MessageCreate, ResponseCreate, ResponseList

urlpatterns = [
    path('', MessageList.as_view()),
    path('<int:pk>', MessageDetail.as_view()),
    path('create', MessageCreate.as_view()),
    path('response_create', ResponseCreate.as_view(), name='response_create'),
    path('response_list', ResponseList.as_view()),
]