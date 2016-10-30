#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function that combines customer info and customer orders."""


def sum_orders(customers, orders):
    """A function that
    Args:
        customers (dict): A dictionary of customers keyed by customer_id.
        orders (dict): A dictionary of orders keyed by order id.
    Returns:
        dict: A dictionary keyed by customer_id with an inner dictionary showing
              customer name, email, number of orders, and total sum of orders.
    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
                      3: {'customer_id': 2, 'total': 10},
                      4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                         3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'total': 20, 'orders': 2, 'name': 'Person One', 'email': 'email@one.
        com'}, 3: {'total': 15, 'orders': 1, 'name': 'Person Two', 'email':
        'email@two.com'}}
    """
    for key in customers:
        order = 0
        total = 0
        for value in orders.itervalues():
            if value.get('customer_id') == key:
                order += 1
                total += value.get('total')
        customers[key]['orders'] = order
        customers[key]['total'] = total
    return customers
