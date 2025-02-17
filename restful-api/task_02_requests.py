#!/usr/bin/python3

def fetch_and_print_posts():
    """Fetches and prints posts from the API"""
    
    import requests

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    print(f"Status code: {response.status_code}")
    for posts in posts:
        print(posts["title"])

def fetch_and_save_posts():
    """Fetches and saves posts from the API"""
    
    import requests
    import csv

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    if response.status_code == 200:
        posts = response.json()
        data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
        with open("posts.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
