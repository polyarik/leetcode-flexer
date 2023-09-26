import requests


BASE_URL = "https://leetcode.com/graphql"


def get_leetcode_data(username: str, query_fields: dict) -> dict | None:
    request_body = construct_request_body(query_fields, username)
    full_url = f"{BASE_URL}?query=query{{{request_body}}}"
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
        data = json["data"]
        return data


# TODO: handle empty fields
def construct_request_body(query_fields: dict, username: str = None) -> str:
    result = ""

    for field_name, value in query_fields.items():
        if username is not None:
            result += f'{field_name}(username: "{username}") {{{construct_request_body(value)}}}'
            result += " "
        elif field_name == "general":
            result += " " + " ".join(value)
        elif isinstance(value, list):
            result += " " + f"{field_name} {{ {' '.join(value)} }}"
        elif isinstance(value, dict):
            result += " " + f"{field_name} {{ {construct_request_body(value)} }}"

    return result
