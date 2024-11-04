import json
import random
import os
from typing import Dict


class PasswordManager:
    def __init__(self, filename: str = "passwords.json"):
        self.filename = filename
        self.passwords = self._load_passwords()

    def _load_passwords(self) -> Dict[str, str]:
        """Initialize or load the passwords file."""
        if not os.path.isfile(self.filename):
            self._save_passwords({})
        with open(self.filename, "r") as f:
            return json.load(f)

    def _save_passwords(self, data: Dict[str, str]) -> None:
        """Save passwords to file."""
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def _get_valid_input(self, prompt: str, valid_options: list) -> str:
        """Get and validate user input."""
        while True:
            user_input = input(prompt).lower()
            if user_input in valid_options:
                return user_input
            print(f"Please enter one of: {', '.join(valid_options)}")

    @staticmethod
    def generate_password(length: int = 25) -> str:
        """Generate a secure random password."""
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        return ''.join(random.choice(chars) for _ in range(length))

    def create_password(self) -> None:
        """Create a new password entry."""
        creation_type = self._get_valid_input(
            "Do you want to create a new password manually or automatically? (manual/auto)\n",
            ["manual", "auto"]
        )

        site = input(
            "Enter site for which you want password to be stored\n").lower()

        if site in self.passwords:
            print("Site already exists, no need for a new password!")
            return

        if creation_type == "manual":
            password = input("Enter password for site\n")
        else:
            password = self.generate_password()

        self.passwords[site] = password
        self._save_passwords(self.passwords)
        print(
            f"Success! Password for site {site} created. Password is: {password}")

    def get_password(self) -> None:
        """Retrieve a stored password."""
        site = input("Enter site for which you want password for\n").lower()
        password = self.passwords.get(site)

        if password:
            print(f"Password for {site} is: {password}")
        else:
            print("You do not have a password saved for this site!")

    def update_password(self) -> None:
        """Update an existing password."""
        site = input(
            "Enter site for which you want password to be updated\n").lower()

        if site not in self.passwords:
            print(f"There is no password stored for {site}")
            return

        update_type = self._get_valid_input(
            "Do you want to update password manually or automatically? (manual/auto)\n",
            ["manual", "auto"]
        )

        if update_type == "manual":
            password = input("Enter new password\n")
        else:
            password = self.generate_password()

        self.passwords[site] = password
        self._save_passwords(self.passwords)
        print(f"Success! Password for {site} updated to {password}")

    def run(self) -> None:
        """Run the password manager interface."""
        actions = {
            "create": self.create_password,
            "access": self.get_password,
            "update": self.update_password
        }

        while True:
            action = input(
                "What do you want to do? (create/access/update)\nEnter nothing to exit\n"
            ).lower()

            if action in ("", "nothing"):
                print("Quitting...")
                break

            if action in actions:
                actions[action]()
            else:
                print("Invalid input")


def main():
    password_manager = PasswordManager()
    password_manager.run()


if __name__ == "__main__":
    main()
