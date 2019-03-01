#!/usr/bin/env python
"""
scripts/deploy_frontend.py

Deploy the frontend to the CDN. Read more at
    https://github.com/progteam/parrot/wiki/Deployment
"""
from mimetypes import MimeTypes
import glob
import os
import time

from tqdm import tqdm
import boto3


# Create boto3 clients
S3 = boto3.client(
    's3',
    aws_access_key_id=os.environ['PARROT_AWS_KEY_ID'],
    aws_secret_access_key=os.environ['PARROT_AWS_KEY_SECRET'])
CF = boto3.client(
    'cloudfront',
    aws_access_key_id=os.environ['PARROT_AWS_KEY_ID'],
    aws_secret_access_key=os.environ['PARROT_AWS_KEY_SECRET'])
# Read our targets
BUCKET = os.environ['PARROT_CDN_BUCKET']
DIST = os.environ['PARROT_CDN_DIST']

print('Uploading files...')
MIME = MimeTypes()
for filename in tqdm(glob.glob('frontend/build/**/*', recursive=True)):
    if not os.path.isdir(filename):
        # Try to fill the MIME type based on the filename. If we cannot make a
        # guess, then we assume it's a binary file.
        mime_type = MIME.guess_type(filename)[0]
        if mime_type is None:
            mime_type = 'application/octet-stream'
        # Upload the file to the s3 bucket with read permission
        S3.upload_file(
            filename,
            BUCKET,
            # The new filename on s3. We want to remove the frontend/build/
            # prefix from the name.
            filename.split('frontend/build/')[-1],
            ExtraArgs={
                'ACL': 'public-read',
                'ContentType': mime_type,
            })
print('Done.')

print('Creating invalidation...')
# Invaliate all assets caches on CloudFront
CF.create_invalidation(
    DistributionId=DIST,
    InvalidationBatch={
        'Paths': {
            'Quantity': 1,
            'Items': ['/*']
        },
        'CallerReference': str(time.time()),
    })
print('Done.')
