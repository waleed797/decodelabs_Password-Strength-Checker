# Password Strength Checker

**DecodeLabs Cyber Security Internship — Project 1**

A Python program that checks whether a password is **Weak**, **Medium**, or **Strong** based on its length and character variety.

## Goal

Build a program that evaluates password security using basic string handling and conditional logic — no external libraries required.

## Key Requirements

- Check password length
- Check use of numbers, symbols, and uppercase letters
- Display the password strength result

## Key Skills Used

- String handling
- Condition checks
- Security basics

## How It Works

The password is checked against 4 criteria:

1. **Length** — must be at least 6 characters to avoid being automatically Weak
2. **Uppercase letter** — at least one A–Z character
3. **Number** — at least one digit
4. **Symbol** — at least one punctuation character

Based on how many of these are met, the password is classified as:

| Condition | Result |
|---|---|
| Length < 6 | Weak |
| Length ≥ 6, fewer than 2 criteria met | Weak |
| Length ≥ 6, exactly 2 criteria met | Medium |
| Length ≥ 8, all 3 criteria met | Strong |

## How to Run

```bash
python password_strength_checker.py
```

You'll be prompted to enter a password, and the program will display a breakdown of the checks along with the final strength result.

## Example

```
=== Password Strength Checker ===
Enter your password: MyPass1!

--- Result ---
Length: 8 characters
Contains uppercase letter: Yes
Contains number: Yes
Contains symbol: Yes

Password Strength: Strong
```

## Requirements

- Python 3.x (uses only the built-in `string` module — no installation needed)
