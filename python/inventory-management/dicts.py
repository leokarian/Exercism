"""Functions to keep track and alter inventory."""


def create_inventory(items: list) -> dict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    dic_items = {}
    for item in items:
        if dic_items.get(item, False):
            dic_items[item] += 1
        else: 
            dic_items[item] = 1
    return dic_items


def add_items(inventory: dict, items: list) -> dict:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        if inventory.get(item, False):
            inventory[item] += 1
        else: 
            inventory[item] = 1
    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if inventory[item] != 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, False)
    return inventory


def list_inventory(inventory: dict) -> list:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    lista = []
    for key, value in inventory.items():
        if value != 0: lista.append((key, value))
    return lista