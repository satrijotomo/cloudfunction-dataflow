def main(event, context):
    from googleapiclient.discovery import build
    print('File: {}'.format(event['name']))

    project = '<your-project-id'
    job = '<any-job-name>'
    template = 'gs://dataflow-templates/latest/Word_Count'

    parameters = {
        #'inputFile': 'gs://dataflow-samples/shakespeare/kinglear.txt',
        'inputFile': 'gs://dstreambucket2820/{}'.format(event['name']),
        'output': 'gs://dstreambucket2820/wordcount/outputs',
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