#!/usr/bin/env python3

import random
import string
import sys
import os
import shutil


def generate_voucher(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))


def display_help():
    help_text = """
    Voucher Generator Script

    Usage:
      voucher [OPTIONS]

    Options:
      --help          Show this message and exit.
      -lim <int>      Number of vouchers to generate.
      -len <int>      Length of each voucher.
      -c              Use uppercase letters.
      -s              Use lowercase letters.
      -n              Use digits.
      --install       Install this script to /usr/local/bin.(The installation process requires superuser (sudo) permissions.)
      --uninstall     Uninstall this script.(The uninstallation process requires superuser (sudo) permissions.)

    Example:
      voucher -lim 10 -len 16 -c -s -n
    """
    print(help_text)


def install_script():
    script_path = os.path.realpath(__file__)
    target_path = "/usr/local/bin/voucher"
    if not os.path.exists(target_path):
        shutil.copy(script_path, target_path)
        os.chmod(target_path, 0o777)
        print("Script installed successfully. You can now run 'voucher' from anywhere.")
    else:
        print("Script is already installed.")


def uninstall_script():
    os.path.realpath(__file__)
    target_path = "/usr/local/bin/voucher"
    if os.path.exists(target_path):
        os.remove(target_path)
        print("Script uninstalled successfully.")
    else:
        print("Script isn't available")


def main():
    if '--help' in sys.argv:
        display_help()
        return

    if '--install' in sys.argv:
        install_script()
        return

    if '--uninstall' in sys.argv:
        uninstall_script()
        return

    try:
        limit_index = sys.argv.index('-lim') + 1
        length_index = sys.argv.index('-len') + 1

        limit = int(sys.argv[limit_index])
        length = int(sys.argv[length_index])

        characters = ''
        if '-c' in sys.argv:
            characters += string.ascii_uppercase
        if '-s' in sys.argv:
            characters += string.ascii_lowercase
        if '-n' in sys.argv:
            characters += string.digits

        if not characters:
            characters = string.ascii_letters + string.digits

    except (ValueError, IndexError):
        print("Invalid arguments. Use --help for usage details.")
        return

    for _ in range(limit):
        voucher = generate_voucher(length, characters)
        print(voucher)


if __name__ == "__main__":
    main()
