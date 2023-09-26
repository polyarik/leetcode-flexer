def format_for_telegram_desc(data: dict) -> str:  # example: 🟢 42 🟡 32 🔴 9 | 420690
    result = ""

    # TODO - handle errors
    if "matchedUser" in data:
        user_data = data["matchedUser"]

        easy_solved = user_data["submitStats"]["acSubmissionNum"][1]["count"]
        medium_solved = user_data["submitStats"]["acSubmissionNum"][2]["count"]
        hard_solved = user_data["submitStats"]["acSubmissionNum"][3]["count"]
        ranking = user_data["profile"]["ranking"]

        result = f"🟢 {easy_solved} 🟡 {medium_solved} 🔴 {hard_solved} | {ranking}"

    return result
