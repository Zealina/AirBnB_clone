#!/usr/bin/python3
"""
Entry Point into the command interpreter
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Defines the methods for the command interpreter
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "Place",
        "City",
        "Review",
        "Amenity"
        }
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            my_instance = BaseModel()
            my_instance.save()
            print(my_instance.id)
        else:
            print("** class doesn't exist **")

    def show(self, arg):
        """
        Prints string representation based on class name and id"""
        pass

    def emptyline(self):
        """Called when an emptyline is entered
        """
        pass
    def do_EOF(self, arg):
        """
        Exits on pressing Ctrl + D on  keyboard
        """
        return True

    def do_quit(self, arg):
        """Exits the console"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
