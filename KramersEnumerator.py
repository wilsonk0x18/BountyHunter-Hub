import requests
import concurrent.futures

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

input_website = input('Input the website you want to discover with no subdomain: ')

def check_website(subdomain, counter, pass_list, fail_list):
    url = f"http://{subdomain}.{input_website}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            result = f'{url} - pass'
            pass_list.append(result)
        else:
            result = f'{url} - fail'
            fail_list.append(result)
    except requests.exceptions.RequestException:
        result = f'{url} - fail'
        fail_list.append(result)
    print(result)
    print(f"Out of {total_tasks} tasks, {counter + 1} are completed")

with open('subdomains-top1mil-5000.txt', 'r') as file:
    subdomains = [line.strip() for line in file]

total_tasks = len(subdomains)
counter = 0

pass_results = []  # List to store "pass" results
fail_results = []  # List to store "fail" results

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    for subdomain in subdomains:
        if subdomain:  # Check if subdomain is not empty
            check_website(subdomain, counter, pass_results, fail_results)
            counter += 1

# Display the pass and fail results
print("\n--- Pass Results ---")
for result in pass_results:
    print(result)

output_fail = input("would you like to also see the failed results? Y or n:    ")

if output_fail == "Y" or "y":
    print("\n--- Fail Results ---")
    for result in fail_results:
        print(result)

input("Press Enter to exit...")