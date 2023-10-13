def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "\033[31m{}\033[0m".format("Give me name and phone please.")
        except IndexError:
            return "\033[31m{}\033[0m".format("Give me name please.")
        except KeyError:
            return "\033[31m{}\033[0m".format("Please enter a correct name.")
        except:
            return "\033[31m{}\033[0m".format("Oops, something went wrong, try again.")

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "\033[32m{}\033[0m".format("Contact added.")


@input_error
def change_username_phone(args, contacts):
    name, phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = phone
    else:
        raise KeyError
    return "\033[32m{}\033[0m".format("Contact changed.")


@input_error
def phone_username(args, contacts):
    name = args
    name[0] = name[0].lower()
    if name[0] in contacts:
        return contacts[name[0]]
    else:
        raise KeyError
    

@input_error
def all_phone_print(contacts):
    str = ""
    for keys, value in contacts.items():
        str = str + "\033[1m{}\033[0m".format(keys) + ": " + value + "\n"
    return str[:-1]  


@input_error
def main():
    contacts = {}
    print("\033[1m\033[34m{}\033[0m".format("Welcome to the assistant bot!"))
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("\033[34m{}\033[0m".format("Good bye!"))
            break
        elif command == "hello":
            print("\033[34m{}\033[0m".format("How can I help you?"))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts)) 
        elif command == "all":
            print(all_phone_print(contacts))             
        elif user_input == "" or command == "":
            print("\033[31m{}\033[0m".format("You did not enter the command, please try again."))
        else:
            print("\033[31m{}\033[0m".format("Invalid command, please try again."))


if __name__ == "__main__":
    main()

