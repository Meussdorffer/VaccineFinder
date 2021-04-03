import os
try:
    import requests
except:
    from botocore.vendored import requests
import argparse


from twilio.rest import Client

URL = os.environ['VACC_URL']
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
FROM_PHONE = os.environ['TWILIO_PHONE']
TO_PHONES = os.environ['USER_PHONE'].split(',')


def get_data(region_search, addr_search=None) -> list:
    addr_search = region_search if not addr_search else addr_search
    f = lambda datum: (
        region_search.lower() in datum.get('region', '').lower()
        and datum.get('availability').lower() == 'yes'
        and addr_search.lower() in datum.get('address', '').lower()
    )

    r = requests.get(URL)
    return list(filter(f, r.json()))


def send_mms(msg) -> None:

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for phone_num in TO_PHONES:
        print(f'Sending text to {phone_num}')
        client.messages.create(
            body=msg,
            from_=FROM_PHONE,
            to=phone_num
        )
        break

def find_vaccine(search_arg):
    data = get_data(search_arg)
    if data:
        print(f'Found vaccines for {len(data)} locations!')
        txt_msg = '\n\nVaccine available at the following locations:\n\n'
        txt_msg += '\n\n'.join({x.get('address') for x in data})
        txt_msg += '\n\n\nSign up for your appointment below!\n\n'

        if len(txt_msg) > 1500:
            txt_msg = txt_msg[:1500]

        txt_msg += 'https://www.mhealthappointments.com/covidappt'
        send_mms(txt_msg)
    else:
        print('No data found...')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('search', type=str)
    search_arg = parser.parse_args().search
    find_vaccine(search_arg)
