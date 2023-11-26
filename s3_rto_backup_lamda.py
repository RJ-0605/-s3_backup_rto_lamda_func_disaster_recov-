import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Logic to handle backup to S3
    # Example: Copying a file from one bucket to another
    source_bucket = 'source-bucket-name'
    target_bucket = 'target-bucket-name'
    file_name = 'file-to-backup.txt'

    copy_source = {'Bucket': source_bucket, 'Key': file_name}
    s3.copy(copy_source, target_bucket, file_name)

    return {
        'statusCode': 200,
        'body': json.dumps('Backup successful')
    }
