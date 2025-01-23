from django.db.models.functions import Lower
from django.views.generic import TemplateView

from cv.models import PersonalInfo, PortfolioItemTag


class LandingPageView(TemplateView):
    template_name = 'cv/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["info"] = PersonalInfo.load()
        ctx["tags"] = PortfolioItemTag.objects.order_by(Lower("tag"))
        return ctx
