from distutils.core import setup

setup(
    name = 's3upload',
    version = '0.2.0',
    py_modules=['s3upload'],
    description = 'A python module for uploading data to s3 using the s3 multipart API',
)