from django.conf import settings

lol_crypt = str.maketrans(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-@_.",
    settings.CRYPTO
)
