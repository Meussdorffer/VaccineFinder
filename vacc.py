import os
import requests
import argparse

from twilio.rest import Client

URL = os.environ['VACC_URL']
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
FROM_PHONE = os.environ['TWILIO_PHONE']
USER_PHONE = os.environ['USER_PHONE']


def get_data(region_search) -> list:
    f = lambda datum: (
        region_search.lower() in datum.get('region', '').lower()
        and datum.get('availability').lower() == 'yes'
    )

    r = requests.get(URL)
    return list(filter(f, r.json()))


def send_mms(msg) -> None:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=msg,
        from_=FROM_PHONE,
        to=USER_PHONE
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('search', type=str)
    search_arg = parser.parse_args().search


    data = get_data(search_arg)
    if data:
        txt_msg = 'Vaccine available at the following locations:\n'
        txt_msg += '\n'.join({x.get('address') for x in data})
        send_mms(txt_msg)
    else:
        print('No data found...')
