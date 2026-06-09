# 🚀 Serverless Log Analysis System

## 📌 Overview
This project is a serverless log analysis system built using AWS.

The system automatically analyzes log files uploaded to Amazon S3, classifies severity levels, stores historical analysis results in DynamoDB, and generates structured reports.

---

## 🧱 AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch

---

## ⚙️ Workflow

1. Upload log file to S3
2. Lambda function gets triggered
3. Logs are analyzed
4. Severity levels are counted
5. Results are stored in DynamoDB
6. JSON report is generated
7. CloudWatch stores execution logs

---

## 📊 Severity Levels

- INFO
- WARNING
- ERROR
- CRITICAL

---

## 📁 Sample Input

```txt
INFO User login successful
WARNING High memory usage
ERROR Database timeout
CRITICAL Payment service failure
```

---

## 📁 Sample Output

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

## 🚀 Future Improvements

- Add alerting system
- Add retry handling
- Add dashboard visualization
- Add automated notifications

---

## 🎥 Demo

LinkedIn demo video attached in project post.
