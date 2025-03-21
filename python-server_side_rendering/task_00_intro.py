from os import path

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Invalid template type. Expected string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Invalid attendees type. Expected list of dictionaries.")
        return
    
    # Handle empty content cases
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    required_fields = ['name', 'event_title', 'event_date', 'event_location']

    try:

        for index, attendee in enumerate(attendees, start=1):
            replaced = template
            for field in required_fields:
                value = attendee.get(field)
                if value is None:
                    value = 'N/A'
                str_value = str(value)
                replaced = replaced.replace(f'{field}', str_value)

            filename = f'output_{index}.txt'
            with open(filename, 'w') as file:
                file.write(replaced)
    except Exception as e:
        print('Fatal Error')