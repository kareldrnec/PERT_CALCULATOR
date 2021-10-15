# pert calculator obdoba
from flask import Flask, render_template, request, redirect, flash
from flask_bootstrap import Bootstrap
from modules import pert_calc, data_parser

app = Flask(__name__)
app.secret_key = 'dont tell anyone'

Bootstrap(app)

headings = ("#", "Task Name", "Optimistic", "Most Likely", "Pessimistic", "Delete")
data_array = []
results_data = []
results = []


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', headings=headings, data_array=data_array, number_of_tasks=len(data_array),
                           results_data=results_data, results=results)


@app.route('/form', methods=["POST"])
def form():
    task_name = request.form.get("task")
    optimistic = request.form.get("optimistic")
    most_likely = request.form.get("mostLikely")
    pessimistic = request.form.get("pessimistic")
    data = data_parser.parse_to_json(task_name, optimistic, most_likely, pessimistic)
    data_array.append(data)
    return redirect("/")


@app.route('/about/')
def hello():
    return 'About page'


@app.route('/calculate', methods=["POST"])
def calculate():
    desired_time = request.form.get("desiredTime")
    if len(data_array) == 0:
        flash("No data to calculate!")
    else:
        results_data.clear()
        results.clear()
        x, y = pert_calc.calculate_pert(data_array, desired_time)
        for _ in x:
            results_data.append(_)
        results.append(y)
        print(results)
    return redirect("/")


@app.route('/clear')
def clear():
    data_array.clear()
    results.clear()
    results_data.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(threaded=True, port=33507)
