from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, SignupView
# DefaultRouter — auto-generates CRUD URLs for ViewSets


# ─── Router for Task CRUD ──────────────────────────────────────────────────────
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # Creates /api/tasks/ with GET, POST, PUT, DELETE


urlpatterns = [
    path('', include(router.urls)),                    # All task routes
    path('auth/signup/', SignupView.as_view()),         # POST /api/auth/signup/
]