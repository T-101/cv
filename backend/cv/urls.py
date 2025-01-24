from django.urls import path

from cv.views import LandingPageView, PortfolioItemView

app_name = 'cv'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('item/<slug:slug>/', PortfolioItemView.as_view(), name='portfolio_item'),
]
