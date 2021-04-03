import json
from vacc import find_vaccine

ERR = {
    'statusCode': 404,
    'body': "Something went wrong, but I'm too lazy to tell you what it was."
}

def lambda_handler(event, context):
    search = event.get('search')
    if not search:
        return ERR

    find_vaccine(search)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
