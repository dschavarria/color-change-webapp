import os
import sys
import random
from flask import Flask
from flask import render_template

app = Flask(__name__)

if os.environ.get('HOSTNAME') != None:
    hostname = os.environ.get('HOSTNAME')
elif os.environ.get('NAME') != None:
    hostname = os.environ.get('NAME')
else:
    hostname = "anon"


def choose_color():
    if os.environ.get('APP_COLOR') != None:
        color = os.environ.get('APP_COLOR')
        color_source = 'APP_COLOR env variable'
    elif len(sys.argv) > 1:
        color = sys.argv[1]
        color_source = 'commandline argument'
    else:
        switcher = {
            1: 'gray',
            2: 'red',
            3: 'yellow',
            4: 'green',
            5: 'blue',
            6: 'indigo',
            7: 'purple',
            8: 'pink'
        }
        color = switcher.get(random.randint(1, 8), "ERROR")
        color_source = 'random value'
    return {"color": color, "color_source": color_source}


@app.route("/")
def main():
    color_dict = choose_color()
    color = color_dict.get("color", "error")
    color_source = color_dict.get("color_source", "error")

    bgcolor = f"bg-{color}-400"

    print("\nThe background color is chosen at random unless set by passing a \nsingle string argument or by setting the APP_COLOR environmental\nvariable.")

    print(
        f"\nIn this case the background color ({color}) is from the {color_source}\n")

    return render_template('hello.html', bgcolor=bgcolor, hostname=hostname)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
