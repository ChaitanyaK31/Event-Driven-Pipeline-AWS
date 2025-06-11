# Event-Driven-Pipeline-AWS
This AWS event-driven pipeline ingests S3 data, triggers ETL via Lambda and Glue, stores results in a target S3 bucket, runs a Glue Crawler to update the catalog, and enables querying via Athena. Failures trigger CloudWatch alarms, notifying PagerDuty and Slack through SNS and EventBridge.
