#!/usr/bin/python3
"""
Entry Point into the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Defines the methods for the command interpreter
    """
    prompt = "(hbnb) "
    __classes = {"BaseModel": BaseModel}
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg in self.__classes:
            my_instance = self.__classes[arg]()
            my_instance.save()
            print(my_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints string representation based on class name and id
        """
        arg = self.parser(arg)
        if not arg:
            return
        key = arg[0] + '.' + arg[1]
        all_inst = storage.all()
        try:
            print(all_inst[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Removes an instance of class from storage
        """
        arg = self.parser(arg)
        if not arg:
            return
        key = arg[0] + '.' + arg[1]
        all_inst = storage.all()
        try:
            storage.all().pop(key)
            storage.save()
        except KeyError:
            print("** no instance found **")

    def emptyline(self):
        """Called when an emptyline is entered
        """
        pass

    def parser(self, arg):
        """Sanitizes the argument"""
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            return arg

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
