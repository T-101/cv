from django.urls import path

from cv.views import LandingPageView

app_name = 'cv'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
]
