# odo-daily
A Tumblr bot that posts as Odo

All posts are in the format of "*No ___ on the Promenade!*"
The blank is filled through random words on inWords.txt
Each line is a should be what you want to fill the blank.

Run by using getWords.py

I based the ingWords dictionary off a FreeBSD dictionary, you can refresh the dictionary by running the getAll method.
**This will delete any custom words you have saved**

I have a method getIngWords sing -ing words sound better overall in the post format

You will need to make a tumblr secrets file inorder to post. Default name of the file is secrets_tumblr

Fill in your blogname in the blogName variable and you should be able to post

by default it queues 200 posts, you can raise this to a tumblr set max of 300
