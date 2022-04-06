# for service account requirement, check: 
# https://cloud.google.com/dataflow/docs/concepts/security-and-permissions#specifying_a_user-managed_worker_service_account
#
# wordcount template reference::
# https://cloud.google.com/dataflow/docs/guides/templates/provided-templates#wordcount
# https://beam.apache.org/get-started/wordcount-example/

from googleapiclient.discovery import build

def main(event, context):

    print('Processing File: {}'.format(event['name']))
    project = '<your-project-id'
    job = '<any-job-name>'
    template = 'gs://dataflow-templates/latest/Word_Count'

    parameters = {
        #'inputFile': 'gs://dataflow-samples/shakespeare/kinglear.txt',
        'inputFile': 'gs://<input-bucket-name>/{}'.format(event['name']),
        'output': 'gs://<output-bucket-name>/wordcount/outputs',
    }

    dataflow = build('dataflow', 'v1b3')
    request = dataflow.projects().templates().launch(
        projectId=project,
        gcsPath=template,
        body={
            'jobName': job,
            'parameters': parameters,
        }
    )
    response = request.execute()