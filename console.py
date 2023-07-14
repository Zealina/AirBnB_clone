#!/usr/bin/python3
"""
Entry Point into the command interpreter
"""
import re
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Defines the methods for the command interpreter
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel, "User": User,
            "State": State, "Amenity": Amenity,
            "Place": Place, "Review": Review
    }
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
    
    def do_all(self, arg):
        """
        Prints string representation of all instances of all classes
        """
        all_inst = storage.all()
        if arg and arg not in self.__classes:
            print("** class doesn't exist **")
            return
        elif arg and arg in self.__classes:
            instances = [str(inst) for inst in all_inst.values() if inst.__class__.__name__ == arg]
        else:
            instances = [inst.__str__() for inst in all_inst.values()]
        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or 
        updating attribute
        """
        arg = self.parser(arg)
        if not arg:
            return
        all_inst = storage.all()
        key = arg[0] + '.' + arg[1]
        if key not in all_inst:
            print("** no instance found **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            data_types = [int, float, str]
            for d_type in data_types:
                try:
                    if d_type is str:
                        arg[3] = arg[3][1:-1]
                    value = d_type(arg[3])
                    all_inst[key].__setattr__(arg[2], value)
                    break
                except ValueError:
                    continue


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

    def default(self, line):
        """
        Add customizations to the default command
        """
        pattern = r"^([a-zA-Z]+).([a-z]+)\(([\w-]+)?\)$"
        match = re.findall(pattern, line)
        if match != [] and match[0][0] in self.__classes:
            a = match[0]
            if a[1] == 'all' and not a[2]:
                self.all(match[0][0])
            elif a[1] == 'count' and not a[2]:
                self.count(match[0][0])
            elif a[1] == 'show':
                self.do_show(a[0] + ' ' + a[2])
            elif a[1] == 'destroy':
                self.do_destroy(a[0] + ' ' + a[2])
            elif a[1] == 'update':
                arg = a[2].split()
                print(arg)
        else:
            print("** Unknown command: ", line)

    def all(self, cls_name):
        """
        Retrieves all instances of cls_name
        """
        all_inst = storage.all()
        i = 0
        print("[", end='')
        for inst in all_inst.values():
            if inst.__class__.__name__ == cls_name:
                if i == 0:
                    print(inst, end='')
                    i += 1
                else:
                    print(inst, end=', ')
        print("]")

    def count(self, cls_name):
        """
        Count number of instances of a class
        """
        count = 0
        all_inst = storage.all()
        for inst in all_inst.values():
            if inst.__class__.__name__ == cls_name:
                count += 1
        print(count)

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
