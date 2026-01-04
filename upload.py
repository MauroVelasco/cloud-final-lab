import json, boto3, uuid
s3 = boto3.client('s3')
def upload_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    filename = body.get('filename', str(uuid.uuid4()))
    content_type = body.get('contentType', 'application/octet-stream')
    
    # Generate pre-signed PUT URL (valid for 15 mins)
    url = s3.generate_presigned_url('put_object', Params={
        'Bucket': "${UploadBucket}", 'Key': filename, 'ContentType': content_type
    }, ExpiresIn=900)
    
    return {
        "statusCode": 201,
        "headers": { "Location": url, "Access-Control-Allow-Origin": "*" },
        "body": json.dumps({"objectKey": filename, "uploadUrl": url})
    }
