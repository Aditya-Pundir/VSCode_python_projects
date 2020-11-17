letter = '''
Dear <|Name|>,
    Greetings from google.
    We are happy to tell you about your selection
    as our L8 software engineer at the USA.
    Regards,
    Google

Date: <|Date|>
'''
Name = input("Enter your name here:\n")
Date = input("Enter today's date here:\n")
letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)
print(letter)