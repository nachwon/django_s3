from django.core.files.storage import Storage
from storages.backends.s3boto import S3BotoStorage


class S3Storages(S3BotoStorage):
    pass