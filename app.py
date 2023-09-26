from src.leetcode_api import get_leetcode_data
from config import leetcode_name, query_fields


if __name__ == "__main__":
    data = get_leetcode_data(leetcode_name, query_fields)

    if data:
        print(data)
