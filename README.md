# 🔐 Secure File Storage System

### Python-Based File Encryption, Decryption & Integrity Verification

A cybersecurity project developed using Python to demonstrate secure local file storage through encryption, decryption, and file integrity verification.

The application provides a simple graphical user interface (GUI) that allows users to encrypt files, decrypt previously encrypted files, and calculate SHA-256 hashes for integrity checking.

---

## 📌 Project Overview

The Secure File Storage System is designed to protect files from unauthorized access by converting readable files into encrypted data.

The application uses the Python **Cryptography** library and the Fernet authenticated encryption mechanism. It also uses SHA-256 hashing to support file integrity verification.

This project demonstrates practical concepts of cryptography, secure file handling, and Python GUI development.

## ✨ Features

- File encryption using Fernet authenticated encryption
- Secure file decryption using the correct encryption key
- Graphical user interface developed with Tkinter
- SHA-256 file integrity verification
- Local storage of encrypted files
- File selection through a graphical file dialog
- Error handling for invalid or corrupted encrypted files
- Simple and beginner-friendly interface

## 🛠️ Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Application development             |
| Tkinter      | Graphical user interface            |
| Cryptography | File encryption and decryption      |
| Fernet       | Authenticated symmetric encryption  |
| SHA-256      | File integrity checking             |
| VS Code      | Development environment             |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
Secure-File-Storage-AES/
│
├── main.py
├── README.md
├── .gitignore
├── secret.key
├── sample.txt
│
└── encrypted_files/
    ├── sample.txt.enc
    └── decrypted_sample.txt
```

**Note:** The encryption key and generated files are local project data. They should not be uploaded to a public repository.

## 💻 Installation & Setup

### Prerequisites

- Windows 10 or Windows 11
- Python 3.10 or later
- Visual Studio Code (recommended)
- Git (for GitHub upload)

### Step 1: Verify Python Installation

Open Command Prompt or the VS Code terminal.

```bash
python --version
```

If Python is not recognized, install it from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

During installation, enable **Add Python to PATH**.

### Step 2: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Secure-File-Storage-AES.git
```

Navigate to the project directory:

```bash
cd Secure-File-Storage-AES
```

### Step 3: Install Required Library

```bash
python -m pip install cryptography
```

Verify the installation:

```bash
python -c "import cryptography; print('Cryptography installed successfully')"
```

### Step 4: Generate an Encryption Key

If `secret.key` is not present, generate a new key using:

```bash
python -c "from cryptography.fernet import Fernet; open('secret.key','wb').write(Fernet.generate_key()); print('Key generated successfully')"
```

**Important:** If you already have the original key, do not generate a replacement. Files encrypted with the previous key cannot be decrypted using a new key.

### Step 5: Run the Application

```bash
python main.py
```

The Secure File Storage System GUI will open.

## 🚀 How to Use

### Encrypt a File

1. Launch the application.
2. Click **Encrypt File**.
3. Select the file you want to protect.
4. The application encrypts the file.
5. The encrypted output is saved inside the `encrypted_files` directory with the `.enc` extension.

### Decrypt a File

1. Launch the application.
2. Click **Decrypt File**.
3. Select the encrypted `.enc` file.
4. The application decrypts the file using the stored encryption key.
5. The decrypted file is saved inside the `encrypted_files` directory.

### Verify File Integrity

1. Click **Verify File Integrity**.
2. Select the file you want to check.
3. The application calculates its SHA-256 hash.
4. Compare the hash with a previously recorded hash to check whether the file content has changed.

## 🔒 Security Considerations

- Keep `secret.key` private and secure.
- Never upload encryption keys to a public GitHub repository.
- Do not share encrypted files and their encryption key with unauthorized users.
- A new encryption key cannot decrypt files encrypted using an older key.
- SHA-256 hashes can help identify changes when compared against a trusted, previously recorded hash.
- This project is intended for educational and local demonstration purposes.

## 🧪 Recommended Testing

| Test                                 | Expected Result                   |
| ------------------------------------ | --------------------------------- |
| Encrypt a text file                  | Encrypted `.enc` file is created  |
| Decrypt the encrypted file           | Original file content is restored |
| Compare original and decrypted files | Content matches                   |
| Calculate SHA-256 hash               | Hash is displayed                 |
| Select an invalid encrypted file     | Error message is displayed        |
| Use an incorrect encryption key      | Decryption fails                  |

## 📚 Learning Outcomes

Through this project, I explored:

- Fundamentals of symmetric encryption
- Authenticated file encryption using Fernet
- File handling in Python
- Cryptographic key management
- SHA-256 hashing and integrity verification
- GUI development using Tkinter
- Error handling and secure coding practices
- Git and GitHub project management

## 👨‍💻 Author

** Aritra Pal**

Cyber crime investigation and fraud analyser | Ethical Hacking Enthusiast

## ⚠️ Disclaimer

This project was developed for educational and cybersecurity learning purposes. It is intended for authorized use on personal or permitted files only.

---

⭐ If you find this project useful, feel free to explore the code and learn from it.
