#Kevin Luu 48783106
import re, traceback, keyword
        
def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i, l in enumerate(s.split('\n'),1):
            print('{num: >3} {text}'.format(num= i, text= l.rstrip()))

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    def is_legal(name):
        legal_name = re.compile('([a-zA-Z]+)(\w*)$')
        if legal_name.match(str(name)) == None or name in keyword.kwlist:
            return False
        return True
    
    if not is_legal(str(type_name)):
        raise SyntaxError('{name} is not a legal entry.'.format(name = type_name))
    
    if type(field_names) != list and type(field_names) != str:
        raise SyntaxError('{name} + is not a list or string.'.format(name = field_names))
    
    arguments = []
    
    if type(field_names) == list:
        for item in field_names:
            if not is_legal(item):
                raise SyntaxError('{name} is not a legal entry.'.format(name = item))
            else:
                if item not in arguments:
                    arguments.append(item)
                
    elif type(field_names) == str:
        fields = re.split('\s*,*', field_names)
        for item in fields:
            if len(item) > 0 and item not in arguments:
                if not is_legal(item):
                    raise SyntaxError('{name} is not a legal entry.'.format(name = item))
                else:
                    arguments.append(item)
                      
    class_template = '''
class {type_name}:
    def __init__(self, {list_args}):
        {items}
        self._fields = {arguments}
        self._mutable = {self_mutable}'''
    
    template_repr = '''    
    def __repr__(self):
        return '{type_name}({repr})'.format({string_format})'''
    
    template_get = '''
    def get_{item}(self):
        return self.{item}'''
    
    template_getitem = '''
    def __getitem__(self, index):
        if type(index) == int:
            if index > len(self._fields):
                raise IndexError('{index} is greater than length of item'.format(index = index))
            return eval('self.get_{num}()'.format(num = self._fields[index]))
        elif type(index) == str:
            if index in self._fields:
                return eval('self.get_{place}()'.format(place = index))
            else:
                raise IndexError('{index} is an invalid indexing item'.format(index = index))
        else:
            raise IndexError('{index} is an invalid indexing item'.format(index = index))'''
    
    template_eq = '''
    def __eq__(self, right):
        if type(right) != {cla}:
            return False
        for item in self._fields:
            if self.__getitem__(item) != right.__getitem__(item):
                return False
        return True'''

    template_replace = '''
    def _replace(self, **kargs):
        if self._mutable:
            for element in kargs:
                self.__dict__[element] = kargs[element]
        else:
            for element in self._fields:
                if element not in kargs:
                    kargs[element] = self.__dict__[element]
            return {cla}(**kargs)'''
    
    template_setattr = '''
    def __setattr__(self, name, value):
        if '_mutable' in self.__dict__:
            if self._mutable == False:
                raise AttributeError("Value cannot be changed")
            else:
                self.__dict__[name] = value
        else:
            self.__dict__[name] = value'''

    class_definition = class_template.format(
        type_name = type_name, 
        list_args = ', '.join(item for item in arguments), 
        items = ('\n'+8*' ').join('self.{name} = {name}'.format(name = item) for item in arguments), 
        arguments = arguments, 
        self_mutable = mutable)
    
    class_definition += template_repr.format(
        type_name = type_name, 
        repr = ','.join('{value}={{{value}}}'.format(value = item)  for item in arguments),
        string_format = ','.join('{name}=self.{name}'.format(name=name) for name in arguments))
    
    for item in arguments:
        class_definition += template_get.format(item = item) 
        
    class_definition += template_getitem + template_eq.format(cla = type_name)+ template_replace.format(cla = type_name) + template_setattr

    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local name-space and bind the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   show the error
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except(SyntaxError,TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    import driver
    driver.driver()
