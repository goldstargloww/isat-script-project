import random


def generate_shake(count = 1, start = 1):
    # count = the amount of shakes to generate
    # start = the number to start at in the animation names
    
    # this generates a shake animation in case you feel like the current ones
    # aren't enough. this is useful for more variation in the animations


    # these set different offsets for each keyframe in the animation
    #
    # the random function is taken from the kinetic text tags renpy plugin
    # (? are they called plugins. idk it's just some code i found)

    x1 = (random.random()-0.2) * 2
    x2 = (random.random()-0.2) * 2
    x3 = (random.random()-0.2) * 2
    x4 = (random.random()-0.2) * 2
    x5 = (random.random()-0.2) * 2
    x6 = (random.random()-0.2) * 2
    x7 = (random.random()-0.2) * 2
    x8 = (random.random()-0.2) * 2
    x9 = (random.random()-0.2) * 2
    xX = (random.random()-0.2) * 2

    y1 = (random.random()-0.3) * 2
    y2 = (random.random()-0.3) * 2
    y3 = (random.random()-0.3) * 2
    y4 = (random.random()-0.3) * 2
    y5 = (random.random()-0.3) * 2
    y6 = (random.random()-0.3) * 2
    y7 = (random.random()-0.3) * 2
    y8 = (random.random()-0.3) * 2
    y9 = (random.random()-0.3) * 2
    yX = (random.random()-0.3) * 2

    if count <= 0:
        raise ValueError("need at least 1!")

    elif count > 1:
        output = []
        for i in range(count):
            output.append("@keyframes shake" + str(i + start) + " {\n  0%   { transform: translate(" + str(x1) + "px, " + str(y1) + "px)}\n  10%  { transform: translate(" + str(x2) + "px, " + str(y2) + "px)}\n  20%  { transform: translate(" + str(x3) + "px, " + str(y3) + "px)}\n  30%  { transform: translate(" + str(x4) + "px, " + str(y4) + "px)}\n  40%  { transform: translate(" + str(x5) + "px, " + str(y5) + "px)}\n  50%  { transform: translate(" + str(x6) + "px, " + str(y6) + "px)}\n  60%  { transform: translate(" + str(x7) + "px, " + str(y7) + "px)}\n  70%  { transform: translate(" + str(x8) + "px, " + str(y8) + "px)}\n  80%  { transform: translate(" + str(x9) + "px, " + str(y9) + "px)}\n  90%  { transform: translate(" + str(xX) + "px, " + str(yX) + "px)}\n  100% { transform: translate(" + str(x1) + "px, " + str(y1) + ")}\n}")

            # looks complicated, but essentially returns a list of these:

            # @keyframes shake<i> {
            #   0%   { transform: translate(<x1>px, <y1>px)}
            #   10%  { transform: translate(<x2>px, <y2>px)}
            #   20%  { transform: translate(<x3>px, <y3>px)}
            #   30%  { transform: translate(<x4>px, <y4>px)}
            #   40%  { transform: translate(<x5>px, <y5>px)}
            #   50%  { transform: translate(<x6>px, <y6>px)}
            #   60%  { transform: translate(<x7>px, <y7>px)}
            #   70%  { transform: translate(<x8>px, <y8>px)}
            #   80%  { transform: translate(<x9>px, <y9>px)}
            #   90%  { transform: translate(<xX>px, <yX>px)}
            #   100% { transform: translate(<x1>px, <y1>px)}
            # }

        return output

    elif count == 1:
        return "@keyframes shake" + str(start) + " {\n  0%   { transform: translate(" + str(x1) + "px, " + str(y1) + "px)}\n  10%  { transform: translate(" + str(x2) + "px, " + str(y2) + "px)}\n  20%  { transform: translate(" + str(x3) + "px, " + str(y3) + "px)}\n  30%  { transform: translate(" + str(x4) + "px, " + str(y4) + "px)}\n  40%  { transform: translate(" + str(x5) + "px, " + str(y5) + "px)}\n  50%  { transform: translate(" + str(x6) + "px, " + str(y6) + "px)}\n  60%  { transform: translate(" + str(x7) + "px, " + str(y7) + "px)}\n  70%  { transform: translate(" + str(x8) + "px, " + str(y8) + "px)}\n  80%  { transform: translate(" + str(x9) + "px, " + str(y9) + "px)}\n  90%  { transform: translate(" + str(xX) + "px, " + str(yX) + "px)}\n  100% { transform: translate(" + str(x1) + "px, " + str(y1) + ")}\n}"
    
        # looks complicated, but essentially returns this:

        # @keyframes shake<i> {
        #   0%   { transform: translate(<x1>px, <y1>px)}
        #   10%  { transform: translate(<x2>px, <y2>px)}
        #   20%  { transform: translate(<x3>px, <y3>px)}
        #   30%  { transform: translate(<x4>px, <y4>px)}
        #   40%  { transform: translate(<x5>px, <y5>px)}
        #   50%  { transform: translate(<x6>px, <y6>px)}
        #   60%  { transform: translate(<x7>px, <y7>px)}
        #   70%  { transform: translate(<x8>px, <y8>px)}
        #   80%  { transform: translate(<x9>px, <y9>px)}
        #   90%  { transform: translate(<xX>px, <yX>px)}
        #   100% { transform: translate(<x1>px, <y1>px)}
        # }

    else:
        raise Exception("what") # how did you get here. this should be impossible
    





def wrap_in_spans(input: str):
    output = ""
    for character in input:
        if character == " ":
            output += " "
        else:
            output += "<span>" + character + "</span>"
    return output


# replace the text here with whatever you want your text to say!
print(wrap_in_spans(
    "(ボニーが、こんなこと、言うはずないだろ！！！)"
))