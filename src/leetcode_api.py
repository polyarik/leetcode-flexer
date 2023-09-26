import requests


BASE_URL = "https://leetcode.com/graphql"


def get_leetcode_data(username: str, query_fields: dict) -> dict | None:
    query_body = parse_fields(query_fields)
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
        data = json["data"]["matchedUser"]
        return data


def parse_fields(fields: dict) -> str:
    result = ""

    for key, value in fields.items():
        if key == "general":
            result += " " + " ".join(value)
        elif isinstance(value, list):
            result += " " + f"{key} {{ {' '.join(value)} }}"
        elif isinstance(value, dict):
            result += " " + f"{key} {{ {parse_fields(value)} }}"

    return result
