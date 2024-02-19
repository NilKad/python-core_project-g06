colors_dict = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "PURPLE": "\033[35m",
    "SKY": "\033[36m",
    "GREY": "\033[37m",
    "DARKGREY": "\033[90m",
    "RESET": "\033[0m",
}


def textc(text_string, color):
    return f'{colors_dict[color]}{text_string}{colors_dict["RESET"]}'
