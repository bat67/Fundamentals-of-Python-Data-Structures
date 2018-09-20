"""
File: erapp.py
Author: Ken Lambert

A terminal-based view for an emergency room scheduler.
"""

from ermodel import ERModel, Patient, Condition

class ERView(object):
    """The view class for the ER application."""

    def __init__(self, model):
        self.model = model

    def run(self):
        """Menu-driven command loop for the app."""
        menu = "Main menu\n" + \
               "  1  Schedule a patient\n" + \
               "  2  Treat the next patient\n" + \
               "  3  Treat all patients\n" \
               "  4  Exit the program\n"
        while True:
            command = self.getCommand(4, menu)
            if   command == 1: self.schedule()
            elif command == 2: self.treatNext()
            elif command == 3: self.treatAll()
            else: break

    def treatNext(self):
        """Treats one patient if there is one."""
        if self.model.isEmpty():
            print("No patients available to treat")
        else:
            patient = self.model.treatNext()
            print(patient, "is being treated.")

    def treatAll(self):
        """Treats all the remaining patients."""
        if self.model.isEmpty():
            print("No patients available to treat.")
        else:
            while not self.model.isEmpty():
                self.treatNext()
   
    def schedule(self):
        """Obtains patient info and schedules patient."""
        name = input("\nEnter the patient's name: ")
        condition = self.getCondition()
        self.model.schedule(Patient(name, condition))
        print(name, "is added to the", condition, "list\n")

    def getCondition(self):
        """Obtains condition info."""
        menu = "Patient's condition:\n" + \
               "  1  Critical\n" + \
               "  2  Serious\n" + \
               "  3  Fair\n"
        number = self.getCommand(3, menu)
        return Condition(number)

    def getCommand(self, high, menu):
        """Obtains and returns a command number."""
        prompt = "Enter a number [1-" + str(high) + "]: "
        commandRange = list(map(str, range(1, high + 1)))
        error = "Error, number must be 1 to " + str(high)
        while True:
            print(menu)
            command = input(prompt)
            if command in commandRange:
                return int(command)
            else:
                print(error)

# Main function to start up the application

def main():
    model = ERModel()
    view = ERView(model)
    view.run()

if __name__ == "__main__":
    main()

            
