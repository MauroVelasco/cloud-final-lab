import boto3
s3 = boto3.client('s3')
def download_handler(event, context):
    object_key = event['pathParameters']['objectKey']
    
    # Generate pre-signed GET URL (valid for 1 hour)
    url = s3.generate_presigned_url('get_object', Params={
        'Bucket': "${UploadBucket}", 'Key': object_key
    }, ExpiresIn=3600)
    
    return {
        "statusCode": 302,
        "headers": { "Location": url }
    }