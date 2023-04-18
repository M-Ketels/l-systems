import turtle
import lSystems as lSys
import ProgressBar as pb
import sys


def main():
    # draw_turtle(5, "Examples/KochCurve.json", 1000)
    # draw_turtle(5, "Examples/SierpinskiTriangle.json", 1000)
    # draw_turtle(6, "Examples/fractalplant.json", 1000)
    draw_turtle(5, "Examples/AsignmentPlant.json", 0)


def trans_to_dict(json_file_loc: str) -> dict:
    config_dict = lSys.json_to_dict(json_file_loc)
    translations_dict = config_dict["translations"]
    return translations_dict


def draw_turtle(iteration: int, json_file_loc: str, draw_speed: int, show_progressbar=True, export=False, export_file_name="export.eps") -> None:
    # TODO: add documentation
    to_draw_string = lSys.json_str_expansion(json_file_loc, iteration)
    translations = trans_to_dict(json_file_loc)

    position_stack = []
    heading_stack = []
    color_stack = []

    draw = turtle.Turtle()
    draw.setheading(90)
    turtle.Screen()
    draw.speed(draw_speed)

    if show_progressbar:
        amount_of_chars = len(to_draw_string)
        step = 0
        pb.printProgressBar(0, amount_of_chars, "drawing l-system")

    for char in to_draw_string:
        to_do = translations[char][0]
        if "draw" == to_do:
            value = translations[char][1]
            draw.forward(value)
        elif "angle" == to_do:
            value = translations[char][1]
            if value > 0:
                draw.right(value)
            else:
                draw.left(abs(value))
        elif "nop" == to_do:
            draw.heading()
        elif "push" == to_do:
            position_stack.append(draw.pos())
            heading_stack.append(draw.heading())
            color_stack.append(draw.pencolor())
        elif "pop" == to_do:
            draw.penup()
            popped_position = position_stack.pop()
            draw.goto(popped_position[0], popped_position[1])
            popped_heading = heading_stack.pop()
            draw.setheading(popped_heading)
            popped_color = color_stack.pop()
            draw.pencolor(popped_color)
            draw.pendown()
        elif "forward" == to_do:
            draw.penup()
            value = translations[char][1]
            draw.forward(value)
            draw.pendown()
        elif "color" == to_do:
            color = translations[char][1]
            draw.pencolor(color)

        if show_progressbar:
            step += 1
            pb.printProgressBar(step, amount_of_chars, "drawing l-system")

    if export:
        turtle_screen = turtle.getscreen()
        turtle_screen.getcanvas().postscript(file=export_file_name)

    turtle.done()

    if show_progressbar:
        sys.stdout.write("\n")  # needed to correctly setup the next line in the terminal


if __name__ == "__main__":
    main()
