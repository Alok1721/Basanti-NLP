#find out the twitter handle
import re

text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''

pattern = r'https://twitter\.com/([A-Za-z0-9_]+)'
twitter_handles = re.findall(pattern, text)
print(twitter_handles)

