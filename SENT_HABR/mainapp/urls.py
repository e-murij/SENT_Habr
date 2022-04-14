from django.urls import path, include

from .views import IndexListView, \
                    HelpListView, \
                    SectionListView, \
                    DesignListView, \
                    MarketingListView, \
                    MobileDevelopmentListView, \
                    WebDevelopmentListView

urlpatterns = [
    path('', IndexListView.as_view()),
    path('<int:pk>/', SectionListView.as_view(), name='section'),
    path('help', HelpListView.as_view(), name='help'),
    path('design', DesignListView.as_view(), name='design'),
    path('marketing', MarketingListView.as_view(), name='marketing'),
    path('mobile_development', MobileDevelopmentListView.as_view(), name='mobile_development'),
    path('web_development', WebDevelopmentListView.as_view(), name='web_development'),


    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('article/', include('articleapp.urls', namespace='article'), name='article'),
    path('account/', include('persaccapp.urls', namespace='account'), name='account'),
]
