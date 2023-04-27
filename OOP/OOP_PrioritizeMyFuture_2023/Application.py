import sys

import var.Constants
from src.User import User, RegisteredUser
from src.RegistrationPolicy import RegistrationPolicy


class Application:
    def __init__(self):
        self.user = User()

    def run(self):
        print(var.Constants.GREETING_TEXT)
        self.user.set_username(input("Enter your username: "))
        self.user.set_password(input("Enter your password: "))
        RegistrationPolicy.registration(self, self.user.get_username(), self.user.get_password())
        self.registration_user = RegisteredUser(self.user.get_username())
        self.response()

    @staticmethod
    def stop(self):
        sys.exit()

    def response(self):
        print(var.Constants.OPTIONS_TODO)
        while True:
            user_input = input('Choose command: ')
            if user_input == '1':
                self.registration_user.add_task()
            if user_input == '2':
                operation = int(input("Enter task that are you going to remove:  "))
                self.registration_user.remove_task(operation)
            if user_input == '3':
                operation = int(input("Enter number of task that are you going to update:  "))
                choose_operation = int(
                    input("Enter the field in task to update:\n1-name\n2-cost\n3-category\n4-status\n"))
                new_parameter = input("Enter new field: ")
                self.registration_user.update_task(operation, choose_operation, new_parameter)
            if user_input == '4':
                self.registration_user.show_all_tasks()
            if user_input == '5':
                operation = int(input("Enter number of task: "))
                self.registration_user.show_specific_task(operation)
            if user_input == '6':
                self.registration_user.show_done_task()
            if user_input == '7':
                self.registration_user.show_not_done_task()
            if user_input == '8':
                self.registration_user.calculate_statistic_for_not_done_task()
            if user_input == '9':
                self.registration_user.calculate_statistic_for_done_task()
            if user_input == '10':
                print("Thank you for using our app! See you soon!")
                self.stop(self)
            """
            if user_input == '11':
                self.burn_today(self)
            if user_input == '12':
                self.transfer_to_future(self)
            """