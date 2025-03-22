#!/usr/bin/python3
"""
Module for genreating file invitations
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendee list.
    """
    if not isinstance(template, str):
        print("Error: template must be a string")
        return []
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries")
        return []

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: all attendees must be dictionaries")
        return []

    # Handle empty content cases
    if not template:
        print("Template is empty, no output files generated.")
        return []

    if not attendees:
        print("No data provided, no output files generated.")
        return []

    required_fields = ["name", "event_title", "event_date", "event_location"]
    for index, attendee in enumerate(attendees, start=1):
        replaced = template
        for field in required_fields:
            value = attendee.get(field)
            if value is None:
                value = f'{field}: N/A'
            str_value = str(value) if not isinstance(value, str) else value
            replaced = replaced.replace(f'{{{field}}}', str_value)

        filename = f'output_{index}.txt'

        with open(filename, 'w') as file:
            file.write(replaced)
