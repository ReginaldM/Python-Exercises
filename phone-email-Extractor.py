#! python3
# phone-email-Extractor.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, sys, re

def findExpression(someTuple):
    extractor = [someTuple[i][0] for i in range(len(someTuple))]    
    if extractor is not None:
        pyperclip.copy(", ".join(extractor))
    return extractor


myRegex = re.compile(r"""(
    ((\w+\.*){2,4}?@\w+\.\w+(\.\w*)?) |     # Email Expression
    (\d|\+\d{2})(\d{2}(-)?\d{3}(-)?\d{4})   # Phone number Expression
    )""", re.VERBOSE)


copiedText = pyperclip.paste()
matches = myRegex.findall(copiedText)

if len(matches) < 1:
    print("No matches were found")
    sys.exit()
else:
    findExpression(matches)
