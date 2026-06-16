import time
from config import EMAIL_ADDRESS

split_email = EMAIL_ADDRESS.split("@")

def _email(index: int) -> str:
    return f"{split_email[0]}+{int(time.time())}_{index}@{split_email[1]}"

def _phone_number(index: int) -> int:
    return (int(time.time())+index)

VALID_DATA= [
    {
        "firstName": "Random",
        "lastName": "Person",
        "email":  _email(0),
        "phoneNumber": _phone_number(0),
        "password": "Testtest7*",
        "confirmPassword": "Testtest7*",
        "agency_name": "Random Agency",
        "role_in_agency": "Manager",
        "agency_email": "agencymail@gmail.com",
        "agency_website": "www.agency.com",
        "agency_address": "Kathmandu, Nepal",
        "number_of_students_recruited_annually": "50",
        "focus_area": "Engineering",
        "success_metrics": "80",
        "business_registration_number": "123456",
    }  
]

INVALID_PERSONAL_DATA = [
    {
        "firstName": "",
        "lastName": "Person", 
        "email": _email(1),
        "phoneNumber": _phone_number(1),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    }, 
    {
        "firstName": "Sit labore id voluptate non labore tempor ad occaecat consectetur pariatur. Do est cillum proident enim ut amet non laborum laborum et nostrud Lorem. Sunt esse irure magna dolore cillum adipisicing. Consectetur aliqua laborum quis cupidatat adipisicing cupidatat cupidatat laboris occaecat dolore. Eiusmod non do cupidatat enim et sunt velit mollit fugiat deserunt enim consectetur Lorem incididunt. Dolor aute et excepteur reprehenderit consequat. Sunt magna aute consequat sunt do irure veniam minim magna quis et ut enim. Fugiat proident laborum amet nulla minim sit aliquip veniam velit consequat enim nostrud eu enim. Nulla nostrud laborum excepteur consectetur Lorem laboris magna veniam cupidatat laborum excepteur. Tempor duis deserunt magna labore enim irure nostrud adipisicing incididunt est tempor. Minim incididunt officia mollit est nostrud magna eiusmod nisi laboris proident consequat. Fugiat ex aliqua fugiat in excepteur ullamco dolore esse est minim.",
        "lastName": "Person", 
        "email": _email(2),
        "phoneNumber": _phone_number(2),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "f",
        "lastName": "Person", 
        "email": _email(3),
        "phoneNumber": _phone_number(3),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": 518584,
        "lastName": "Person", 
        "email": _email(4),
        "phoneNumber": _phone_number(4),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "", 
        "email": _email(5),
        "phoneNumber": _phone_number(5),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Eu et dolore ut deserunt ut velit anim sit labore excepteur. Laborum reprehenderit amet Lorem ea eu adipisicing sunt et id consequat duis. Ut mollit ullamco labore voluptate nisi ea labore do excepteur aute. Excepteur ullamco sunt pariatur commodo sunt deserunt aliquip. Nulla commodo sunt mollit do anim laboris labore et deserunt. Consequat sint laboris eu do.Ipsum consectetur do consectetur laboris minim enim duis ullamco adipisicing ut duis dolor cillum. Nostrud in dolor consequat aliquip pariatur officia ad ullamco aliqua ipsum. Magna duis nisi consectetur ut non laborum nulla dolor. Lorem ea labore duis laborum culpa sint ea esse. Laboris dolore amet non duis est ut. Irure deserunt anim aliquip esse officia eu ullamco consequat proident eiusmod consequat. Sint Lorem ex qui veniam Lorem qui dolore minim tempor enim ut officia.", 
        "email": _email(6),
        "phoneNumber": _phone_number(6),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "f", 
        "email": _email(7),
        "phoneNumber": _phone_number(7),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": 841256, 
        "email": _email(8),
        "phoneNumber": _phone_number(8),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email":"",
        "phoneNumber": _phone_number(9),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email":"jptrandom120",
        "phoneNumber": _phone_number(10),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email":"fhdjf@",
        "phoneNumber": _phone_number(11),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email":"fdkafkd@fdjk",
        "phoneNumber": _phone_number(12),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email":"fdjafk@fjda.",
        "phoneNumber": _phone_number(13),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(9),
        "phoneNumber": "",
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(10),
        "phoneNumber": "fjdkadfjka",
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(11),
        "phoneNumber": 12,
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(12),
        "phoneNumber": 1549515615451561541023056489787892300548787845,
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(13),
        "phoneNumber": _phone_number(14),
        "password":"Testtest7*",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(14),
        "phoneNumber": _phone_number(15),
        "password":"Jpt",
        "confirmPassword":"Jpt"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(15),
        "phoneNumber": _phone_number(16),
        "password":"testtest7*",
        "confirmPassword":"testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(16),
        "phoneNumber": _phone_number(17),
        "password":"Testtest7",
        "confirmPassword":"Testtest7"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(17),
        "phoneNumber": _phone_number(18),
        "password":"Testtest*",
        "confirmPassword":"Testtest*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(18),
        "phoneNumber": _phone_number(19),
        "password":"",
        "confirmPassword":"Testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(19),
        "phoneNumber": _phone_number(20),
        "password":"Testtest7*",
        "confirmPassword":""
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(20),
        "phoneNumber": _phone_number(21),
        "password":"Testtest7*",
        "confirmPassword":"testtest7*"
    },
    {
        "firstName": "Random",
        "lastName": "Person", 
        "email": _email(21),
        "phoneNumber": _phone_number(22),
        "password":"Testtest7*",
        "confirmPassword":"Another7*"
    }
]