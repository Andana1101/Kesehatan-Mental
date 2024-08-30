import flask
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import io
import os
import base64

# Use pickle to load in the pre-trained model.
with open(f'model\Random Forest.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
        return flask.render_template('main.html')
    
@app.route('/result', methods=['GET', 'POST'])
def mainResult():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html')) #homepage is loaded

    if flask.request.method == 'POST':
        q1 = flask.request.form['q1']
        q2 = flask.request.form['q2']
        q3 = flask.request.form['q3']
        q4 = flask.request.form['q4']
        q5 = flask.request.form['q5']
        q6 = flask.request.form['q6']
        q7 = flask.request.form['q7']
        q8 = flask.request.form['q8']
        q9 = flask.request.form['q9']
        q10 = flask.request.form['q10']
        q11 = flask.request.form['q11']
        q12 = flask.request.form['q12']
        q13 = flask.request.form['q13']
        q14 = flask.request.form['q14']
        q15 = flask.request.form['q15']
        q16 = flask.request.form['q16']
        q17 = flask.request.form['q17']
        q18 = flask.request.form['q18']
        q19 = flask.request.form['q19']
        q20 = flask.request.form['q20']
        q21 = flask.request.form['q21']
        q22 = flask.request.form['q22']
        q23 = flask.request.form['q23']
        q24 = flask.request.form['q24']
        q25 = flask.request.form['q25']
        q26 = flask.request.form['q26']
        q27 = flask.request.form['q27']
        q28 = flask.request.form['q28']
        q29 = flask.request.form['q29']
        q30 = flask.request.form['q30']
        q31 = flask.request.form['q31']
        q32 = flask.request.form['q32']
        q33 = flask.request.form['q33']
        q34 = flask.request.form['q34']
        q35 = flask.request.form['q35']
        q36 = flask.request.form['q36']
        q37 = flask.request.form['q37']
        q38 = flask.request.form['q38']
        q39 = flask.request.form['q39']
        q40 = flask.request.form['q40']
        q41 = flask.request.form['q41']
        q42 = flask.request.form['q42']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, 
                                         q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28,
                                         q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42]],
                                      columns = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14',
                                                 'q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28',
                                                 'q29','q30','q31','q32','q33','q34','q35','q36','q37','q38','q39','q40','q41','q42'], 
                                      dtype=float,
                                      index=['input'])
        
        #Mengubah data float menjadi integer agar dapat digunakan untuk plot grafik
        #Kategori Depresi
        q1 = int(flask.request.form['q1'])
        q2 = int(flask.request.form['q2'])
        q3 = int(flask.request.form['q3'])
        q4 = int(flask.request.form['q4'])
        q5 = int(flask.request.form['q5'])
        q6 = int(flask.request.form['q6'])
        q7 = int(flask.request.form['q7'])
        q8 = int(flask.request.form['q8'])
        q9 = int(flask.request.form['q9'])
        q10 = int(flask.request.form['q10'])
        q11 = int(flask.request.form['q11'])
        q12 = int(flask.request.form['q12'])
        q13 = int(flask.request.form['q13'])
        q14 = int(flask.request.form['q14'])

        #Kategori Kecemasan
        q15 = int(flask.request.form['q15'])
        q16 = int(flask.request.form['q16'])
        q17 = int(flask.request.form['q17'])
        q18 = int(flask.request.form['q18'])
        q19 = int(flask.request.form['q19'])
        q20 = int(flask.request.form['q20'])
        q21 = int(flask.request.form['q21'])
        q22 = int(flask.request.form['q22'])
        q23 = int(flask.request.form['q23'])
        q24 = int(flask.request.form['q24'])
        q25 = int(flask.request.form['q25'])
        q26 = int(flask.request.form['q26'])
        q27 = int(flask.request.form['q27'])
        q28 = int(flask.request.form['q28'])

        #Kategori Stress
        q29 = int(flask.request.form['q29'])
        q30 = int(flask.request.form['q30'])
        q31 = int(flask.request.form['q31'])
        q32 = int(flask.request.form['q32'])
        q33 = int(flask.request.form['q33'])
        q34 = int(flask.request.form['q34'])
        q35 = int(flask.request.form['q35'])
        q36 = int(flask.request.form['q36'])
        q37 = int(flask.request.form['q37'])
        q38 = int(flask.request.form['q38'])
        q39 = int(flask.request.form['q39'])
        q40 = int(flask.request.form['q40'])
        q41 = int(flask.request.form['q41'])
        q42 = int(flask.request.form['q42'])

        variables = ['Depresi', 'Kecemasan', 'Stress']
        depr = int( q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10 + q11 + q12 + q13 + q14 )
        anx = int ( q15 + q16 + q17 + q18 + q19 + q20 + q21 + q22 + q23 + q24 + q25 + q26 + q27 + q28 )
        stre = int ( q29 + q30 + q31 + q32 + q33 + q34 + q35 + q36 + q37 + q38 + q39 + q40 + q41 + q42 )
        
        print("Tingkat Nilai Depresi = ", depr)
        print("Tingkat Nilai Kecemasan = ", anx)
        print("Tingkat Nilai Stress = ", stre)
        values = [depr, anx, stre]  # Nilai contoh untuk k1, k2, k3

        # Membuat bar horizontal
        plt.figure(figsize=(10, 4))
        plt.barh(variables, values, color=['Blue', 'green', 'Black'])
        plt.xlabel('Values')
        plt.ylabel('Variables')
        plt.title('Grafik Bar Chart Untuk Depresi, Kecemasan, Stress')

        # Tentukan lokasi dan nama file
        image_path = os.path.join('static', 'images', 'chart.png')
        
        # Buat folder jika belum ada
        os.makedirs(os.path.dirname(image_path), exist_ok=True)

        # Simpan gambar di lokasi tertentu
        plt.savefig(image_path)
        plt.close()

        # Get the model's prediction
        # Get the model's prediction
        prediction = model.predict(input_variables)[0]

        if prediction <= 30: 
            guess = "Normal"
        elif prediction <= 73: 
            guess = "Ringan"
        elif prediction <= 102: 
            guess = "Sedang"
        elif prediction <= 141: 
            guess = "Parah"
        elif prediction >= 141: 
            guess = "Sangat Parah"

        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('result.html',
                                     original_input={},
                                     result=guess,
                                     chart_image=image_path
                                     )
                                
if __name__ == '__main__':
    app.run(debug=True)