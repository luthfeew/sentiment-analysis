import stweet as st


def try_search():
    search_tweets_task = st.SearchTweetsTask(all_words="bsnget sama bang junot")
    output_jl_tweets = st.JsonLineFileRawOutput("output_raw_search_tweets.jl")
    output_jl_users = st.JsonLineFileRawOutput("output_raw_search_users.jl")
    output_print = st.PrintRawOutput()
    st.TweetSearchRunner(
        search_tweets_task=search_tweets_task,
        tweet_raw_data_outputs=[output_print, output_jl_tweets],
        user_raw_data_outputs=[output_print, output_jl_users],
    ).run()


def try_tweet_by_id_scrap_1():
    id_task = st.TweetsByIdTask("1575282529426444291")
    output_json = st.JsonLineFileRawOutput("output_raw_id_1.jl")
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(
        tweets_by_id_task=id_task, raw_data_outputs=[output_print, output_json]
    ).run()


def try_tweet_by_id_scrap_2():
    id_task = st.TweetsByIdTask("1577951557059956736")
    output_json = st.JsonLineFileRawOutput("output_raw_id_2.jl")
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(
        tweets_by_id_task=id_task, raw_data_outputs=[output_print, output_json]
    ).run()


def try_tweet_by_id_scrap_3():
    id_task = st.TweetsByIdTask("1595119378462560257")
    output_json = st.JsonLineFileRawOutput("output_raw_id_3.jl")
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(
        tweets_by_id_task=id_task, raw_data_outputs=[output_print, output_json]
    ).run()


def try_tweet_by_id_scrap_4():
    id_task = st.TweetsByIdTask("1596535050262106114")
    output_json = st.JsonLineFileRawOutput("output_raw_id_4.jl")
    output_print = st.PrintRawOutput()
    st.TweetsByIdRunner(
        tweets_by_id_task=id_task, raw_data_outputs=[output_print, output_json]
    ).run()


if __name__ == "__main__":
    # try_search()
    try_tweet_by_id_scrap_1()
    try_tweet_by_id_scrap_2()
    try_tweet_by_id_scrap_3()
    try_tweet_by_id_scrap_4()
