#!/bin/bash
# Termux setup for SMS Bomber

echo -e "\033[1;32mInstalling dependencies...\033[0m"
pkg update -y
pkg install python -y
pip install requests

echo -e "\033[1;32mSetup complete. Run with: python bomber.py\033[0m"
