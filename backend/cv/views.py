import random

from django.conf import settings
from django.db.models.functions import Lower
from django.views.generic import TemplateView

from cv.models import PersonalInfo, PortfolioItemTag


class LandingPageView(TemplateView):
    template_name = 'cv/index.html'

    @staticmethod
    def _get_crypto():
        chars = list(settings.CHAR_SET)
        random.shuffle(chars)
        return "".join(chars)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["info"] = PersonalInfo.load()
        ctx["tags"] = PortfolioItemTag.objects.order_by(Lower("tag"))
        ctx["crypto"] = self._get_crypto()
        ctx['char_set'] = settings.CHAR_SET
        return ctx
