#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Delete keys with a specific value from a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        value: The value to search for and delete in the dictionary.

    Returns:
        dict: The modified dictionary after deleting the keys.

    """
    # Create a list to store the keys to delete
    keys_to_delete = []

    # Iterate over each key in the dictionary
    for key in a_dictionary:
        # Check if the value of the current key matches the given value
        if a_dictionary[key] == value:
            # Add the key to the list of keys to delete
            keys_to_delete.append(key)

    # Delete the keys from the dictionary using the pop() method
    for key in keys_to_delete:
        a_dictionary.pop(key, None)

    return a_dictionary
