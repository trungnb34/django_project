from django.urls import path
from .views import ping, registerUser, get_all_completed_tasks, \
    get_all_tasks_today
from .views import ColorList ,IconList, CategoryList, \
                    CategoryDetail, TaskList, TaskDeital
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("api/register", registerUser, name="register"),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    path('api/colors', ColorList.as_view(), name="color"),
    path('api/icons', IconList.as_view(), name="icon"),
    
    path('api/categories', CategoryList.as_view(), name="category"),
    path('api/category/<pk>', CategoryDetail.as_view(), name="category_detai"),

    path('api/tasks', TaskList.as_view(), name="task"),
    path('api/task/<pk>', TaskDeital.as_view(), name="task_detai"),

    path('api/get_completed_task', get_all_completed_tasks, name="completed_task"),
    path('api/today', get_all_tasks_today, name="today_task")
]