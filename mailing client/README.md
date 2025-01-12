# Mailing Client

This project demonstrates how to send emails using Python's `smtplib` and `email` modules. It is configured to work with Mailgun's SMTP service, utilizing a sandbox domain for testing purposes.

## Folder Structure

```
mailing client
├── encrypt_password.py  # Script for encrypting sensitive data
├── main.py              # Main script for sending emails
├── message.txt          # Email body content
├── pic.jpg              # Attachment file
```

## Prerequisites

1. **Python**: Ensure Python 3.x is installed on your system.
2. **Mailgun Account**: A Mailgun sandbox account with SMTP credentials.
3. **Dependencies**: The `smtplib` and `email` modules (both are built-in with Python).

## Setup

### 1. Configure Mailgun Sandbox

- Sign up for a [Mailgun account](https://www.mailgun.com/).
- Activate your account and use the provided sandbox domain.
- Authorize your recipient email address in the Mailgun dashboard.

### 2. Add Email Content

- Update `message.txt` with the email body content.
- Ensure `pic.jpg` is the file you want to attach to the email.

### 3. Verify SMTP Credentials

- Replace the credentials in `main.py`:
  ```python
  server.login('postmaster@sandbox12345.mailgun.org', 'your-mailgun-api-key')
  ```
  - Replace `postmaster@sandbox12345.mailgun.org` with your sandbox domain.
  - Replace `your-mailgun-api-key` with the API key from your Mailgun account.

## Usage

1. Navigate to the project directory:
   ```bash
   cd "E:\Vscode\Network_Programming_with_PY_eg_port_scanner-mailing_client\mailing client"
   ```

2. Run the `main.py` script:
   ```bash
   python main.py
   ```

3. The email will be sent to the authorized recipient with the specified subject, body, and attachment.

## Scripts Description

### `encrypt_password.py`

- Generates a key and encrypts a password.
- Saves the key to `secret.key` and the encrypted password to `encrypted_password.bin`.

### `main.py`

- Sends an email using Mailgun's SMTP service.
- Attaches a plain-text message (`message.txt`) and a binary file (`pic.jpg`).

## Notes

- Ensure your Mailgun account is activated before testing.
- Use the sandbox domain for testing and authorize recipient emails as needed.
- For production use, consider upgrading to a custom domain in Mailgun.

## Troubleshooting

### Common Errors

1. **FileNotFoundError**: Ensure `message.txt` and `pic.jpg` exist in the specified paths.
2. **SMTPDataError (421)**: Ensure your Mailgun account is activated and your domain is correctly configured.
3. **Authentication Errors**: Double-check your Mailgun credentials.

### Debugging Tips

- Enable SMTP debug mode by adding:
  ```python
  server.set_debuglevel(1)
  ```
- Verify your current working directory using:
  ```python
  import os
  print(os.getcwd())
  ```

## License

This project is for educational purposes and does not include a license.
