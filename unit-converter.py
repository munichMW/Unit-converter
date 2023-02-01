import math

prefix = {
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

    "angle": {
        "degrees": 180,
        "radian": math.pi,
        "gradians": 200,
        "circle": 0.5,
        "brad": 128,
        "c MOA": 20000,
        "c SOA": 2000000,
        "gons": 200,
        "hexacontades": 30,
        "Hour Angles": 12,
        "mils": 3200,
        "points": 16,
        "revolution": 0.5,
        "sign": 6,
        "turns": 0.5,
    },

    "data": {
        "bit": 1,
        "byte": 0.125,
        "character": 0.125,
    },

    "area": {
        "square meter": 1,
        "square mile": 0.00062137,
        "square inch": 39.3700787,
        "square foot": 3.2808399,
        "square yard": 1.0936133,
    },

    "volume": {
        "cubic meter": 1,
        "cubic mile": 0.00062137,
        "cubic inch": 39.3700787,
        "cubic foot": 3.2808399,
        "cubic yard": 1.0936133,
    },


}


def checki(prompt):
    split_word = [prompt, prompt, prompt]
    for unit in prefix:
        if prompt.startswith(unit):
            split_word = [unit, prompt[len(unit):], prompt]
            break
    return split_word


def convert_unit(value, from_unit_pre, to_unit_pre, from_unit, to_unit):
    fpre = prefix.get(from_unit_pre)
    if fpre is None:
        fpre = 0

    tpre = prefix.get(to_unit_pre)
    if tpre is None:
        tpre = 0

    for category in conversion:
        if from_unit in conversion[category] and to_unit in conversion[category]:
            return value * ((conversion[category][to_unit] * 10 ** float(fpre)) / (conversion[category][from_unit] * 10 ** float(tpre)))
    return "incorrect"


def convert_area(value, from_unit_pre, to_unit_pre, from_unit, to_unit, dimen):
    fpre = prefix.get(from_unit_pre)
    if fpre is None:
        fpre = 0

    tpre = prefix.get(to_unit_pre)
    if tpre is None:
        tpre = 0

    for category in conversion:
        if from_unit in conversion[category] and to_unit in conversion[category]:
            return value * math.pow(((conversion[category][to_unit] * 10 ** float(fpre)) / (conversion[category][from_unit] * 10 ** float(tpre))), dimen)
    return "incorrect"

def check_float(number):
    while True:
        try:
            value = float(input(number))
        except ValueError:
            print("Only numbers can be used.")
            continue
        break
    return value


def get_category(unit):
    for category, units in conversion.items():
        if unit in units:
            return category
    return None


def checker():
    while True:
        try:
            a = check_float("value: ")
            b = checki(input("from: "))
            c = checki(input("to: "))

            value = a
            from_unit_pre = b[0]
            to_unit_pre = c[0]
            from_unit = b[1]
            to_unit = c[1]
            u = get_category(b[2])

            if u == "None":
                u = get_category(from_unit)

            if (u == "length" or u == "mass" or u == "time" or u == "angle" or u == "data"):
                ck = float(convert_unit(value, from_unit_pre,
                           to_unit_pre, from_unit, to_unit))
            elif (u == "area"):
                ck = float(convert_area(value, from_unit_pre,
                           to_unit_pre, from_unit, to_unit,2))
            elif (u == "volume"):
                ck = float(convert_area(value, from_unit_pre,
                           to_unit_pre, from_unit, to_unit,3))

        except ValueError:
            print("Incorrect unit")
            continue
        break
    return ck, c[2]


p = checker()
print(p[0], p[1])
