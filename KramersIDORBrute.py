import requests
from urllib.parse import urlparse

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


# Get user input for the website URL with !LIST! and the file path containing the word list
user_website = input("Enter the website you would like to brute force for valid webpages(Replace the positions you would like to enumerate with !LIST!) (DO NOT INCLUDE HTTP:// OR HTTPS://): ")
file_path = input("Enter the file path containing the word list: ")

# Read the word list from the specified file
with open(file_path, 'r') as file:
    word_list = [line.strip() for line in file]

# Check if the user input URL includes a scheme, if not, add 'http://'
parsed_url = urlparse(user_website)
scheme = parsed_url.scheme if parsed_url.scheme else 'http'

# Initialize lists to store valid and invalid URLs
valid_urls = []
invalid_urls = []

# Iterate through the word list and replace !LIST! with each word
for word in word_list:
    # Replace !LIST! with the current word and construct the full URL
    result_url = user_website.replace('!LIST!', word)
    full_url = f"{scheme}://{result_url}"  # Add the scheme

    # Send an HTTP GET request to the modified URL
    response = requests.get(full_url)

    # Check the status code to determine if the webpage is valid
    if response.status_code == 200:
        valid_urls.append(full_url)
    else:
        invalid_urls.append(full_url)

# Display valid URLs
if valid_urls:
    print("Valid URLs:")
    for url in valid_urls:
        print(url)

# Prompt the user to see invalid URLs
if invalid_urls:
    show_invalid = input("Do you want to see the invalid URLs? (yes/no): ").strip().lower()
    if show_invalid == "yes":
        print("Invalid URLs:")
        for url in invalid_urls:
            print(url)
    else:
        print("Invalid URLs not displayed.")

input("Press Enter to exit")













