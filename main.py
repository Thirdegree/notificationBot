import praw, obot, time

r = obot.login()

# Add subreddits seperated by '+' (e.g. Askreddit+funny+gifs+videos...)
subs = "thirdegree+thirdegree2"

def main():
    sub_stream = praw.helpers.submission_stream(r, subs, limit=None)
    for submission in sub_stream:
        if time.time() - submission.created_utc < 10800:        #if it's been created in the last 3 hours
            r.send_message(r.user, "New post", submission.permalink)
            print("sent")

if __name__ == '__main__':
    main()