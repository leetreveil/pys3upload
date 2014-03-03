from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name = 's3upload',
    version = '0.2.4',
    py_modules = ['s3upload'],
    author = 'Lee Treveil',
    author_email = 'leetreveil@gmail.com',
    description = 'A python module for uploading data to s3 using the s3 multipart API',
    long_description=readme(),
    license = "MIT",
    url = "https://github.com/leetreveil/pys3upload",
    entry_points = {
        'console_scripts': [
            's3upload = s3upload:cli',
        ],
    },
    install_requires = ['boto>=2.26'],
    keywords = ['s3', 'multipart', 'upload', 'amazon'],
)
