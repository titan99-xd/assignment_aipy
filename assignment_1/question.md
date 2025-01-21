Artificial Intelligence with Python

Assignment 1

1. This exercise tests out the default values of parameters. Create a program which has
   a main function and a subfunction called tester. The main function prompts user for
   an input "Write something (quit ends): " and sends this input to the subfunction as a
   parameter.
   Define the subfunction tester so that it has one parameter called "givenstring", which
   has the default value "Too short". If the user input is less than 10 characters, the
   program uses the default value and if 10 or more, it prints the usergiven input. If the
   user inputs "quit", the program is terminated. When working correctly, the program
   will print out something like this:

   > > > Write something (quit ends): what?
   > > > Too short
   > > > Write something (quit ends): What do you mean?
   > > > What do you mean?
   > > > Write something (quit ends): Ok thats it
   > > > Ok thats it
   > > > Write something (quit ends): I am out of here
   > > > I am out of here
   > > > Write something (quit ends): quit
   > > >
   > > > The easiest way of testing the length of a string is by using the function len().
   > > > Example output:
   > > > Write something (quit ends): test
   > > > Too short
   > > > Write something (quit ends): second test
   > > > second test
   > > > Write something (quit ends): quit
   > > > The verification of program output does not account for whitespace and is not casesensitive (the least strict comparison level)

2. In the second exercise the idea is to create a small grocery shopping list with the list
   datastructure. In short, create a program that allows the user to (1) add products to the
   list, (2) remove items and (3) print the list and quit.
   If the user adds something to the list, the program asks "What will be added?: " and
   saves it as the last item in the list. If the user decides to remove something, the
   program informs the user about how many items there are on the list (There are
   [number] items in the list.") and prompts the user for the removed item ("Which item
   is deleted?: "). If the user selects 0, the first item is removed. When the user quits, the
   final list is printed for the user "The following items remain in the list:" followed by
   the remaining items one per line. If the user selects anything outside the options,
   including when deleting items, the program responds "Incorrect selection.". When the
   program works correctly it prints out the following:

   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 1
   > > > What will be added?: Apples
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 1
   > > > What will be added?: Beer
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 1
   > > > What will be added?: Carrots
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 2
   > > > There are 3 items in the list.
   > > > Which item is deleted?: 3
   > > > Incorrect selection.
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 2
   > > > There are 3 items in the list.
   > > > Which item is deleted?: 2
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 2
   > > > There are 2 items in the list.
   > > > Which item is deleted?: 0
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 4
   > > > Incorrect selection.
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 3
   > > > The following items remain in the list:
   > > > Beer
   > > >
   > > > Example output:
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 1
   > > > What will be added?: Milk
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 1
   > > > What will be added?: Beer
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 2
   > > > There are 2 items in the list.
   > > > Which item is deleted?: 1
   > > > Would you like to
   > > > (1)Add or
   > > > (2)Remove items or
   > > > (3)Quit?: 3
   > > > The following items remain in the list:
   > > > Milk
   > > > The verification of program output does not account for whitespace and is not casesensitive (the least strict comparison level)

3. Make simple Supermarket -program,
   • having 10 products with prices in a list as follows:[10,14,22,33,44,13,22,55,66,77].
   • asking product number from 1 to 10 and summing its price to totalsum and printing
   product number and price for every product as in example.
   • asking products until user gives '0' to quit the program (while-loop).
   • printing "Total:" and the total sum of prices.
   • asking "Payment:" from user and printing "Change:" and finally calculating and
   printing the amount of change (payment - totalsum) to customer.
   • You must use in this program: while, input
   Example output:
   Supermarket
   ===========
   Please select product (1-10) 0 to Quit: 3
   Product: 3 Price: 22
   Please select product (1-10) 0 to Quit: 5
   Product: 5 Price: 44
   Please select product (1-10) 0 to Quit: 7
   Product: 7 Price: 22
   Please select product (1-10) 0 to Quit: 1
   Product: 1 Price: 10
   Please select product (1-10) 0 to Quit: 6
   Product: 6 Price: 13
   Please select product (1-10) 0 to Quit: 10
   Product: 10 Price: 77
   Please select product (1-10) 0 to Quit: 0
   Total: 188
   Payment: 200
   Change: 12
   The verification of program output does not account for whitespace and is not casesensitive (the least strict comparison level)

4. In this exercise create two functions
   my_split : which splits sentence given as first argument using second argument as a
   separator character to separate list items. Function returns a list of items.
   my_join : which joins list given as first argument to a string separated with character given
   as second argument. Function returns a string.
   In this exercise you are not allowed to use Python split and join functions
   Example output:
   Please enter sentence:This is a sentence
   This,is,a,sentence
   This
   is
   a
   sentence
   The output of the program must be exactly the same as the example output (the most strict
   comparison level)
