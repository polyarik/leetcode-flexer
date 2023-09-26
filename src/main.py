import requests


def getLeetCodeData(username: str, query_fields):  # set[str]):
    base_url = "https://leetcode.com/graphql"

    query_data = f'matchedUser(username: "{username}") {{{query_fields}}}'
    print(query_data)

    full_url = f"{base_url}?query=query{{{query_data}}}"
    print(full_url)

    response = requests.get(full_url)
    print(response.status_code)
    print(response)

    json = response.json()
    # data = {"username": json["data"]["matchedUser"]["username"]}
    data = json  # temp
    return data
