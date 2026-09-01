# Unit Converter

A beginner-friendly Python command-line application that allows users to convert between several common units of length, weight, and speed.

## Features

* Convert centimeters to inches
* Convert inches to centimeters
* Convert kilograms to pounds
* Convert pounds to kilograms
* Convert kilometers per hour to miles per hour
* Convert miles per hour to kilometers per hour
* Interactive command-line menu
* Input validation using `try` and `except`
* Results rounded to two decimal places

## Available Conversions

| Option | Conversion                           |
| ------ | ------------------------------------ |
| 1      | Centimeters → Inches                 |
| 2      | Inches → Centimeters                 |
| 3      | Kilograms → Pounds                   |
| 4      | Pounds → Kilograms                   |
| 5      | Kilometers per Hour → Miles per Hour |
| 6      | Miles per Hour → Kilometers per Hour |
| 7      | Exit                                 |

## How It Works

The application uses individual Python functions for each unit conversion. The user selects a conversion from the menu and enters the value they want to convert.

The program then:

1. Displays the conversion menu.
2. Prompts the user to select a conversion.
3. Asks the user to enter a numerical value.
4. Passes the value to the appropriate conversion function.
5. Calculates and displays the converted value.
6. Returns the user to the conversion menu until they choose to exit.

## Technologies Used

* Python 3
* Functions
* `while` loops
* Conditional statements
* `try` / `except` error handling
* User input and validation
* Mathematical calculations

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program with:

```bash
python converter.py
```

## Project Status

Version 1.0 — Complete

This project was created as a beginner Python project to practice using functions, loops, conditional statements, user input, and error handling.

## Future Improvements

Potential improvements for future versions include:

* Add temperature conversions (Celsius, Fahrenheit, and Kelvin)
* Add additional length and weight conversions
* Add a conversion history
* Allow users to perform multiple conversions without returning to the main menu
* Improve result formatting
