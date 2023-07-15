#!/usr/bin/python3
"""
Entry Point into the command interpreter
"""
import re
import ast
import cmd
import sys
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
            instances = [str(inst) for inst in all_inst.values()
                         if inst.__class__.__name__ == arg]
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
            return
        elif len(arg) < 3:
            print("** attribute name missing **")
            return
        elif len(arg) < 4:
            print("** value missing **")
            return
        else:
            data_types = [int, float, str]
            for d_type in data_types:
                try:
                    if d_type is str:
                        arg[3] = arg[3].strip('"')
                    value = d_type(arg[3])
                    all_inst[key].__setattr__(arg[2], value)
                    break
                except ValueError:
                    continue
        storage.save()

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
        pattern = r"^([a-zA-Z]+)\.([a-z]+)" \
            r"\((?:\"([\w-]+)\"(?:,\s+(.+?,\s+.+?|\{.+?\})?)?)?\)$"
        match = re.findall(pattern, line)
        if match != [] and match[0][0] in self.__classes:
            cls = match[0][0]
            method = match[0][1]
            user_id = match[0][2]
            data_str = match[0][3]
            if method == 'all' and (user_id == '' and data_str == ''):
                self.all(cls)
            elif method == 'count' and (user_id == '' and data_str == ''):
                self.count(cls)
            elif method == 'show' and data_str == '':
                self.do_show(cls + ' ' + user_id)
            elif method == 'destroy' and data_str == '':
                self.do_destroy(cls + ' ' + user_id)
            elif method == 'update':
                if data_str[0] != '{':
                    data_str = '(' + data_str + ')'
                try:
                    data_str = ast.literal_eval(data_str)
                    if type(data_str) is dict:
                        for key, value in data_str.items():
                            self.do_update(' '.join([cls, user_id,
                                                     str(key), str(value)]))
                    elif type(data_str) is tuple:
                        self.do_update(' '.join([cls, user_id,
                                                str(data_str[0]),
                                                str(data_str[1])]))
                    else:
                        print("** Unknown command: ", line)
                        return
                except (SyntaxError, ValueError):
                    print("** Unknown command: ", line)
                    return
            else:
                print("** Unknown command: ", line)
                return
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

    def postloop(self):
        """
        Runs after the console loop is over
        """
        print("")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
