# Serverless Log Analysis System

## Overview

This project is a serverless log analysis system built on AWS. It processes log files uploaded to Amazon S3, analyzes different log severity levels, stores analysis results in DynamoDB, and generates structured reports.

The goal of this project was to understand event-driven architecture and how multiple AWS services work together in a serverless environment.

---

## AWS Services Used

* Amazon S3
* AWS Lambda
* Amazon DynamoDB
* Amazon CloudWatch

---

## Workflow

1. A log file is uploaded to an S3 bucket.
2. AWS Lambda is triggered automatically.
3. The Lambda function reads and analyzes the log file.
4. Log severity levels are identified and counted.
5. The overall system health is determined.
6. Analysis results are stored in DynamoDB.
7. A JSON report is generated and stored in S3.
8. CloudWatch records execution logs for monitoring and debugging.

---

## Log Severity Levels

The system identifies the following log levels:

* INFO
* WARNING
* ERROR
* CRITICAL

---

## Sample Input

```txt
INFO User login successful
WARNING High memory usage
ERROR Database timeout
CRITICAL Payment service failure
```

---

## Sample Output

```json
{
  "INFO": 1,
  "WARNING": 1,
  "ERROR": 1,
  "CRITICAL": 1,
  "health": "CRITICAL"
}
```

---

## Future Improvements

Some possible improvements for future versions:

* Add automated alert notifications
* Improve error handling and retry mechanisms
* Create monitoring dashboards
* Support larger log files and batch processing
* Add real-time log streaming support

---

## Purpose of the Project

This project was built to gain hands-on experience with:

* Serverless computing
* Event-driven workflows
* AWS service integration
* Cloud monitoring and logging
* NoSQL database usage

---

## Demo

A demo video of the project workflow is available in the LinkedIn project post.
