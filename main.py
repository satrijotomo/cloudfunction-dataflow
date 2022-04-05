from googleapiclient.discovery import build

def main(event, context):

    print('Processing File: {}'.format(event['name']))
    project = '<your-project-id'
    job = '<any-job-name>'
    template = 'gs://dataflow-templates/latest/Word_Count'

    parameters = {
        #'inputFile': 'gs://dataflow-samples/shakespeare/kinglear.txt',
        'inputFile': 'gs://<bucket-name>/{}'.format(event['name']),
        'output': 'gs://<bucket-name>/wordcount/outputs',
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