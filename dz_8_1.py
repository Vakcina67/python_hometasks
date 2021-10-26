import re

def email_parse(email):
    result_parse = re.findall(r'([\w*\.]+)@([\w*]+\.[\w*\.]+)', email)
    if result_parse:
        return {'username': result_parse[0][0], 'domain': result_parse[0][1]}
    raise ValueError(f'wrong email: {email}')

print(email_parse('evgechernykh@gmail.com'))
print(email_parse('Ivan.Ivanov123@mail.ru'))
print(email_parse('Sergey_Sidorov@corp.mail111.ru'))
print(email_parse('66466@mail'))