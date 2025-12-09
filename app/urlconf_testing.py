from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChatView.as_view(), name='chat'),
    path('login/', views.OperatorLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('login/operator/', views.OperatorLoginView.as_view(), name='login_operator'),
    path('login/admin/', views.AdminLoginView.as_view(), name='login_admin'),
    path('suggestions/<uuid:chat_id>/', views.SuggestedResponsesView.as_view(), name='suggestions'),
    path('history/<uuid:chat_id>/', views.ChatHistoryView.as_view(), name='history'),
    path('operator/', views.OperatorView.as_view(), name='operator'),
    path('operator/close/<uuid:chat_id>/', views.CloseChatView.as_view(), name='close_chat'),
    path('admin/dashboard/stats/', views.AdminStatsAPIView.as_view(), name='admin_stats_api'),
    path('admin/dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/report/', views.AdminGeneratePDFView.as_view(), name='admin_report'),
    path('admin/staff/', views.AdminStaffView.as_view(), name='admin_staff'),
    path('admin/staff/list/', views.AdminStaffListView.as_view(), name='admin_staff_list'),
    path('admin/staff/<int:user_id>/', views.AdminStaffUserView.as_view(), name='admin_staff_user'),
    path('admin/knowledge/', views.AdminKnowledgeView.as_view(), name='admin_knowledge'),
    path('admin/knowledge/list/', views.AdminKnowledgeListView.as_view(), name='admin_knowledge_list'),
    path('admin/knowledge/<int:knowledge_id>/', views.AdminKnowledgeItemView.as_view(), name='admin_knowledge_item'),
]
