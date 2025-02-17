#!/usr/bin/python3
"""This module demonstrates how to use the requests library to interact"""
import requests
import csv


def fetch_and_print_posts():
    """Send a GET request to fetch posts"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Send a GET request to fetch posts and save them to a CSV file"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        structured_data = [{'id': post['id'], 'title': post['title'],
                            'body': post['body']} for post in posts]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_data)
