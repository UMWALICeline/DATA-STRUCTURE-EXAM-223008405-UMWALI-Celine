example 1 explanations are following
#include <iostream>  :This includes the <iostream> library, which allows input and output operations (e.g., cin for input and cout for output).

using namespace std;  :This allows direct use of standard library objects (like cout, cin, endl) without prefixing them with std::.

int main()   :This defines the main function, which is the entry point of the C++ program.

{ Begins the body of the main function.

 int age = 20;  :Declares an integer variable age and assigns it the value 20.

double price = 19.99;  :Declares a double variable price (used for floating-point numbers) and assigns it 19.99.

char grade = 'A';  :Declares a char variable grade (used to store a single character) and assigns it 'A'.

string name = "Alice";  :Declares a string variable name (used for text) and assigns it "Alice". (Requires the string library, which is included by default.)
cout << "Name: " << name << endl;  :Outputs "Name: Alice" to the console. The << operator is used for concatenation, and endl moves to the next line.

cout << "Age: " << age << endl;  :Outputs "Age: 20" to the console.

 cout << "Price: $" << price << endl;  :Outputs "Price: $19.99" to the console.

cout << "Grade: " << grade << endl;  Outputs "Grade: A" to the console.

return 0;  :Returns 0, indicating successful execution of the program.

}  :Closes the main function.


example 2 explanations are following
#include <iostream>  :This includes the <iostream> library, which allows input and output operations (e.g., cin for input and cout for output).

using namespace std;  :This allows direct use of standard library objects (like cout, cin, endl) without prefixing them with std::.

int main()   :This defines the main function, which is the entry point of the C++ program.

{  : Begins the body of the main function.

string name;  :Declares a string variable name to store the user's name.
int age;  :Declares an int variable age to store the user's age.

cout << "Enter your name: ";  :Prints "Enter your name: " to the console and The user is expected to enter their name.

cin >> name;  ;Takes user input and stores it in the name variable and cin reads input until the first space. If the user enters "John Doe", only "John" will be stored.Prompting the User for Age

cout << "Enter your age: ";  :Prints "Enter your age: " to the console.

cin >> age;  :Takes user input and stores it in the age variable,Since age is an int, the user must enter a number.Displaying the Output

cout << "Hello, " << name << "! You are " << age << " years old." << endl;  :Prints a greeting message using the user's input.Example output if the user entered "Alice" and 25:

return 0;  :Returns 0, indicating successful execution of the program.

}  :Closes the main function.


example 3 explanations are following
#include <iostream>  :This includes the <iostream> library, which allows input and output operations (e.g., cin for input and cout for output).
using namespace std;  :This allows direct use of standard library objects (like cout, cin, endl) without prefixing them with std::.

int main()   :This defines the main function, which is the entry point of the C++ program.

{  : Begins the body of the main function.

int a = 10, b = 3;  :Declares two integer (int) variables,a is assigned the value 10 and b is assigned the value 3.

cout << "Sum: " << a + b << endl;  :Computes the sum: 10 + 3 = 13

cout << "Difference: " << a - b << endl;   :Computes the difference: 10 - 3 = 7

cout << "Product: " << a * b << endl;  :Computes the product: 10 * 3 = 30

cout << "Quotient: " << a / b << endl;  :Performs integer division: 10 / 3 and Since a and b are both int, the decimal part is discarded.10 / 3 = 3.333, but only 3 is kept.

cout << "Remainder: " << a % b << endl;  :Computes the remainder when 10 is divided by 3. and 10 % 3 = 1 (since 3 * 3 = 9, remainder 1).

return 0;  :Returns 0, indicating successful execution of the program.

}  :Closes the main function.

example 4 explanations are following
#include <iostream>  :This includes the <iostream> library, which allows input and output operations (e.g., cin for input and cout for output).

using namespace std;  :This allows direct use of standard library objects (like cout, cin, endl) without prefixing them with std::.

int main()   :This defines the main function, which is the entry point of the C++ program.

{  : Begins the body of the main function.

int age = 30;  :Declares an integer variable age and assigns it the value 30. ,int is used to store whole numbers.

float pi = 3.14;  :Declares a floating-point variable pi and assigns it 3.14 and float is used for decimal numbers with less precision (typically up to 6-7 digits).

double num = 3.1415926535;  ;Declares a double-precision floating-point variable num and assigns it 3.1415926535 and double has higher precision than float (typically up to 15-16 digits).

char letter = 'A';  :Declares a character variable letter and assigns it 'A' and char is used to store a single character (always enclosed in single quotes ' ').

bool isHappy = true;  :Declares a boolean variable isHappy and assigns it true and bool can store only true (1) or false (0).
string name = "Alice";  :Declares a string variable name and assigns it "Alice" andstring is used to store text (always enclosed in double quotes " ").
Printing Values to the Console

cout << "age: " << age << endl;  :Prints: age: 30 and << is the insertion operator, used to display output and also endl moves the cursor to a new line.

cout << "pi: " << pi << endl;  :Prints: pi: 3.14

cout << "num: " << num << endl;  :Prints: num: 3.1415926535 (shows more decimal places than float).

cout << "letter: " << letter << endl;  :Prints: letter: A

cout << "isHappy: " << isHappy << endl;  :Prints: isHappy: 1 and In C++, true is displayed as 1, and false is displayed as 0.

cout << "name: " << name << endl;  :Prints: name: Alice

return 0;  ;Indicates successful execution of the program and return 0; is a convention in main() to tell the system that the program ran without errors.

}  :Closes the main function.

