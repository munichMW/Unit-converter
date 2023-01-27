import math

units = {
    "quetta": 30,
    "ronna": 27,
    "yotta": 24,
    "zetta": 21,
    "exa": 18,
    "peta": 15,
    "tera": 12,
    "giga": 9,
    "mega": 6,
    "kilo": 3,
    "hecto": 2,
    "deca": 1,
    "normal": 0,
    "deci": -1,
    "centi": -2,
    "milli": -3,
    "micro": -6,
    "nano": -9,
    "pico": -12,
    "femto": -15,
    "atto": -18,
    "zepto": -21,
    "yocto": -24,
    "ronto": -27,	
    "quecto": -30

}

def checki(question):
    prompt = input(question)
    split_word = None
    for unit in units:
        if unit in prompt:
            split_word = [unit, prompt[len(unit):], prompt]
            break
    return split_word

def sci_notation(num):
  power = 0
  while abs(num) >= 10:
    num /= 10
    power += 1
  return num,power

numb = float(input("amount: "))
default_unit = checki("default_unit: ")
new_unit = checki("new_unit: ")

newdefault_unit = units.get(default_unit[0], None)
newnew_unit = units.get(new_unit[0], None)

if newdefault_unit is not None and newnew_unit is not None:
    calcu = numb * math.pow(10.00000000000,(newdefault_unit - newnew_unit))
    scinonum = sci_notation(numb)
    print(calcu, new_unit[2],)
    print(scinonum[0],"x 10 ^",(scinonum[1] + (newdefault_unit - newnew_unit)))
else:
    print("Invalid unit selected.")
