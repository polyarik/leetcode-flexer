def format_for_telegram_desc(data: dict) -> str:  # example: 🟢 42 🟡 32 🔴 9 | 420690
    user_data: dict = data.get("matchedUser", {})

    submit_stats: dict = user_data.get("submitStats", {})
    ac_submission_num: list = submit_stats.get("acSubmissionNum", [])
    easy_solved: int = ac_submission_num[1].get("count", 0)
    medium_solved: int = ac_submission_num[2].get("count", 0)
    hard_solved: int = ac_submission_num[3].get("count", 0)

    profile: dict = user_data.get("profile", {})
    ranking: int = profile.get("ranking", 0)

    result = f"🟢 {easy_solved} 🟡 {medium_solved} 🔴 {hard_solved} | {ranking}"

    return result
