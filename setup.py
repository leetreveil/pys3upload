from distutils.core import setup

setup(
    name = 's3upload',
    version = '0.2.1',
    py_modules = ['s3upload'],
    author = 'Lee Treveil',
    author_email = 'leetreveil@gmail.com'
    description = 'A python module for uploading data to s3 using the s3 multipart API',
)