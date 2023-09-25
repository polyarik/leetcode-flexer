from src.main import getLeetCodeData
from src.config import leetcode_name


if __name__ == "__main__":
    data = getLeetCodeData(leetcode_name)
    print(data)
