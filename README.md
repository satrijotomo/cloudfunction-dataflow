# GCP: Cloud Function to Trigger Dataflow template

This repo is meant to give an example of triggering a dataflow template, in this case "Word count" template, and trigger the function based on the arrival of a file in the storage bucket. The word count is then run on the file.

Create the cloud function as "Cloud Storage" trigger type and "Finalize/Create" event type.

### Reference:
https://cloud.google.com/dataflow/docs/guides/templates/running-templates#using-the-rest-api



### Disclaimer:
The code in this repo is provided as is. Use it at your own risk. 