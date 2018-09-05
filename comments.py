import facebook
import requests
import re

ACCESS_TOKEN="EAAehyoyl7mkBAPqUZCmS4pgi80jLp6sGbVpBrzClcKiC8fg6AqD7BpkYuXlfVzR2hpN2pbOusKPXD05ihxaauAT8faLmZAiZBYvlNBZBbAfwZBkZCWXRK4nEZBtvMgAXksfCKZA7UgNCZC6vZAtH8ZCXVBH18ZCOwhKl9aiK6eRjUZBCDUCasDpRI0ko5X3Y9tCGbGcYZD"
user_token="1067581170297125|g1LynV8p5zZ8RAjQpeFEYq-aG5A"
access_token=ACCESS_TOKEN
page_access_token="EAAehyoyl7mkBAIi5w5wtZBQgM3ZAjmNhdwPDauhEvPlO5bDyNoTDSW6oVS62LAZCM37xZBvOWurCZAncbU5wJnULFNaAtvJQb8fLyZAT0SCu0i8DGrwY20lvykclNDqlsDnk2NoxdUiK9yWOyRxsZBcW6lIhTcv083xnrSMiOOEs8YvVs5yyXLNKbMR7xdanZBgZD"
page_token = page_access_token
user1="elpecosgrill"



graph=facebook.GraphAPI(access_token=page_token, version='2.7')
profile=graph.get_object(user1)
posts=graph.get_connections(id=user1,connection_name ='posts', fields='comments', limit=100)


for i, j in posts.items():
    for items in j:
        thelist=(items)
        otherlist=thelist.get('comments')
        if not otherlist:
         continue
        for l,m in otherlist.items():
                for p in m:
                    try:
                     if p.get('message'):
                         split = re.sub(r"[^a-zA-Z0-9\s]",' ',p.get('message')).lower().split()
                         replies = {"abcde": "hello to you too!"}
                         for item in split:
                             if item in replies:
                                response = p.get('id')
                                idfile=open("comment_ids.txt","r")
                                if response not in idfile:
                                    idfile1=open("comment_ids.txt","a")
                                    idfile1.write("\n" + response)
                                    graph.put_comment(object_id=response, message=replies.values())
                                    idfile1.readlines()
                                    idfile1.close()
                                    print(q)
                                else:
                                    print("hello")

                    except AttributeError:
                        continue
