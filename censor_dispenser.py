# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

word = "learning algorithms"


def censor(word, text):
    placeholder = "-" * len(word)
    if word in text:
        censored_text = text.replace(word, placeholder)
    return censored_text


print(censor(word, email_one))
