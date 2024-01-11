start_text="\033["
end_text="m"
def build(id):
    return f"{start_text}{id}{end_text}"
class ForeColor():
    RED=build(31)
    GREEN=build(32)
    YELLOW=build(33)
    BLUE=build(34)
    PURPLE=build(35)
    LIGHT_BLUE=build(36)
    GREY=build(90)
    LIGHT_RED=build(91)
    LIGHT_GREEN=build(92)
    LIGHT_YELLOW=build(93)
    LIGHT_BLUE_EX=build(94)
    LIGHT_PURPLE=build(95)
    LIGHT_BLUE_EEX=(96)
    LIGHT_WHITE=build(97)

    pass

class BackColor():
    RED=build(41)
    GREEN=build(42)
    YELLOW=build(43)
    BLUE=build(44)
    PURPLE=build(45)
    WHITE=build(46)
    GREY=build(100)
    LIGHT_RED=build(101)
    LIGHT_GREEN=build(102)
    LIGHT_YELLOW=build(103)
    LIGHT_BLUE=build(104)
    LIGHT_PURPLE=build(105)
    LIGHT_BLUE_EX=build(106)
    LIGHT_WHITE=build(1070)

class Style():
    STRONG=build(1)
    CLOSE_STRONG=build(2)
    ITALICS=build(3)
    ONE_UNDERLINE=build(4)
    FLASH=build(5)
    BACKGROUND=build(7)
    STRIKETHROUGH=build(9)
    TWO_UNDERLINE=build(21)
    REST=build(0)
    pass

