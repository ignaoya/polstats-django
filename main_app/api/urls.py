from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views


app_name = 'courses'


urlpatterns = [
    path('articles/',
         views.ArticleListView.as_view(),
         name='article_list'),
    path('articles/<pk>/',
         views.ArticleDetailView.as_view(),
         name='article_detail'),
    path('countries/',
         views.CountryListView.as_view(),
         name='country_list'),
    path('countries/<pk>/',
         views.CountryDetailView.as_view(),
         name='country_detail'),
    path('sources/',
         views.SourceListView.as_view(),
         name='source_list'),
    path('sources/<pk>/',
         views.SourceDetailView.as_view(),
         name='source_detail'),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
