import re
text = """
I am a ml engineer.You can contract with me using  email or contract number.
my email is rafiulhoque21@gmail.com and my mobile number is +88017120765433
"""



def extract_emails_and_phones(text):
   
    email_method = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_method = r'\+?(\d[\d\s-]{8,}\d)'
    email = re.findall(email_method, text)

    phone = re.findall(phone_method, text)
    
    return email, phone


email, phone = extract_emails_and_phones(text)

print("Emails:", email)
print("Phones:", phone)
