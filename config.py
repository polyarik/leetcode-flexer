username = "PolYarik"  # your LeetCode username

# data requested from LeetCode # uncomment to request!
query_fields = {
    "matchedUser": {
        # "general": [
        #     "username",
        #     "submissionCalendar",
        # ],
        # "contributions": [
        #     "points",
        # ],
        "profile": [
            "ranking",
            # "reputation",
        ],
        "submitStats": {
            "acSubmissionNum": [
                "difficulty",
                "count",
                "submissions",
            ],
            # "totalSubmissionNum": [
            #     "difficulty",
            #     "count",
            #     "submissions",
            # ],
        },
    },
    # "userContestRanking": {
    #     "general": [
    #         "attendedContestsCount",
    #         "rating",
    #         "globalRanking",
    #         "totalParticipants",
    #         "topPercentage",
    #     ]
    # },
    # "userContestRankingHistory": {
    #     "general": [
    #         "attended",
    #         "trendDirection",
    #         "problemsSolved",
    #         "totalProblems",
    #         "finishTimeInSeconds",
    #         "rating",
    #         "ranking",
    #     ],
    #     "contest": [
    #         "title",
    #         "startTime",
    #     ],
    # },
}


# TODO: TOKEN - the Telegram bot token
# TODO: URL - the Heroku app link
