from django.urls import path
from .views import UserView, UserDetailView, AdminView, ArtistView,UserRegister,CustomTokenObtainPairView
urlpatterns =[
    path("user/",UserView.as_view(), name="user-view"),
    path('register/', UserRegister.as_view(), name='user-list'),
    path("user/<int:pk>/",UserDetailView.as_view(), name="user-detail"),
    path("admin-view/",AdminView.as_view(), name="admin-view"),
    path("artist/",ArtistView.as_view(), name="artist-view"),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
 