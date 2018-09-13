#!/usr/bin/env python

import argparse


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('item_count')
    parser.add_argument('price')
    parser.add_argument('state_code')
    return parser.parse_args()


def calculate_discount_rate(subtotal):
    discount_table = {
        0: 0,
        1000: 3,
        5000: 5,
        7000: 7,
        10000: 10,
        50000: 15
    }

    best_match = 0

    for dollar_amount, percent in discount_table.items():
        if subtotal < dollar_amount:
            continue

        if dollar_amount > best_match:
            best_match = dollar_amount

    return discount_table[best_match]


def main():
    args = _get_args()

    subtotal = float(int(args.item_count) * float(args.price))
    tax_rates = {
        'UT': 6.85,
        'NV': 8,
        'TX': 6.25,
        'AL': 4,
        'CA': 8.25
    }

    if args.state_code not in tax_rates:
        raise Exception('we only support these states: %s' % tax_rates.keys())

    discount_rate = calculate_discount_rate(subtotal)
    tax_modifier = 1.0 + (tax_rates[args.state_code] / 100.0)
    discount_modifier = 1.0 - (float(discount_rate) / 100.0)
    total = subtotal * discount_modifier * tax_modifier
    print '%s x %s x %s = %s' % (subtotal, discount_modifier, tax_modifier, total)


if __name__ == '__main__':
    main()
