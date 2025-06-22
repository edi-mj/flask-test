from flask import Flask, render_template, jsonify
import numpy as np
import skfuzzy
from skfuzzy import control as ctrl

app = Flask(__name__)

# ===================================================================
# BAGIAN 1: Definisi Sistem Fuzzy Anda (sama seperti kode Anda)
# ===================================================================

# Variabel Input (Antecedents)
luas_rumah = ctrl.Antecedent(np.arange(0, 251, 1), 'luas_rumah')
daya_listrik = ctrl.Antecedent(np.arange(0, 2201, 1), 'daya_listrik')
perlengkapan_elektronik = ctrl.Antecedent(np.arange(0, 19, 1), 'perlengkapan_elektronik')
pendapatan_ekonomi = ctrl.Antecedent(np.arange(0, 10.5, 0.5), 'pendapatan_ekonomi')

# Variabel Output (Consequent)
biaya_pemakaian = ctrl.Consequent(np.arange(0, 1201, 1), 'biaya_pemakaian')

# Fungsi Keanggotaan untuk luas_rumah
luas_rumah['standard'] = skfuzzy.trapmf(luas_rumah.universe, [0, 0, 15, 55])
luas_rumah['medium'] = skfuzzy.trimf(luas_rumah.universe, [40, 80, 120])
luas_rumah['besar'] = skfuzzy.trapmf(luas_rumah.universe, [105, 145, 250, 250])

# Fungsi Keanggotaan untuk daya_listrik
daya_listrik['rendah'] = skfuzzy.trapmf(daya_listrik.universe, [0, 0, 400, 900])
daya_listrik['sedang'] = skfuzzy.trimf(daya_listrik.universe, [400, 900, 1400])
daya_listrik['tinggi'] = skfuzzy.trapmf(daya_listrik.universe, [900, 1400, 2200, 2200])

# Fungsi Keanggotaan untuk perlengkapan_elektronik
perlengkapan_elektronik['sedikit'] = skfuzzy.trapmf(perlengkapan_elektronik.universe, [0, 0, 5, 7])
perlengkapan_elektronik['normal'] = skfuzzy.trimf(perlengkapan_elektronik.universe, [5, 9, 13])
perlengkapan_elektronik['banyak'] = skfuzzy.trapmf(perlengkapan_elektronik.universe, [11, 13, 18, 18])

# Fungsi Keanggotaan untuk pendapatan_ekonomi
pendapatan_ekonomi['rendah'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [0, 0, 1, 2.5])
pendapatan_ekonomi['sedang'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [2, 4, 4.5, 6.5])
pendapatan_ekonomi['tinggi'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [6, 7.5, 10, 10])

# Fungsi Keanggotaan untuk biaya_pemakaian
biaya_pemakaian['rendah'] = skfuzzy.trapmf(biaya_pemakaian.universe, [0, 0, 200, 300])
biaya_pemakaian['sedang'] = skfuzzy.trapmf(biaya_pemakaian.universe, [200, 300, 400, 500])
biaya_pemakaian['tinggi'] = skfuzzy.trapmf(biaya_pemakaian.universe, [400, 500, 1200, 1200])

# Simpan semua variabel dalam dictionary agar mudah diakses
fuzzy_variables = {
    'luas_rumah': luas_rumah,
    'daya_listrik': daya_listrik,
    'perlengkapan_elektronik': perlengkapan_elektronik,
    'pendapatan_ekonomi': pendapatan_ekonomi,
    'biaya_pemakaian': biaya_pemakaian
}

# ===================================================================
# BAGIAN 2: Fungsi dan Routing Flask
# ===================================================================

def generate_chart_data(variable_name):
    """
    Fungsi ini mengekstrak data dari objek fuzzy untuk Chart.js
    """
    variable = fuzzy_variables.get(variable_name)
    if not variable:
        return {}

    # Sumbu X adalah 'universe' dari variabel fuzzy
    labels = variable.universe.tolist()
    datasets = []
    
    # Warna untuk setiap kurva
    colors = ['rgb(255, 99, 132)', 'rgb(54, 162, 235)', 'rgb(255, 205, 86)']

    # Iterasi setiap term (e.g., 'rendah', 'sedang', 'tinggi')
    for i, (term_name, term_obj) in enumerate(variable.terms.items()):
        # Hitung nilai keanggotaan (sumbu Y) untuk setiap titik di universe
        y_values = skfuzzy.interp_membership(variable.universe, term_obj.mf, variable.universe)
        
        datasets.append({
            'label': term_name,
            'data': y_values.tolist(),
            'borderColor': colors[i % len(colors)],
            'fill': False,
            'tension': 0.1,
            'pointRadius': 0, # Sembunyikan titik agar menjadi garis murni
        })

    return {
        'labels': labels,
        'datasets': datasets,
        'title': f'Fungsi Keanggotaan untuk {variable.label.replace("_", " ").title()}'
    }


@app.route('/')
def index():
    """Merender halaman utama web."""
    # Kirim nama-nama variabel ke template
    variable_names = list(fuzzy_variables.keys())
    return render_template('index.html', variable_names=variable_names)


@app.route('/api/data/<variable_name>')
def get_data(variable_name):
    """API endpoint untuk menyediakan data plot."""
    data = generate_chart_data(variable_name)
    if not data:
        return jsonify({'error': 'Variable not found'}), 404
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)