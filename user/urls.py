from django.urls import path
from . import views

# importing jwt views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_genarate'),     # view for token generation
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), # view for token refresh
    path('create-user/', views.CreateUser.as_view(), name='create_user'),
    path('all-books/', views.AllBooks.as_view(), name='all_books'),
    path('details/<int:id>/', views.Detail.as_view(), name='book_details'),
    path('borrow-book/', views.Borrow.as_view(), name='borrow_books'),
]