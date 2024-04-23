class Email():
    inbox = []

    def mark_as_read (self,):
        if self.has_been_read == False:
            return self.has_been_read == True + self.subject_line, "Is now marked Read"
        else:
            self.has_been_read == True
            return self.subject_line + " Has already been marked as Read"

    def __init__(self,email_address,subject_line,email_content) :
        self.email_adress = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False


def populate_inbox():
        
        welcomes_to_hyperdevion = Email("Hyperiondev@gmail.com", "welcomes_to_hyperdevion","Welcome to Hyperiondev! Dive into our tech community for top-notch courses, expert mentors, and endless opportunities to thrive. ")
        great_work_on_the_bootcamp = Email("John.Cenna@hotmail.com", "Great Work on the BootCamp", " Fantastic job completing the Python bootcamp! Your dedication and progress are truly impressive. ")
        your_excellent_marks = Email("Mistypokemon@msn.com ","Your excellent marks !", " Impressive marks! Don't forget to add your signature to make it official.")

        
        Email.inbox.extend(welcomes_to_hyperdevion,great_work_on_the_bootcamp,your_excellent_marks)
        
        
def list_Emails():
    print("inbox")
    for index, email in enumerate(Email.inbox):
        if not email .has_ben_read:
             print(f"{index} {email.subject_line} [Unread]")
        else:
             print(f"{index} {email.subject_line}")


def read_emails():
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_reademail = Email.inbox[index]:
        print(f"From: {email.email_address}")
    
        print("Email marked as read.")
    
    else:
        print("Invalid index. Please enter a valid index.")


populate_inbox()

while True:
    print("\nMenu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    choice = input("Enter your choice: ")


if user_choice == 1:
    list_emails()
    index = int(input("Enter the index of the email you want to read: "))
    read_emails()
    elif choice == "2":
        list_emails()
    elif choice == "3":
        print("Quitting application. Goodbye!")









