import json
import os
import subprocess


def lambda_handler(event, context):
    if "numUsers" not in event or "region" not in event:
      return {
        'statusCode': 500,
        'body': json.dumps('numUsers and region must be passed in')
      }
    number_of_users = event['numUsers']
    region = event['region']
    batcmd="python test.py -r {region} -n {numUsers}".format(region=region, numUsers=number_of_users)
    cmd="python buildsubnets.py -r us-west-2 -n 6"
    result = subprocess.check_output(batcmd, shell=True)
    print(result.decode('utf-8'))
    if result == 'success':
        # run the cloudformation
        print('build cfn; now run')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
