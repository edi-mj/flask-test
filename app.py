from flask import Flask, render_template, request, jsonify
import numpy as np
import skfuzzy
from skfuzzy import control as ctrl

app = Flask(__name__)

# --------------------------------------------
# DEFINISI VARIABLE DAN KEANGGOTAAN
# --------------------------------------------
luas_rumah = ctrl.Antecedent(np.arange(0, 251, 1), 'luas_rumah')
daya_listrik = ctrl.Antecedent(np.arange(0, 2201, 1), 'daya_listrik')
perlengkapan_elektronik = ctrl.Antecedent(np.arange(0, 19, 1), 'perlengkapan_elektronik')
pendapatan_ekonomi = ctrl.Antecedent(np.arange(0, 10.5, 0.5), 'pendapatan_ekonomi')
biaya_pemakaian = ctrl.Consequent(np.arange(0, 1201, 1), 'biaya_pemakaian')

# Fungsi keanggotaan input
luas_rumah['standard'] = skfuzzy.trapmf(luas_rumah.universe, [0, 0, 15, 55])
luas_rumah['medium'] = skfuzzy.trimf(luas_rumah.universe, [40, 80, 120])
luas_rumah['besar'] = skfuzzy.trapmf(luas_rumah.universe, [105, 145, 250, 250])

daya_listrik['rendah'] = skfuzzy.trapmf(daya_listrik.universe, [0, 0, 400, 900])
daya_listrik['sedang'] = skfuzzy.trimf(daya_listrik.universe, [400, 900, 1400])
daya_listrik['tinggi'] = skfuzzy.trapmf(daya_listrik.universe, [900, 1400, 2200, 2200])

perlengkapan_elektronik['sedikit'] = skfuzzy.trapmf(perlengkapan_elektronik.universe, [0, 0, 5, 7])
perlengkapan_elektronik['normal'] = skfuzzy.trimf(perlengkapan_elektronik.universe, [5, 9, 13])
perlengkapan_elektronik['banyak'] = skfuzzy.trapmf(perlengkapan_elektronik.universe, [11, 13, 18, 18])

pendapatan_ekonomi['rendah'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [0, 0, 1, 2.5])
pendapatan_ekonomi['sedang'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [2, 4, 4.5, 6.5])
pendapatan_ekonomi['tinggi'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [6, 7.5, 10, 10])

biaya_pemakaian['rendah'] = skfuzzy.trapmf(biaya_pemakaian.universe, [0, 0, 200, 300])
biaya_pemakaian['sedang'] = skfuzzy.trapmf(biaya_pemakaian.universe, [200, 300, 400, 500])
biaya_pemakaian['tinggi'] = skfuzzy.trapmf(biaya_pemakaian.universe, [400, 500, 1200, 1200])

# Simpan semua variabel
fuzzy_variables = {
    'luas_rumah': luas_rumah,
    'daya_listrik': daya_listrik,
    'perlengkapan_elektronik': perlengkapan_elektronik,
    'pendapatan_ekonomi': pendapatan_ekonomi,
    'biaya_pemakaian': biaya_pemakaian
}

# --------------------------------------------
# RULE INFERENSI OTOMATIS 81 KOMBINASI
# --------------------------------------------
# --------------------------------------------
# RULE INFERENSI OTOMATIS BERDASARKAN ATURAN USER
# --------------------------------------------

rules = []
terms_luas = ['standard', 'medium', 'besar']
terms_daya = ['rendah', 'sedang', 'tinggi']
terms_alat = ['sedikit', 'normal', 'banyak']
terms_pendapatan = ['rendah', 'sedang', 'tinggi']

# List hasil sesuai urutan yang Anda berikan (total 81 elemen)
hasil_list = [
    # standard
    'rendah','rendah','rendah','rendah','rendah','sedang','rendah','sedang','sedang',
    'rendah','rendah','sedang','rendah','sedang','sedang','sedang','sedang','tinggi',
    'sedang','sedang','sedang','sedang','tinggi','tinggi','tinggi','tinggi','tinggi',
    # medium
    'rendah','rendah','sedang','rendah','sedang','sedang','sedang','sedang','tinggi',
    'rendah','sedang','sedang','sedang','sedang','tinggi','sedang','tinggi','tinggi',
    'tinggi','tinggi','tinggi','tinggi','tinggi','tinggi','tinggi','tinggi','tinggi',
    # besar
    'sedang','sedang','sedang','sedang','sedang','tinggi','sedang','tinggi','tinggi',
    'sedang','sedang','tinggi','sedang','tinggi','tinggi','tinggi','tinggi','tinggi',
    'tinggi','tinggi','tinggi','tinggi','tinggi','tinggi','tinggi','tinggi','tinggi'
]

index = 0
for l in terms_luas:
    for d in terms_daya:
        for a in terms_alat:
            for p in terms_pendapatan:
                hasil = hasil_list[index]
                rule = ctrl.Rule(
                    luas_rumah[l] & daya_listrik[d] & perlengkapan_elektronik[a] & pendapatan_ekonomi[p],
                    biaya_pemakaian[hasil]
                )
                rules.append(rule)
                index += 1


# --------------------------------------------
# SISTEM KONTROL FUZZY
# --------------------------------------------
fuzzy_ctrl = ctrl.ControlSystem(rules)
fuzzy_simulasi = ctrl.ControlSystemSimulation(fuzzy_ctrl)

# --------------------------------------------
# ROUTING UTAMA
# --------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    hasil_biaya = None

    if request.method == 'POST':
        luas = float(request.form['luas'])
        daya = float(request.form['daya'])
        alat = float(request.form['alat'])
        pendapatan = float(request.form['pendapatan'])

        fuzzy_simulasi.input['luas_rumah'] = luas
        fuzzy_simulasi.input['daya_listrik'] = daya
        fuzzy_simulasi.input['perlengkapan_elektronik'] = alat
        fuzzy_simulasi.input['pendapatan_ekonomi'] = pendapatan

        fuzzy_simulasi.compute()

        hasil = fuzzy_simulasi.output['biaya_pemakaian']
        hasil_biaya = f"Rp {hasil:,.0f}".replace(",", ".")

    return render_template('index.html', hasil_biaya=hasil_biaya, variable_names=list(fuzzy_variables.keys()))

# --------------------------------------------
# API UNTUK DATA VISUALISASI
# --------------------------------------------
@app.route('/api/data/<variable_name>')
def get_data(variable_name):
    variable = fuzzy_variables.get(variable_name)
    if not variable:
        return jsonify({'error': 'Variable not found'}), 404

    labels = variable.universe.tolist()
    datasets = []

    colors = ['#ef4444', '#10b981', '#3b82f6', '#a855f7']

    for i, (term_name, term_obj) in enumerate(variable.terms.items()):
        y_values = skfuzzy.interp_membership(variable.universe, term_obj.mf, variable.universe)
        datasets.append({
            'label': term_name,
            'data': y_values.tolist(),
            'borderColor': colors[i % len(colors)],
            'fill': False,
            'tension': 0.3,
            'pointRadius': 0
        })

    return jsonify({
        'labels': labels,
        'datasets': datasets,
        'title': f'Fungsi Keanggotaan untuk {variable.label.replace("_", " ").title()}'
    })

if __name__ == '__main__':
    app.run(debug=True)