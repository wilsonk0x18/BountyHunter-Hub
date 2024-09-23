import requests

url = "https://example.com"  # Replace with the URL you want to check

try:
    response = requests.get(url)
    response.raise_for_status()  # This will raise an exception if there's an HTTP error (e.g., 404)

    # Check if the response times out
    if response.elapsed.total_seconds() > 5:  # Adjust the timeout value as needed
        print("The website timed out.")
    else:
        print("The website exists and is responsive.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
