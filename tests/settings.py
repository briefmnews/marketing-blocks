SECRET_KEY = "dump-secret-key"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.admin",
    "marketing_blocks",
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

TEMPLATES = [
    {"BACKEND": "django.template.backends.django.DjangoTemplates",},
]
