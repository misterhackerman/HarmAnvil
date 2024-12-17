#!/usr/bin/env python
import sys
import re
import string

ALRT = 0
if not sys.stdin.isatty():
    input_string = sys.stdin.read()
elif len(sys.argv) == 2:
    input_string = sys.argv[1]
else:
    print("\033[32m:: Usage: harptoy <string>\033[0m")
    exit(1)
# here you can change the table to fit your toy.
table = { "4"     :	"1",
"(4)"	:	"(2)",
"5"     :	"3",
"(5)"	:	"(4)",
"6"     :	"5",
"(6)"	:	"(6)",
"7"     :	"(8)",
"(7)"	:	"7",
"8"     :	"!(10)",
"(8)"   :	"9"}

notes = re.split(r'(\s)', input_string)

for note in notes:
    if note == ' ':
        print(' ', end='')
        continue
    if note in string.ascii_lowercase:
        print(note, end='')
        continue
    if note == "\n":
        print()
        continue
    if note == "\t":
        print("\t", end='')
        continue
    if note == "":
        continue
    if '-' in note:
        note = "(" + note.strip("-") + ")"
    if "+" in note:
        note = note.strip("+")
    if note not in table:
        print(f"\033[1;31m{note}\033[0m", end='')
        ALRT = 1
        continue

    print(table[note], end=' ')
print()
if ALRT:
    print("In red shown the original notes, cause your fucking toy can't play the note")

