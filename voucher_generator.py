# ---------------------------------------------------------------
# Voucher Generator Script
# Author: CyberGhoul(cyb3rgh0u1)
# This script is property of cyb3rgh0u1. It was a test project of
# mine, so you can use or modify it.
# For those who are going to use this code as it is free:
# Please give credit to cyb3rgh0u1.
# ---------------------------------------------------------------

import random
import string

def generate_voucher(length):
    # Uppercase, lowercase, and digits
    characters = string.ascii_letters + string.digits
    # Voucher length
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    # Voucher generation limit
    limit = int(input("VOUCHER_LIMIT = "))
    length = int(input("VOUCHER_LENGTH = "))
    for _ in range(limit):
        voucher = generate_voucher(length)
        print(voucher)

if __name__ == "__main__":
    main()
