# IC-2K24-80-PythonLab-SabhyataYadav 
# Python Lab 1

## 1. Variable Practice

### Aim

To declare variables for name, age, height, and student status and print each variable along with its data type using `type()`.

### Logic

1. Declare variables for name, age, height, and student status.
2. Assign appropriate values to each variable.
3. Use the `type()` function to identify the data type of each variable.
4. Print each variable along with its data type.

### Sample Input / Output

No user input is required.

**Output:**

```text
Name: Sabhyata | Type: <class 'str'>
Age: 20 | Type: <class 'int'>
Height: 5.4 | Type: <class 'float'>
Student: True | Type: <class 'bool'>
```

---

## 2. Greeting

### Aim

To take the user's name, age, and city as input and display them in one sentence using an f-string.

### Logic

1. Take the user's name as input.
2. Take the user's age as input.
3. Take the user's city as input.
4. Use an f-string to combine all three values into one sentence.
5. Print the sentence.

### Sample Input / Output

**Input:**

```text
Enter your name: Sabhyata
Enter your age: 20
Enter your city: Mhow
```

**Output:**

```text
My name is Sabhyata, I am 20 years old, and I live in Mhow.
```

---

## 3. Arithmetic Operations

### Aim

To take two numbers as input and calculate their sum, difference, product, quotient, and remainder.

### Logic

1. Take two numbers as input from the user.
2. Calculate their sum using `+`.
3. Calculate their difference using `-`.
4. Calculate their product using `*`.
5. Calculate their quotient using `/`.
6. Calculate their remainder using `%`.
7. Print each result with a clear label.

### Sample Input / Output

**Input:**

```text
Enter the first number: 10
Enter the second number: 3
```

**Output:**

```text
Sum: 13
Difference: 7
Product: 30
Quotient: 3.3333333333333335
Remainder: 1
```

---

## 4. Celsius to Fahrenheit

### Aim

To take temperature in Celsius as input and convert it into Fahrenheit.

### Logic

1. Take the temperature in Celsius as input.
2. Convert the input into a number using `float()`.
3. Apply the formula:
   `F = (C × 9 / 5) + 32`
4. Print the Fahrenheit value.

### Sample Input / Output

**Input:**

```text
Enter temperature in Celsius: 25
```

**Output:**

```text
Temperature in Fahrenheit: 77.0
```

---

## 5. String Manipulation

### Aim

To take a full name as input and print it in uppercase, lowercase, and display its length using string operations.

### Logic

1. Take the user's full name as input.
2. Use `upper()` to convert the name into uppercase.
3. Use `lower()` to convert the name into lowercase.
4. Use `len()` to find the length of the name.
5. Use `title()` and `strip()` as additional string methods.
6. Print all the results.

### Sample Input / Output

**Input:**

```text
Enter your full name: Sabhyata Yadav
```

**Output:**

```text
Uppercase: SABHYATA YADAV
Lowercase: sabhyata yadav
Length: 14
Title Case: Sabhyata Yadav
Without Extra Spaces: Sabhyata Yadav
```

---

## 6. Escape Sequence

### Aim

To print a small receipt using `\t` and `\n` to arrange the text and prices neatly.

### Logic

1. Use `\t` to create tab spaces between item names and prices.
2. Use `\n` to move text to a new line.
3. Print the items and their prices in a receipt format.
4. Display the total amount.

### Sample Input / Output

No user input is required.

**Output:**

```text
        SHOPPING RECEIPT
-----------------------------
Item            Price
-----------------------------
Pen             ₹20
Notebook        ₹50
Pencil          ₹10
Eraser          ₹5
-----------------------------
Total           ₹85
```

---

## 7. Menu-Driven Calculator

### Aim

To build a menu-driven calculator that performs addition, subtraction, multiplication, and division and continues running until the user chooses to exit.

### Logic

1. Display a calculator menu with four arithmetic operations and an exit option.
2. Take the user's choice as input.
3. If the user selects an arithmetic operation, take two numbers as input.
4. Perform the selected operation.
5. Display the result.
6. Use a `while` loop to keep displaying the menu.
7. Stop the program when the user selects the exit option.
8. Display an error message for an invalid choice or division by zero.

### Sample Input / Output

**Input:**

```text
----- CALCULATOR MENU -----
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice: 1
Enter first number: 10
Enter second number: 5
```

**Output:**

```text
Result: 15.0
```

**Exit:**

```text
Enter your choice: 5
Calculator closed. Thank you!
```

---

## Conclusion

All the programs demonstrate basic Python concepts such as variables, data types, user input, arithmetic operations, type conversion, string methods, escape sequences, loops, conditional statements, and menu-driven programming.

