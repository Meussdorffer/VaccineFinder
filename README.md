# VaccineFinder
Find a vaccine near you!

## Usage
1. This script requires a Twilio account to run.
2. Install the packages in `requirements.txt`.
3. Set the following ENV variables:
    - URL: The URL to the data source for vaccine availability. 
    - ACCOUNT_SID: The SID of your Twilio account.
    - AUTH_TOKEN: The auth token of your Twilio account.
    - FROM_PHONE: The phone number associated to your Twilio account.
    - USER_PHONE: The phone number you'd like to send vaccine availability info to.


4. Then just run the following:

```
python vacc.py <city|state>
```
