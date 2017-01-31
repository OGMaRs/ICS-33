#48783106 Kevin Luu
from goody import type_as_str
import inspect
class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (raises AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')

3.
class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (raise AssertionError) this classes raises AssertionError and prints its
      failure, along with a list of all annotations tried followed by the check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set name to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self.checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        def error_message(error):
            if error == "incorrect type":
                return '{param} failed annotation check ({error}): value = {x} was type {type_value} ...should be type {annot}'.format(param = param, error = 'wrong type', x = value , type_value = type_as_str(value), annot = annot) + check_history
            elif error == 'wrong number':
                return '{param} failed annotation check ({error}): value = {x} annotation had {length} elements {annot}'.format(param = param, error = 'wrong number of elements', x = value , length = len(annot), type_value = type_as_str(value), annot = annot)
            elif error == "inconsistent":
                return '{param} {error}: {type_annot} should have 1 item but had {length} annotation = {annot}'.format(param = param, error = 'annotation inconsistency', type_annot = str(type(annot)), length = str(len(annot)), annot = annot)

            
        def check_list(type_item):
            assert isinstance(value, type_item),error_message(error = 'incorrect type')
            if len(annot) == 1:
                for i in range(len(value)):
                    self.check(param, annot[0], value[i], check_history + '\n' + type_as_str((annot)) + str([i]) + 'check: '+str(annot[0]))
            elif len(annot) > 1:
                assert len(annot) == len(value), error_message( error = 'wrong number')
                for i in range(len(annot)):
                    self.check(param, annot[i], value[i], check_history + '\n' + type_as_str((annot)) + str([i]) + 'check: '+str(annot[i]))
                    
        def check_dict():
            assert isinstance(value,dict),error_message(error = 'incorrect type')
            assert len(annot.keys()) <= 1, error_message(error = 'inconsistent')
            for key in value.keys():
                self.check(param, list(annot.keys())[0], key, check_history + '\n' +'dict value check: ' + str(list(annot.keys())[0]))
            for element in value.values():
                self.check(param, list(annot.values())[0], element, check_history + '\n' +'dict key check: ' + str(list(annot.values())[0]))
                
        def check_sets(set_type):
            assert isinstance(value, set_type), error_message(error = 'incorrect type')
            assert len(annot) == 1, error_message(error = 'wrong number')
            for values in value:
                self.check(param, list(annot)[0], values, check_history + '\n' +'set value check: ' +str(list(annot)[0]))
                
        def check_lambda():
            assert len(annot.__code__.co_varnames) == 1, '{param} annotation inconsistency: predicate should have 1 parameter but had {x} predicate = {annot}'.format(param = param, x = len(annot.__code__.co_varnames), annot = annot )
            try:
                funct = annot(value)
                assert funct, '{param} failed annotation check: value = {value} predicate = {annot}'.format(param = (param), value = (value), annot = str(annot))    
            except Exception as error:
                raise AssertionError('{param} annotation predicate({annot}) raised exception exception = {error}: {message}'.format(param = param, annot = annot, error = type(error), message = error) + check_history)
                

        if annot == None:
            pass
        elif annot == int:
            assert isinstance(value, int), error_message(error = 'incorrect type')
        elif annot == str:
            assert isinstance(value, str), error_message(error = 'incorrect type')
            
        elif annot == float:
            assert isinstance(value, float), error_message(error = 'incorrect type')
            
        elif annot == list:
            assert isinstance(value, list),error_message(error = 'incorrect type')
        elif type(annot) == list:
            check_list(type_item = list)
            
        elif annot == tuple:
            assert isinstance(value, tuple),error_message(error = 'incorrect type')
        elif type(annot) == tuple:
            check_list(type_item = tuple)
            
        elif annot == dict:
            assert isinstance(value,dict),error_message(error = 'incorrect type')  
        elif type(annot) == dict:
            check_dict()
            
        elif annot == set:
            assert isinstance(value, set), error_message(error = 'incorrect type')
        elif type(annot) == set:
            check_sets(set)
            
        elif annot == frozenset:
            assert isinstance(value, frozenset), error_message(error = 'incorrect type')
        elif type(annot) == frozenset:
            check_sets(frozenset)
            
        elif inspect.isfunction(annot):
            check_lambda()
            
        else:
            try:
                annot.__check_annotation__(self.check, param, value, check_history)
            except AttributeError:
                raise AssertionError("{cla} has no _check_annotation__method persent".format(cla = annot))
            except:
                raise AssertionError("{cla} __check__annotation has failed or raised an exception".format(cla = annot))


        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Decode annotation and check it 
        
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if self.checking_on == False and Check_Annotation.checking_on == False :
            return self._f(*args, **kargs)
        x = param_arg_bindings()
        y = self._f.__annotations__
        try:
            # Check the annotation for every parameter (if there is one)
            for item in x.keys():
                if item in y:
                    self.check(item,y[item],x[item])
            # Compute/remember the value of the decorated function
            value = self._f(*args, **kargs)
            # If 'return' is in the annotation, check it
            if 'return' in y:
                self.check('return', y['return'], value)
            # Return the decorated answer
            return value
           
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            #print(80*'-')
            #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
                #print(l.rstrip())
            #print(80*'-')
            raise

  
if __name__ == '__main__':     

    import driver
    driver.driver()
