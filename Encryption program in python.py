import random
import string


CHARACTERS = string.printable
KEY_FILE = "secret_key.txt"


def generate_key():
    characters = list(CHARACTERS)
    key = characters.copy()
    random.shuffle(key)

    return "".join(key)


def save_key(key):
    with open(KEY_FILE, "w", encoding="utf-8") as file:
        file.write(key)


def load_key():
    try:
        with open(KEY_FILE, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def create_or_load_key():
    key = load_key()

    if key is None:
        key = generate_key()
        save_key(key)
        print("New encryption key generated and saved.")
    else:
        print("Existing encryption key loaded.")

    return key


def encrypt_message(message, key):
    encrypted_text = ""

    for character in message:
        index = CHARACTERS.index(character)
        encrypted_text += key[index]

    return encrypted_text


def decrypt_message(message, key):
    decrypted_text = ""

    for character in message:
        index = key.index(character)
        decrypted_text += CHARACTERS[index]

    return decrypted_text


def display_menu():
    print("\n" + "=" * 45)
    print("        Python Encryption Program")
    print("=" * 45)
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Generate a new key")
    print("4. Exit")
    print("=" * 45)


def main():
    key = create_or_load_key()

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            message = input("\nEnter a message to encrypt: ")
            encrypted_message = encrypt_message(message, key)

            print("\nOriginal message:")
            print(message)

            print("\nEncrypted message:")
            print(encrypted_message)

        elif choice == "2":
            message = input("\nEnter a message to decrypt: ")
            decrypted_message = decrypt_message(message, key)

            print("\nEncrypted message:")
            print(message)

            print("\nDecrypted message:")
            print(decrypted_message)

        elif choice == "3":
            confirm = input(
                "\nWarning: generating a new key will make old encrypted messages unreadable. Continue? (y/n): "
            ).lower().strip()

            if confirm == "y":
                key = generate_key()
                save_key(key)
                print("New key generated and saved successfully.")
            else:
                print("Key generation cancelled.")

        elif choice == "4":
            print("\nThank you for using the Encryption Program.")
            break

        else:
            print("Invalid choice. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()



