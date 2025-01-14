def format_name(first_name, last_name):
    """
    Formats the first and last name to proper title case.
    
    Args:
    - first_name (str): The first name of the person.
    - last_name (str): The last name of the person.
    
    Returns:
    - str: The full name formatted in title case.
    """
    # Check for valid inputs
    if not first_name or not last_name:
        return "Invalid input: both first and last names are required."

    # Format names
    formatted_first = first_name.strip().title()
    formatted_last = last_name.strip().title()

    # Return the formatted name
    return f"{formatted_first} {formatted_last}"

# Example usage
formatted_name = format_name('JENIL', 'SHINGALA')
print(f"The formatted name is: {formatted_name}")
