import argparse
import requests
import json

def fetch_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_user_activity(activity):
    for event in activity:
        print(f"- {event['type'].capitalize()} {event['repo']['name']}")

def main():
    parser = argparse.ArgumentParser(description="Fetch and display GitHub user activity")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()
    activity = fetch_user_activity(args.username)
    if activity:
        display_user_activity(activity)
    else:
        print("Failed to fetch user activity")

if __name__ == "__main__":
    main()