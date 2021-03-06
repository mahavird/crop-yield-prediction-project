import os
import time

buckets = ['cs231n-satellite-images', 'cs231n-satellite-images-clean', 'cs231n-satellite-images-hist', 'cs231n-satellite-images-models']

for bucket in buckets:
    bucketPath = os.path.expanduser('~/' + bucket)
    checkPath = bucketPath + '/dirEmptyCheck'
    bucketName = bucket
    try:
        os.listdir(checkPath)
    except OSError:
        os.system('gcsfuse %s %s' % (bucketName, bucketPath))
        os.system('touch %s' % checkPath)
    time.sleep(3)
