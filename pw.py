#! python3
#pw.py password manager
import pyperclip

passwords = {"email": "HgujhHFB4324235JBJKH",
             "blog": "fesnjakjnj886698kbk",
             "koffer": "12451531"}

import sys
if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()


account = sys.argv[1]       #first command ist der account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account named " + account)
