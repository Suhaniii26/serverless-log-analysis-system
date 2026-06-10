import boto3
import uuid
import json
from datetime import datetime

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

TABLE_NAME = "LogAnalysisHistory"

def lambda_handler(event, context):
    
    bucket = event["bucket"]
    file_key = event["file"]

    response = s3.get_object(Bucket=bucket, Key=file_key)
    content = response["Body"].read().decode("utf-8")

    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "CRITICAL": 0
    }

    for line in content.splitlines():
        for level in counts:
            if level in line:
                counts[level] += 1

    if counts["CRITICAL"] > 0:
        health = "CRITICAL"
    elif counts["ERROR"] > 3:
        health = "UNSTABLE"
    else:
        health = "HEALTHY"

    analysis_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            "analysisId": analysis_id,
            "file": file_key,
            "timestamp": timestamp,
            "counts": counts,
            "health": health
        }
    )

    report = {
        "file": file_key,
        "timestamp": timestamp,
        "counts": counts,
        "health": health
    }

    report_key = f"reports/{analysis_id}.json"

    s3.put_object(
        Bucket=bucket,
        Key=report_key,
        Body=json.dumps(report, indent=2),
        ContentType="application/json"
    )

    return {
        "message": "Log analysis completed",
        "analysisId": analysis_id,
        "health": health,
        "reportFile": report_key
    }