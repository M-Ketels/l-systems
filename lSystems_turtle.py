import turtle
import lSystems as lSys


def main():
    draw_turtle(5, "Examples/SierpinskiTriangle.json", 1000)
    #draw_turtle(6, "Examples/fractalplant.json", 1000)


def trans_to_dict(json_file_loc: str) -> dict:
    config_dict = lSys.json_to_dict(json_file_loc)
    translations_dict = config_dict["translations"]
    return translations_dict


def draw_turtle(iteration: int, json_file_loc: str, draw_speed: int) -> None:
    to_draw_string = lSys.json_str_expansion(json_file_loc, iteration)
    print(to_draw_string)
    translations = trans_to_dict(json_file_loc)
    print(translations)

    position_stack = []

    draw = turtle.Turtle()
    turtle.Screen()
    draw.speed(draw_speed)
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
        elif "stop" == to_do:
            draw.heading()
        elif "save" == to_do:
            position_stack.append(draw.pos())
            #saved_pos = draw.pos()
        elif "rest" == to_do:
            draw.penup()
            popped_position = position_stack.pop()
            draw.goto(popped_position[0], popped_position[1])
            #draw.goto(saved_pos[0], saved_pos[1])
            draw.pendown()
    turtle.done()


if __name__ == "__main__":
    main()
