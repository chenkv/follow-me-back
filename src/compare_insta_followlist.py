import json, os
from pprint import pprint

directory = "data"
following_name = "following.json"
followers_name = "followers_1.json"

try:
  with open(os.path.join(directory, following_name), "r") as following_file:
    following = json.load(following_file)

  with open(os.path.join(directory, followers_name), "r") as followers_file:
    followers = json.load(followers_file)
except Exception as e:
  print("An error occurred while trying to load the following and followers files:")
  print(e)
  exit(1)

if not following or not followers:
  print("Error loading in the following or followers file")
  exit(1)

result = []
for i in following.get("relationships_following"):
  found = False
  if len(i.get("string_list_data")) > 1:
    print(f"Something wrong with {i.get("string_list_data")[0].get("value")}")
  name = i.get("string_list_data")[0].get("value")
  
  for j in followers:
    compare_name = j.get("string_list_data")[0].get("value")
    
    if name == compare_name:
      found = True

  if not found:
    result.append(name)

print("These people are not following u back")
pprint(result)
print(len(result))