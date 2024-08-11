# Voucher Generator Script

## Author
CyberGhoul (cyb3rgh0u1)

## Description
This script generates unique vouchers with a specified limit on the number of vouchers that can be generated. It was initially a test project, and it is free to use and modify. If you use this code, please give credit to the author, cyb3rgh0u1.

## Features
- Generates unique vouchers consisting of uppercase letters, lowercase letters, and digits.
- Allows the user to specify the voucher length and the number of vouchers to be generated.
- Provides options to include uppercase letters, lowercase letters, and digits in the vouchers.
- Includes installation and uninstallation options for easy access.

### Initial Run
To use the script without installing, run:
```bash
python3 voucher_generator.py
```
## Usage
```bash
voucher [OPTIONS]
```
## Options
`--help`    Show the help message and exit.

`-lim`   <int> Specify the number of vouchers to generate.

`-len`  <int> Specify the length of each voucher.

`-c`        Include uppercase letters in the vouchers.

`-s`        Include lowercase letters in the vouchers.

`-n`        Include digits in the vouchers.

`--install` Install this script to /usr/local/bin.

`--uninstall` Uninstall this script.

## Example
To generate 10 vouchers, each 16 characters long, with uppercase letters, lowercase letters, and digits:

```bash
voucher -lim 10 --len 16 -c - s -n
```

## Sample Output

```
f5G7h8K3JmN0
d2L5k0N8yQ9
j9P4m7Q1zXr
........
```
