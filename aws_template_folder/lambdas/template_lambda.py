import json
import boto3
import os
import yaml

def events_handler(event, context):
    # Log the event for debugging
    print("Event:", json.dumps(event))

    s3 = boto3.client('s3')

    for record in event['Records']:
        # Get bucket and file name that triggered this Lambda
        bucket_name = record['s3']['bucket']['name']
        trigering_file_name = record['s3']['object']['key']
        print(f"Triggered by file: {trigering_file_name} in bucket: {bucket_name}")
       
        # Example of download of file from S3 + read as YAML
        s3.download_file(bucket_name, trigering_file_name, f'/tmp/{trigering_file_name}')
        task = yaml.safe_load(open(f'/tmp/{trigering_file_name}'))

        # Example of extracting parameters from YAML
        forum_id = task.get("forum_id")
        bypass_cf = task.get("bypass_cloudflare", 0)

        result_files = ["fetched_data.txt"]  # Example result file
        status = {"status": "done", "success": True}

        # Example of upload results to S3, under key task_id
        for fn in result_files:      
           try: 
               s3.upload_file("/tmp/" + fn, bucket_name, f"{task_id}/{fn}")
               print(f"Successfully uploaded {fn} to s3://{bucket_name}/{task_id}")
           except Exception as e:
               print(f"Failed to upload {fn} to {bucket_name}: {e}")
 
        # Upload status file, indicating we are done
        status_file_name = f"status_{task_id}.yaml"
        yaml.safe_dump(status, open(f"/tmp/{status_file_name}", 'w'))
        try:
            s3.upload_file("/tmp/" + status_file_name, bucket_name, status_file_name)
            print(f"Successfully uploaded {status_file_name} to {bucket_name}.")
        except Exception as e:
            print(f"Failed to upload {status_file_name} to {bucket_name}: {e}")
 
    return {
        'statusCode': 200,
        'body': json.dumps('Processing completed')
    }

if _name_=="_main_":
    event = { 'Records': [ {'s3': {'bucket': {'name': "bn"}, 'object': {'key': "task_111.yaml"}}}]}
    events_handler(event, "")
