from flask import Flask, render_template, request
import pickle

dic_model = pickle.load(open('dic_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('template.html')

@app.route('/predict', methods=['POST'])
def predict():
    Diagnosed_Condition = request.form['Diagnosed_Condition']
    Patient_Body_Mass_Index = request.form['Patient_Body_Mass_Index']
    DX6 = request.form['DX6']
    Patient_Smoker = request.form['Patient_Smoker']
    Patient_Age = request.form['Patient_Age']
    Risk_Index = request.form['Risk_Index']
    Patient_Rural_Urban = request.form['Patient_Rural_Urban']
    DX1 = request.form['DX1']
    DX5 = request.form['DX5']
    D = request.form['D']
    DX3 = request.form['DX3']
    A = request.form['A']
    DX4 = request.form['DX4']
    DX2 = request.form['DX2']
    C = request.form['C']
    B = request.form['B']
    Number_of_prev_cond = request.form['Number_of_prev_cond']

    dict_ft = {'Diagnosed_Condition': Diagnosed_Condition,
               'Patient_Body_Mass_Index': Patient_Body_Mass_Index,
               'DX6': DX6,
               'Patient_Smoker': Patient_Smoker,
               'Patient_Age': Patient_Age,
               'Risk_Index': Risk_Index,
               'Patient_Rural_Urban': Patient_Rural_Urban,
               'DX1': DX1,
               'DX5': DX5,
               'D': D,
               'DX3': DX3,
               'A': A,
               'DX4': DX4,
               'DX2': DX2,
               'C': C,
               'B': B,
               'Number_of_prev_cond': Number_of_prev_cond
               }

    list_ft = []
    list_vl = []
    cb_ft = ['Diagnosed_Condition', 'Patient_Body_Mass_Index', 'DX6',
       'Patient_Smoker', 'Patient_Age', 'Risk_Index', 'Patient_Rural_Urban',
       'DX1', 'DX5', 'D', 'DX3', 'A', 'DX4', 'DX2', 'C', 'B',
       'Number_of_prev_cond']
    for key, value in dict_ft.items():
        if value != '':
            list_ft.append(key)
            list_vl.append(value)
    if list_ft == []:
        out = "[Error] Have not entered data!"

    elif list_ft not in [list(cb_ft[0:i]) for i in range(1, len(cb_ft) + 1)]:
        out = '[Error] Wrong input format!'
    else:
        X = [list_vl]
        model = dic_model[str(list_ft)]
        y_pred = model.predict(X)[0]
        if y_pred == 0:
            out = '[Success] Survived_1_year = 0. This patient has a high risk of death. Special attention and care are required for this patient.'
        else:
            out = '[Success] Survived_1_year = 1. This patient is likely to survive after 1 year of treatment.'
    return render_template('template.html', data=out)

if __name__ == "__main__":
    app.run(debug=True)