import requests


BASE_URL = "https://leetcode.com/graphql"


def getLeetCodeData(username: str, query_fields: dict):
    query_body = constructQueryBody(query_fields)
    query_data = f'matchedUser(username: "{username}") {{{query_body}}}'
    full_url = f"{BASE_URL}?query=query{{{query_data}}}"
    print(full_url)

    response = requests.get(full_url)
    print(response.status_code)
    print(response)

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
