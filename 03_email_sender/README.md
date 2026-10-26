# Email Sender with Python

## Description

A simple email automation project built with Python and Gmail SMTP.

This is the third project in my **Automation Systems & Bots** group. It reads recipient details from a CSV file and uses an HTML template to prepare personalized emails.

---

## What this project does

- Reads recipient details from a CSV file
- Personalizes emails with names and study topics
- Uses an HTML email template
- Sends emails through Gmail SMTP
- Loads email credentials from a `.env` file
- Asks for confirmation before sending
- Shows successful and failed email counts

---

## Modules Used

- `csv` – Reads recipient data
- `pathlib` – Handles file paths
- `smtplib` – Sends emails through SMTP
- `email` – Creates email messages
- `python-dotenv` – Loads credentials from `.env`

---

## Project Structure

```text
03_email_sender/
├── main.py
├── config.py
├── sender.py
├── data.csv
├── index.html
├── .env
├── requirements.txt
└── README.md
```

---

## How to Run

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Add your Gmail details to a `.env` file:

   ```env
   EMAIL=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

3. Add recipient details to `data.csv`.

4. Run the program:

   ```bash
   python main.py
   ```

5. Type `SEND` to confirm email sending.

**Note:** Use a Gmail App Password and never upload your `.env` file to GitHub. Test with email addresses you control.
