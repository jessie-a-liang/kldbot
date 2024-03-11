from flask import Flask, render_template, request, redirect
from selectionslist import SelectionsList

app = Flask(__name__)
selectionsflask = SelectionsList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    selected_options = request.form.getlist('selection')
    for option in selected_options:
        selectionsflask.add_selection(option)
    return redirect('/saved')

@app.route('/saved')
def saved():
    selections = selectionsflask.get_selections()
    return render_template('saved.html', selections=selections)

if __name__ == '__main__':
    app.run(debug=True)
