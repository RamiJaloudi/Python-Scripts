import argparse
import twitter_functions

def main():
    parser = argparse.ArgumentParser()
    woeid = None

    parser.add_argument("-s", "--search",
                      type=str,
                      dest="search_term",
                      nargs=1,
                      help="Display tweets containing a particular string.")

    parser.add_argument("-t", "--trending-topics",
                      action="store_true",
                      help="Display the trending topics.")

    parser.add_argument("-u", "--user-tweets",
                      type=str,
                      action="store",
                      dest="userid",
                      help="Display a user's tweets.")

    parser.add_argument("-w", "--trending-tweets",
                      action="store_true",
                      dest="trending_tweets",
                      help="Display tweets from all of the trending topics.")


    parser.add_argument("-o", "--woeid",
                      type=int,
                      dest="woeid",
                      nargs='?',
                      help="Localize to a particular WOEID. (Only affects -t and -w)")

    args = parser.parse_args()
    if args.woeid:
        woeid = args.woeid

    if args.search_term:
        twitter_functions.search(args.search_term)
    elif args.trending_topics:
        twitter_functions.trendingTopics(woeid)
    elif args.userid:
        twitter_functions.userTweets(args.userid)
    elif args.trending_tweets:
        twitter_functions.trendingTweets(woeid)

if __name__ == "__main__":
    main()