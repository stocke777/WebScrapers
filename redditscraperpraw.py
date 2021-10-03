# praw is api for reddit
import praw
import json
import os

#Login using api credentials
client_id = "jK07XwjxfBwz8Uw4gUDACA"
client_secret = "KRRVsbeSYD05KAE9H0DFBND8-IKf6A"
user_agent = "apitest"
username = "Low_Organization144"
password = "login@reddit123"

#make reddit object
reddit = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent, username = username, password = password)
#make subreddit object
sub = reddit.subreddit("learnprogramming")
#request top 5 hot posts
hot = sub.hot(limit = 5)

#MAIN dictionary for all posts (if already exists, in Posts.json then parse it)
all_posts_dict = dict()
if not os.stat('Posts.json').st_size == 0:
    with open('Posts.json', "r") as f:
        data = json.loads(f.read())
        all_posts_dict = data

if not all_posts_dict:
    all_posts_dict = dict()
    all_posts_dict['posts'] = []

#MAIN dictionary for all comments (if already exists, in Comments.json then parse it)
all_comments_dict = dict()
if not os.stat('Comments.json').st_size == 0:
    with open('Comments.json', "r") as f:
        data = json.loads(f.read())
        all_comments_dict = data

if not all_comments_dict:
    all_comments_dict = dict()
    all_comments_dict['comments'] = []

#traverse the posts
for post in hot:
    if not post.stickied:
        
        post_dict = dict()
        
        post_dict['title'] = post.title
        post_dict['body'] = post.selftext
        post_dict['ups'] = post.ups
        post_dict['downs'] = post.downs
        post_dict['subreddit'] = str(sub)
        
        # add all details of the post into MAIN dictionary
        all_posts_dict['posts'].append(post_dict)

        for comment in post.comments:
            comment_dict = dict()
            comment_dict['body'] = comment.body
            comment_dict['ups'] = comment.ups
            comment_dict['downs'] = comment.downs
            comment_dict['subreddit'] = str(sub)

            # add all details of Comment into MAIN dictionary
            all_comments_dict['comments'].append(comment_dict)
            
# Write MAIN Posts dict into file
with open('Posts.json', 'w') as outfile:
    json.dump(all_posts_dict, outfile, indent=4)
# Write MAIN Comments dict into file
with open('Comments.json', 'w') as outfile:
    json.dump(all_comments_dict, outfile, indent=4)