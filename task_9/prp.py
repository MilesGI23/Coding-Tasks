class Email:
    inbox = []
    
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    
    def mark_as_read(self):
        self.has_been_read = True

def populate_inbox():
    # Populate inbox with sample email objects
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Thank you for joining.")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "Keep up the good work!")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Congratulations on your achievements!")
    
    Email.inbox.extend([email1, email2, email3])

def list_emails():
    print("Inbox:")
    for index, email in enumerate(Email.inbox):
        if not email.has_been_read:
            print(f"{index} {email.subject_line} [Unread]")
        else:
            print(f"{index} {email.subject_line}")

def read_email(index):
    if 0 <= index < len(Email.inbox):
        email = Email.inbox[index]
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
        print("Email marked as read.")
    else:
        print("Invalid index. Please enter a valid index.")

# Main program
populate_inbox()

while True:
    print("\nMenu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    choice = input("Enter your choice: ")

    if choice == "1":
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
    elif choice == "2":
        list_emails()
    elif choice == "3":
        print("Quitting application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
