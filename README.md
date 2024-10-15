# SL-Online

This is a simple Python script that looks at Linden Lab's XML for user activity (https://api.secondlife.com/datafeeds/homepage.xml), reads the file structure, and then outputs users online and last updated into a Mastodon post, including custom text that can be set by you.

Instructions:
- install requirements.txt in a new environment
- copy the python script to a directory of your choosing
- input your access key that you'll have obtained from the Mastodon account that you're using (in the devolopment tab, create an app, copy the key)
- run python sl-onlinebot.py (or whatever you've chosen to name it)

And that should be it!

I made this, because, in all of the time I've been in Second Life, even if for the past year I've been mostly idle, and AFK, I *still* feel like a lot of the community and the world is very insular, and you don't really know what's happening, or how many people are even *there*, unless someone actually shows you. With this in mind, I decided to make an hourly stat that my own bot outputs to a Mastodon post, as as way to show people, "Hey, there are definitely people in Second Life!"

Maybe this will entice more to checkout the virtual world, or maybe it'll just be something neat that I've integrated with LL's API endpoint.

Either way, enjoy!
