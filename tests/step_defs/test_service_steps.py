import requests
from pytest_bdd import scenarios, given, when, then, parsers
from colorama import Fore


# Scenarios
scenarios('../features/Service.feature')


# When Steps
@given(parsers.parse('the endpoint "{endpoint}"'), target_fixture='get_endpoint')
def get_endpoint(endpoint):
    response = requests.get(endpoint)
    print(Fore.GREEN + response.text)

    json_response = response.json()
    oneFact = json_response['fact']
    print(Fore.RED + oneFact)

    file = open('../../Data/cat_fact.json', "w")
    file.write(response.text)
    return response


@then(parsers.parse('obtain status code "{code:d}"'))
def check_status_code(get_endpoint, code):
    assert get_endpoint.status_code == code
    print(Fore.GREEN + 'Successful response')
