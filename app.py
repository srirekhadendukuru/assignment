from flask import Flask, json, request
import random


app = Flask(__name__)

jokes = ["Joke 1: What do a zoo owner and a Python data analyst have in common?They both are pandas   ",
         "Joke 2: A little girl walks into a pet shop and asks for a bunny. The worker says the fluffy white one or the fluffy brown one? The girl then says, I do not think my python really cares   ",
         "Joke 3: When life gets you down, remember the immortal words of Monty Python.NOBODY EXPECTS THE SPANISH INQUISITION   ",
         "Joke 4: Why does the Python live on land?Because its above C-level   ",
         "Joke 5: Did you hear about the computer nerd who was eaten alive by a giant snake?Now he is programming in python.   ",
         "Joke 6: Why do Python programmers have low self esteem?They are constantly comparing their self to other.   ",
         "Joke 7: What do you call Monty Python if it is filled with corn? Del Monte Python   ",
         "Joke 8: Why do some people think Python scripting is offensive? Because white space matters. hehe   ",
         "Joke 9: I remember the day my son found out the neighbor's python was not venomoush was crushed   ",
         "Joke 10: Why was the programmer killed by a snake?He underestimated the speed of the python.   "]


@app.route('/')


def index():
    return json.dumps(jokes)


@app.route('/jokes', methods=['GET'])
def get():
    return json.dumps(random.choices(jokes))


@app.route('/joker', methods=['GET'])
def joke():
    num = request.args.get('num')
    result = ""
    result = result.join((random.sample(jokes, int(num))))
    print(result)
    return (result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)