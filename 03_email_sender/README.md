
# Email Sender with Python

## Description

A simple email automation application built with Python and Gmail's SMTP server.

This is the third project in the **Automation Systems & Bots** group. The main goal is to understand how a Python application can read recipient data from a CSV file, create personalized emails, and send them using SMTP.

The project introduces email protocols, HTML email templates, configuration management, environment variables, and error handling.

---

## What this project does

* Reads recipient information from a CSV file
* Personalizes emails using recipient names and study topics
* Loads an external HTML email template
* Sends emails using Gmail SMTP
* Supports both plain-text and HTML email content
* Keeps credentials outside the source code
* Requests confirmation before sending
* Reports successful and failed email attempts

---

## How It Works

The basic workflow is:

```text
Recipient Data (CSV)
        ↓
     main.py
        ↓
Read HTML Template
        ↓
Prepare Personalized Email
        ↓
    sender.py
        ↓
Gmail SMTP Server
        ↓
Recipient's Inbox
```

For example, a CSV row containing a name and a Python learning topic is used to create an email personalized for that recipient.

The application asks for confirmation before it starts sending emails.

---

## Concepts Learned

### Python

* Functions
* Modules and imports
* Dictionaries
* CSV processing
* File handling
* `pathlib`
* String templates
* Exception handling

### Email Development

* SMTP basics
* Gmail SMTP configuration
* Email authentication
* Sending email messages
* Email headers
* Plain-text email
* HTML email
* MIME multipart messages

### Configuration

* Environment variables
* `.env` files
* `python-dotenv`
* Keeping credentials outside source code

### HTML

* Basic HTML document structure
* HTML email layout
* Inline CSS
* Template placeholders

---

## Project Structure

```text
03_email_sender/
│
├── main.py
├── config.py
├── sender.py
├── data.csv
├── index.html
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

### File Responsibilities

**`main.py`**

Loads recipient data, reads the HTML template, requests confirmation, coordinates email sending, and displays the final summary.

**`config.py`**

Loads and validates Gmail credentials and defines the SMTP connection settings.

**`sender.py`**

Creates personalized email messages and sends them through Gmail's SMTP server.

**`data.csv`**

Stores recipient email addresses, names, study topics, and resource URLs.

**`index.html`**

Contains the HTML structure and styling used in each email.

**`.env`**

Stores the email account and application password.

**`.env.example`**

Documents the required environment variable names without storing real credentials.

---

## Configuration

Create a `.env` file in the project directory:

```dotenv
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

This project uses a Gmail App Password for SMTP authentication.

An App Password is different from your normal Google account password and requires 2-Step Verification. OAuth 2.0 is a possible future improvement.

Never upload `.env` or share your credentials publicly.

---

## Dependencies

The only external dependency is:

```text
python-dotenv
```

Install it using:

```bash
python -m pip install -r requirements.txt
```

The remaining modules are included in Python's standard library.

---

## Running the Project

1. Install the requirements.
2. Configure your Gmail credentials in `.env`.
3. Add recipient data to `data.csv`.
4. Customize the email design in `index.html`.
5. Run the application:

```bash
python main.py
```

6. Review the recipient count and type `SEND` to confirm.

Use real test email addresses you control. The example addresses in the supplied CSV are placeholders.

---

## Testing

### Tests to Perform

* Load recipient data from the CSV file
* Check that required CSV columns exist
* Handle an empty recipient list
* Cancel sending when confirmation is not provided
* Send a personalized plain-text and HTML email
* Handle a row with missing information
* Handle SMTP authentication or connection failures
* Verify the final success and failure counts

### Example

```text
Recipients loaded: 1
Email sending has not started yet.
Type SEND to send these emails: SEND

Sent: your_test_email@example.com

--- Sending Summary ---
Successful: 1
Failed: 0
Total: 1
```

This is an illustrative example of successful output, not a claim that the project has been tested with a real Gmail account.

---

## Important Security Notes

* Never commit `.env` to GitHub.
* Use an App Password rather than your normal Gmail password.
* Test with a small number of recipients first.
* Review recipient addresses and resource URLs before sending.
* Avoid sending unsolicited messages or large volumes of email.
* Gmail may reject authentication attempts or enforce sending limits.

---

## Learning Outcome

The purpose of this project is to understand how a Python application can prepare and send personalized email messages.

Through this project, I aim to learn how to:

* Process structured CSV data
* Separate application logic across modules
* Use external HTML templates
* Communicate with an SMTP server
* Configure credentials safely
* Handle email sending errors
* Build a simple automation workflow

This project is a step toward designing maintainable Python automation systems.

---

## Future Improvements

Possible improvements for later projects:

* Add OAuth 2.0 authentication
* Add automated tests
* Support reusable email templates
* Generate a CSV report of email results
* Add configurable email subjects
* Add attachment support
* Improve validation and logging
