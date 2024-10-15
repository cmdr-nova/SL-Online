import requests
import xml.etree.ElementTree as ET
from mastodon import Mastodon

# Function to fetch data from Second Life API for users online
def fetch_users_online_data():
    url = "https://api.secondlife.com/datafeeds/homepage.xml"
    
    response = requests.get(url)
    
    # Check if the response is valid, not everything is valid!
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    
    # Parse the XML data
    root = ET.fromstring(response.content)
    
    # Initialize us the variables!
    current_users_online = None
    current_users_online_updated = None
    
    # Extract the required fields from the active warzone.
    for stats in root.findall('.//map'):
        for i, elem in enumerate(stats):
            if elem.tag == 'key' and elem.text == 'inworld':
                current_users_online = stats[i + 1].text.strip()
            elif elem.tag == 'key' and elem.text == 'inworld_updated_slt':
                current_users_online_updated = stats[i + 1].text.strip()
    
    if current_users_online is None or current_users_online_updated is None:
        raise Exception("Error parsing data: Missing required fields")
    
    return current_users_online, current_users_online_updated

# Function to post data to Mastodon
def post_to_mastodon(users_online, users_online_updated, custom_text):
    mastodon = Mastodon(
        access_token='input_your_access_token',
        api_base_url='https://your.mastodon.instance'
    )
# This is the text that I personally output with the bot, feel free to change it to your liking if you use this script!   
    post_text = (
        f"{custom_text}\n"
        f"Current Users Online: {users_online} \n (Updated: {users_online_updated})"
        f"\n\n #SL #VirtualWorlds"
        f"\n Data fetched from: https://secondlife.com"
        f"\n Brought to you by @cmdr_nova@mkultra.monster"
    )
    mastodon.toot(post_text)

# Main function, plus a little more text. Not entirely sure why I put more custom text separate from the above, but ay, it works regardless.
def main():
    users_online, users_online_updated = fetch_users_online_data()
    custom_text = "The current amount of users online in #SecondLife:\n\n"
    post_to_mastodon(users_online, users_online_updated, custom_text)

if __name__ == "__main__":
    main()
