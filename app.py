from src.main import getLeetCodeData
from config import leetcode_name, query_fields


if __name__ == "__main__":
    data = getLeetCodeData(leetcode_name, query_fields)

    if data:
        print(data)
