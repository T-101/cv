from django.conf import settings

lol_crypt = str.maketrans(settings.CHAR_SET, settings.CRYPTO)
