from src.leetcode_api import get_leetcode_data
from src.data_formatter import format_for_telegram_desc
from config import leetcode_name, query_fields


if __name__ == "__main__":
    data = get_leetcode_data(leetcode_name, query_fields)

    if data:
        formatted = format_for_telegram_desc(data)
        print(formatted)
