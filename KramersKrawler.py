import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import re

# List of base URLs to check
base_urls = ["https://www.tiktok.com/@", "https://www.youtube.com/@", "https://www.reddit.com/user/", "https://www.instagram.com/", "https://www.pinterest.com/"]

splash_screen = """
      ,-.                               ____                    
  ,--/ /|                             ,'  , `.                  
,--. :/ |   __  ,-.                ,-+-,.' _ |          __  ,-. 
:  : ' /  ,' ,'/ /|             ,-+-. ;   , ||        ,' ,'/ /| 
|  '  /   '  | |' | ,--.--.    ,--.'|'   |  || ,---.  '  | |' | 
'  |  :   |  |   ,'/       \  |   |  ,', |  |,/     \ |  |   ,' 
|  |   \  '  :  / .--.  .-. | |   | /  | |--'/    /  |'  :  /   
'  : |. \ |  | '   \__\/: . . |   : |  | ,  .    ' / ||  | '    
|  | ' \ \;  : |   ," .--.; | |   : |  |/   '   ;   /|;  : |    
'  : |--' |  , ;  /  /  ,.  | |   | |`-'    '   |  / ||  , ;    
;  |,'     ---'  ;  :   .'   \|   ;/        |   :    | ---'     
'--'             |  ,     .-./'---'          \   \  /           
                  `--`---'                    `----'        

________________________________________________________________
________________________________________________________________


"""

print(splash_screen)


# Input for username
user_name = input("Enter a username to search for: ")

print("Searching for the username " + user_name + " across the web")

# Regular expressions for page titles
keywords_to_check = [
    r"This account doesn't exist",  # Use regular expression for flexibility
    r"Page not found • Instagram",
    r"(3) Reddit - Dive into anything",
]

# Function to check a URL
def check_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text  # Return the webpage content

    except requests.exceptions.RequestException:
        return None

# Create a list of modified URLs with the username appended
modified_urls = [base_url + user_name for base_url in base_urls]

# Create a ThreadPoolExecutor to run checks concurrently
with ThreadPoolExecutor(max_workers=7) as executor:
    results = list(executor.map(check_url, modified_urls))

# Function to determine existence based on keywords in the title
def determine_existence(title):
    for keyword in keywords_to_check:
        if re.search(keyword, title, re.I):  # Perform a case-insensitive search
            return "may not exist"
    return "may exist"

# Print the results
for url, result in zip(modified_urls, results):
    if result is not None:
        soup = BeautifulSoup(result, "html.parser")
        title = soup.title.string  # Extract the page title
        existence_status = determine_existence(title)
        print(f"{url} - {existence_status}")
    else:
        print(f"{url} - Request failed")

input("Press Enter to exit")











