print('Hello! Welcome to Our Blood Sugar Monitor')
user_answer = input('To exit please enter "bye". Otherwise, please enter any word: ')


class PatientRecord:
    def __init__(self, id, surname, two_hours_value=0, fasting_value=0):
        self.__id = id
        self.__surname = surname
        self.__two_hours_value = two_hours_value
        self.__fasting_value = fasting_value

    def get_surname(self):
        return self.__surname

    def get_ID(self):
        return self.__id

    def set_two_hours_value(self, two_hours):
        self.__two_hours_value = two_hours

    def set_fasting_value(self, fasting):
        self.__fasting_value = fasting

    def get_current_level(self):
        if self.__two_hours_value > 0:
            return f'Dear Healthcare Provider,\n' \
                   f'The current blood sugar level is {self.__two_hours_value} mmol/l and the test has been done after two hours of eating.'
        elif self.__fasting_value > 0:
            return f'Dear Healthcare Provider,\n' \
                   f'The current blood sugar level is {self.__fasting_value} mmol/l and the test has been done while fasting.'


patient_id = input('Please enter your health insurance ID: ')
patient_surname = input('Please enter your surname: ')
patient_info = PatientRecord(patient_id, patient_surname)
print('Your data has been saved!')
print(f'Welcome Mr/Ms {patient_info.get_surname()}!')

def to_mmol_converter(num):
    return num / 18


unit_type = input('Is your blood sugar level measured in mg/dL?\n Please enter "yes" or "no": ')
if unit_type.lower() == 'yes':
    unit = float(input('Please enter your value in mg/dL and we will convert it to mmol/l: '))
    unit = round(to_mmol_converter(unit), 2)
    print(f'Here is your new blood sugar level value {unit} mmol/l\nPlease use it for the next steps!')
elif unit_type.lower() == 'no':
    print("Great! let's continue")
while user_answer.lower() != 'bye':
    two_hours_test = input(
        'Did you measure your blood sugar level after two hours of eating?\n Please enter "yes" or "no": ')
    if two_hours_test.lower() == 'yes':
        two_hours_value = float(input('Please enter your blood sugar level in mmol/l unit: '))
        patient_info.set_two_hours_value(two_hours_value)
        if 3.9 < two_hours_value < 7.8:
            print('Your blood sugar level is within normal range!')
        elif 7.8 <= two_hours_value < 16.7:
            print('Your blood sugar level is high, please consider taking your medication!')
        elif two_hours_value >= 16.7:
            print('Your blood sugar level is too high! please consider talking to your doctor')
            doctor_consult = input(
                'Would you like to proceed to our videoconference platform?\n If yes please enter "yes": ')
            if doctor_consult.lower() == 'yes':
                print(f'Hello Mr/Ms {patient_info.get_surname()},')
                print(
                    'Welcome to our videoconference platform!\nIn a moment, one of our healthcare providers will talk to you!')
                print(patient_info.get_current_level())
            else:
                print('Please take care!')
        elif two_hours_value < 3.9:
            print('Your blood sugar level is too low! please consider talking to your doctor')
            doctor_consult = input(
                'Would you like to proceed to our videoconference platform?\n If yes please enter "yes": ')
            if doctor_consult.lower() == 'yes':
                print(f'Hello Mr/Ms {patient_info.get_surname()},')
                print(
                    'Welcome to our videoconference platform!\nIn a moment, one of our healthcare providers will talk to you!')
                print(patient_info.get_current_level())
            else:
                print('Please take care!')
        break
    elif two_hours_test.lower() == 'no':
        fasting_test = input('Did you measure your blood sugar level while fasting?\n Please enter "yes" or "no": ')
        if fasting_test.lower() == 'yes':
            fasting_value = float(input('Please enter your blood sugar level in mmol/l unit: '))
            patient_info.set_fasting_value(fasting_value)
            if 3.9 < fasting_value < 7:
                print('Your blood sugar level is within normal range!')
            elif 7 <= fasting_value < 14.4:
                print('Your blood sugar level is high, please consider taking your medication!')
            elif fasting_value >= 14.4:
                print('Your blood sugar level is too high! please consider talking to your doctor')
                doctor_consult = input(
                    'Would you like to proceed to our videoconference platform?\n If yes please enter "yes": ')
                if doctor_consult.lower() == 'yes':
                    print(f'Hello Mr/Ms {patient_info.get_surname()},')
                    print(
                        'Welcome to our videoconference platform!\nIn a moment, one of our healthcare providers will talk to you!')
                    print(patient_info.get_current_level())
                else:
                    print('Please take care!')
            elif fasting_value < 3.9:
                print('Your blood sugar level is too low! please consider talking to your doctor')
                doctor_consult = input(
                    'Would you like to proceed to our videoconference platform?\n If yes please enter "yes": ')
                if doctor_consult.lower() == 'yes':
                    print(f'Hello Mr/Ms {patient_info.get_surname()},')
                    print(
                        'Welcome to our videoconference platform!\nIn a moment, one of our healthcare providers will talk to you!')
                    print(patient_info.get_current_level())

                else:
                    print('Please take care!')
            break
        elif fasting_test.lower() == 'no':
            user_answer = input('Would you like to exit the program?\n If yes please enter "bye": ')
            if user_answer.lower() == 'bye':
                print('Thank you for your time!\nGoodbye!')
                break
