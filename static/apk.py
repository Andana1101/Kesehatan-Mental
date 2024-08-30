import flask
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import os

# Use pickle to load in the pre-trained model.
with open(f'model/Random Forest.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    return flask.render_template('main.html')

@app.route('/result', methods=['GET', 'POST'])
def mainResult():
    if flask.request.method == 'GET':
        return flask.render_template('main.html') #homepage is loaded

    if flask.request.method == 'POST':
        # Retrieve form inputs
        inputs = [int(flask.request.form[f'q{i}']) for i in range(1, 43)]

        # Prepare DataFrame for model prediction
        input_variables = pd.DataFrame([inputs],
                                       columns=[f'q{i}' for i in range(1, 43)], 
                                       dtype=float,
                                       index=['input'])
        
        # Calculate scores for each category
        depr = sum(inputs[0:14])
        anx = sum(inputs[14:28])
        stre = sum(inputs[28:42])
        
        print("Tingkat Nilai Depresi = ", depr)
        print("Tingkat Nilai Kecemasan = ", anx)
        print("Tingkat Nilai Stress = ", stre)
        
        variables = ['Stress', 'Kecemasan', 'Depresi']
        values = [stre, anx, depr]

        # Generate horizontal bar chart
        plt.figure(figsize=(9, 4))
        bars = plt.barh(variables, values, color=['blue', 'green', 'black'])
        plt.xlabel('Values')
        plt.ylabel('Variables')
        plt.title('Grafik Bar Chart Untuk Depresi, Kecemasan, Stress')

        # Menambahkan nilai di ujung setiap batang
        for bar in bars:
            plt.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
                     f'{bar.get_width()}', va='center', ha='left')

        # Save the image
        image_path = os.path.join('static', 'images', 'chart.png')
        os.makedirs(os.path.dirname(image_path), exist_ok=True)
        plt.savefig(image_path)
        plt.close()

        # Adjust prediction based on DASS (42) scoring
        if depr <= 9:
            dep_category = "Normal"
        elif 10 <= depr <= 13:
            dep_category = "Ringan"
        elif 14 <= depr <= 20:
            dep_category = "Sedang"
        elif 21 <= depr <= 27:
            dep_category = "Parah"
        elif depr >= 28:
            dep_category = "Sangat Parah"

        if anx <= 7:
            anx_category = "Normal"
        elif 8 <= anx <= 9:
            anx_category = "Ringan"
        elif 10 <= anx <= 14:
            anx_category = "Sedang"
        elif 15 <= anx <= 19:
            anx_category = "Parah"
        elif anx >= 20:
            anx_category = "Sangat Parah"

        if stre <= 14:
            stre_category = "Normal"
        elif 15 <= stre <= 18:
            stre_category = "Ringan"
        elif 19 <= stre <= 25:
            stre_category = "Sedang"
        elif 26 <= stre <= 33:
            stre_category = "Parah"
        elif stre >= 34:
            stre_category = "Sangat Parah"

        # Include the calculated values and categories in the result
        guess = f"Depresi: {dep_category} (Nilai: {depr}), Kecemasan: {anx_category} (Nilai: {anx}), Stress: {stre_category} (Nilai: {stre})"

        # Render the result page with predictions and chart image
        return flask.render_template('result.html',
                                     original_input={},
                                     result=guess,
                                     chart_image=image_path)

if __name__ == '__main__':
    app.run(debug=True)