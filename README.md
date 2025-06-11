🚀 AWS Event-Driven Data Pipeline Overview
Data Ingestion:
Files are uploaded to the source S3 bucket.
This triggers an S3 event notification, which is sent to SNS (source SNS).

Message Handling:
The SNS pushes the message to an SQS queue.
An ETL Lambda is triggered by SQS to perform data transformation and invokes AWS Glue to process data.

Storage & Crawling:
Transformed data is stored in the target S3 bucket.
A second Lambda function is triggered via S3 events to run a Glue Crawler, which updates the Glue Catalog.

Querying & Analysis:
Updated metadata in Glue Catalog allows querying via Amazon Athena.

Monitoring & Alerts:
Failures are sent to a Dead-letter Queue, monitored by CloudWatch Alarms.
SNS (PD SNS) sends alerts to PagerDuty, which is integrated with Slack for real-time notifications.

Custom Events:
An EventBridge Rule can also trigger PD SNS for alerting via PagerDuty and Slack.
