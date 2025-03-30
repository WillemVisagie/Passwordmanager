# Password Manager

A simple, secure password manager with both CLI and web interfaces. This application allows you to store and manage passwords locally with features for generating secure random passwords.

## Features

- Web-based interface with modern, responsive design
- Command-line interface for terminal users
- Secure password generation
- Password storage in local JSON file
- Copy passwords to clipboard
- Show/hide password visibility
- Flash notifications for user feedback
- Generate new passwords for existing entries

## Prerequisites

- Python 3.6+
- Flask web framework
- Modern web browser

## Installation

1. Clone the repository:

```bash
git clone https://github.com/WillemVisagie/Passwordmanager.git
cd Passwordmanager
```

2. Install required packages:

```bash
pip install flask
```

## Usage

### Web Interface

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

The web interface provides the following features:

- Add new passwords (manual or generated)
- View stored passwords
- Copy passwords to clipboard
- Show/hide password visibility
- Generate new passwords for existing entries

### Command Line Interface

Run the password manager in CLI mode:

```bash
python password_manager.py
```

Available commands:

- `create`: Add a new password entry
- `access`: Retrieve a stored password
- `update`: Update an existing password
- Press Enter without input to exit

## File Structure

```
password-manager/
├── app.py              # Flask web application
├── password_manager.py # Core password management logic
└── templates/
    └── index.html     # Web interface template
```

## Security Notes

- Passwords are stored locally in a JSON file
- The application uses Python's `secrets` module for secure token generation
- Password visibility is controlled client-side
- No external password storage or transmission
- Consider encrypting the passwords.json file for additional security
- The web interface runs on localhost by default

## Technical Details

### Password Generation

- Default password length: 25 characters
- Character set includes:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!#$%&'()\*+,-./:;<=>?@[\]^\_`{|}~)

### Storage

- Passwords are stored in a JSON file (`passwords.json`)
- File format:

```json
{
  "site1": "password1",
  "site2": "password2"
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Improvements

- Password encryption at rest
- Password strength checker
- Export/import functionality
- Password categories/tags
- Search functionality
- Browser extension integration
- Multi-user support
- Password sharing capabilities
