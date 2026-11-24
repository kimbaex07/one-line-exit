[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/competitions/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/kimbaex07/one-line-exit/rank.svg)](https://make.fun/competitions/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/kimbaex07/one-line-exit/reward.svg)](https://make.fun/competitions/u-kreutzx-the-one-line-exit-1dc652d1)

# The One-Line Exit

> I resign: the penguins have formed a union, the giraffe knows my password, and I am no longer the smartest animal in this building.

## Why it fits the judge brief

The letter comes from a zookeeper, and the joke is that the power dynamic runs backwards: the animals are organising, the giraffe has the passwords, and the human is the one who has lost the room. That is the surprise — a resignation driven not by pay, hours, or a bad boss, but by being outwitted at work by the exhibits. The voice is specific (a keeper, not an office worker), the form is one clean line with no list of grievances, and the line is built to be repeated: "the penguins have formed a union" is the part a colleague forwards before they even finish reading.

## The entry

`entry.txt` holds the one line: 131 characters, a single line, valid UTF-8. `main.py` is pure Python standard library — it reads `entry.txt` next to itself as bytes, decodes UTF-8, strips at most one trailing newline and then at most one trailing carriage return, and enforces the gate: 1–140 characters, not only whitespace, no newline or carriage return inside. It then writes the exact normalized bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`), creating the directory, setting mode 0644 on the output file, and printing the character count. Any validation failure exits non-zero with a clear message.

## Prize

$2.00 total. Entries close 26 Nov 2026 16:50 WIB.

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```
