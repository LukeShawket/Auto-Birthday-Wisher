# Birthday Email Sender

A simple Python script to automate the process of sending personalized birthday emails. This script reads a list of birthdays from a CSV file and sends an email to the appropriate person on their birthday.

Features    
• Reads birthday data from a CSV file.

• Personalizes email content using a template text file.

• Automatically sends emails using SMTP.

Requirements    
• Python 3.x

• pandas

• smtplib

Usage    
1. Prepare your files:

• birthdays.csv: Should contain the following columns: name, email, month, day.

• wish.txt: A text file containing the email content. Use [NAME] as a placeholder for the recipient's name.

2. Configure your email credentials:

• Replace my_mail and my_password with your own email and password.

3. Run the script:

• The script will automatically send an email to anyone whose birthday is today.
