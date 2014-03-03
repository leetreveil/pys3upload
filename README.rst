##########
pys3upload
##########

.. image:: https://travis-ci.org/leetreveil/pys3upload.png
        :target: https://travis-ci.org/leetreveil/pys3upload

A python module for uploading data to s3 using the multipart API.

Installation
------------

Install via `pip`_:

.. code:: bash

    $ pip install s3upload


CLI
---

Use the s3upload CLI to upload from stdin or from data provided on the command line.

.. code:: bash

    Usage: s3upload [options]

    Options:
      -h, --help            show this help message and exit
      -b BUCKET, --bucket=BUCKET
                            the s3 bucket to upload to
      -k KEY, --key=KEY     the name of the key to create in the bucket
      -K AWS_KEY, --aws_key=AWS_KEY
                            aws access key
      -s AWS_SECRET, --aws_secret=AWS_SECRET
                            aws secret key
      -d DATA, --data=DATA  the data to upload to s3 -- if left blank will be read
                            from STDIN
      -t THREADS, --threads=THREADS
                            number of threads to use while uploading in parallel

Module
------

You can also interface with the module from python:

.. code:: python

    >>> from s3upload import upload

.. code:: python

    def upload(bucket, aws_access_key, aws_secret_key,
           iterable, key, progress_cb=None,
           threads=5, replace=False, secure=True):
    ''' Upload data to s3 using the s3 multipart upload API.

        Args:
            bucket: name of s3 bucket
            aws_access_key: aws access key
            aws_secret_key: aws secret key
            iterable: The data to upload. Each 'part' in the list
            will be uploaded in parallel. Each part must be at
            least 5242880 bytes (5mb).
            key: the name of the key to create in the s3 bucket
            progress_cb: will be called with (part_no, uploaded, total)
            each time a progress update is available.
            threads: the number of threads to use while uploading.
            replace: will replace the key in s3 if set to true. (Default is false)
            secure: use ssl when talking to s3. (Default is true)
    '''

Licence
-------
MIT

.. _pip: http://www.pip-installer.org/