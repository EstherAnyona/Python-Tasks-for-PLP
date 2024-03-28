def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("12345\n")
            file.write("Line 3: Some more text.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred: {e}")
    finally:
        print("File creation completed.")


def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred: {e}")


def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Additional line 1.\n")
            file.write("98765\n")
            file.write("Appending line 3.\n")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred: {e}")
    finally:
        print("Appending completed.")


def main():
    create_file()
    read_file()
    append_to_file()
    read_file()


if __name__ == "__main__":
    main()
