from flask import Flask 

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python operations with Flask Routing and Views </h1>'

@app.route('/<string:username>')
def user(username):
    return f"<h1>Profile for {username}</h1>"
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f"<h2>The string is: {parameter}</h2>"
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers=[str(i) for i in range(parameter)]
    return "\n".join(numbers) + "\n"
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        return {"result":num1+num2}
    elif operation == "-":
        if num1 >= num2:
            return {"result":num1-num2}
        else:
            return {"result":num2-num1}
    elif operation == "*":
        return {"result":num1*num2}
    elif operation == "div":
        return {"result":num1/num2}
    elif operation == "%":
        return {"remainder is:":num1%num2}
if __name__ == "__main__":
    app.run(port=5555,debug=True)