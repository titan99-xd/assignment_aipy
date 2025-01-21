def main():
    grocery_list = []

    while True:
        print("Would you like to")
        print("(1) Add or")
        print("(2) Remove items or")
        print("(3) Quit?: ", end="")

        choice = input()

        if choice == '1':
            item = input("What will be added?: ")
            grocery_list.append(item)

        elif choice == '2':
            if len(grocery_list) == 0:
                print("The list is empty, nothing to remove.")
            else:
                print(f"There are {len(grocery_list)} items in the list.")
                item_to_remove = input("Which item is deleted?: ")

                if item_to_remove == '0' and len(grocery_list) > 0:
                    removed_item = grocery_list.pop(0)
                    print(f"Removed {removed_item}.")
                elif item_to_remove in grocery_list:
                    grocery_list.remove(item_to_remove)
                    print(f"Removed {item_to_remove}.")
                else:
                    print("Incorrect selection.")

        elif choice == '3':
            # Quit and print the remaining items in the list
            print("The following items remain in the list:")
            for item in grocery_list:
                print(item)
            break

        else:
            # If an invalid option is selected
            print("Incorrect selection.")


if __name__ == "__main__":
    main()
