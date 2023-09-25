import requests


def getLeetCodeData(username: str):
    base_url = "https://leetcode.com/graphql"

    query_data = f'matchedUser(username: "{username}") {{username}}'
    # query_data = 'matchedUser(username: "PolYarik") {username}'
    print(query_data)

    full_url = f"{base_url}?query=query{{{query_data}}}"
    response = requests.get(full_url)

    print(response.status_code)
    print(response)

    json = response.json()
    data = {"username": json["data"]["matchedUser"]["username"]}
    return data
