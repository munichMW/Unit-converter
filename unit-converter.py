units = {
    "quetta": 30,
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


conversion = {
    "none_prefix": {
        "": 1
    },
    "length": {
        "meter": 1,
        "mile": 0.00062137,
        "inch": 39.3700787,
        "foot": 3.2808399,
        "yard": 1.0936133,
        "AU": 1 / 149597870691,
        "ly": 1 / 9460730777119564,
        "pc": 1 / 30856775814671900,
        "เส้น": 2,
        "โยชน์": 1,
        "วา": 2,
        "ศอก": 0.5,
        "คืบ": 0.25,
        "นิ้ว": 1 / 48,
        "ฝ่ามือ": 1 / 12,
    },
    "mass": {
        "gram": 1000,
        "pound": 2.20462262,
        "ounce": 35.27396195,
        "stone": 0.157473,
        "carat": 5000,
        "amu": (1000 / (1.66053886 * (10 ** -24))),
        "newton": (1 / 101.9716212978) * 1000
    },
    "time": {
        "second": 86400,
        "minute": 1440,
        "hour": 24,
        "day": 1
    },
}

def checki(prompt):
    split_word = [prompt, prompt, prompt]
    for unit in units:
        if prompt.startswith(unit):
            split_word = [unit, prompt[len(unit):], prompt]
            break
    return split_word


def convert_unit(value, from_unit_pre, to_unit_pre, from_unit, to_unit):
    fpre = units.get(from_unit_pre)
    if fpre is None:
        fpre = 0
        
    tpre = units.get(to_unit_pre)
    if tpre is None:
        tpre = 0
        
    print(fpre,tpre)
    



    for category in conversion:
        if from_unit in conversion[category] and to_unit in conversion[category]:
            return value * ((conversion[category][to_unit] * 10 ** float(fpre)) / (conversion[category][from_unit] * 10 **  float(tpre)))
    return "incorrect"


a = float(input("a: "))
b = checki(input("from: "))
c = checki(input("to: "))
print(b,c, units.get(c[0]),units.get(b[0]))
print(convert_unit(a, b[0], c[0],b[1],c[1]),c[2]) 
