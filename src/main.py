import requests


BASE_URL = "https://leetcode.com/graphql"


def getLeetCodeData(username: str, query_fields: dict):
    query_body = constructQueryBody(query_fields)
    query_data = f'matchedUser(username: "{username}") {{{query_body}}}'
    full_url = f"{BASE_URL}?query=query{{{query_data}}}"
    print(full_url)

    try:
        response = requests.get(full_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(f"Request failed: {error}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")
    else:
        json = response.json()
        # TODO: build result
        data = json["data"]["matchedUser"]
        return data


def constructQueryBody(query_fields: dict) -> str:
    query_body = ""

    for field, values in query_fields.items():
        if field == "general":
            query_body += " ".join(values) + " "
        else:
            query_body += f'{field} {{{" ".join(values)}}}' + " "

    return query_body
