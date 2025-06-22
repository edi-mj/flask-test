# # -*- coding: utf-8 -*-
# """
# ## **Linguistic Variable**
# Luas Rumah

# STANDAR [0 55]
# MEDIUM [40 120]
# BESAR [105 250]

# Daya Listrik

# RENDAH [0 900]
# SEDANG [450 1350]
# TINGGI [900 2200]

# Perlengkapan
# Elektronik

# SEDIKIT [1 7]
# NORMAL [5 13]
# BANYAK [11 18]

# Pendapatan
# Ekonomi

# RENDAH [0 2,5]
# SEDANG [2 6,5]
# TINGGI [6 10]


# Biaya
# Pemakaian Listrik

# RENDAH [0 300]
# SEDANG [200 500]
# TINGGI [400 1200]

# ## **Rules:**

# 1 	STANDAR 	RENDAH 	SEDIKIT 	RENDAH 	RENDAH

# 2 	STANDAR 	RENDAH 	SEDIKIT 	SEDANG 	RENDAH

# 3 	STANDAR 	RENDAH 	SEDIKIT 	TINGGI 	RENDAH

# 4 	STANDAR 	RENDAH 	NORMAL 	RENDAH 	RENDAH

# 5 	STANDAR 	RENDAH 	NORMAL 	SEDANG 	RENDAH

# 6 	STANDAR 	RENDAH 	NORMAL 	TINGGI 	SEDANG

# 7 	STANDAR 	RENDAH 	BANYAK 	RENDAH 	RENDAH

# 8 	STANDAR 	RENDAH 	BANYAK 	SEDANG 	SEDANG

# 9 	STANDAR 	RENDAH 	BANYAK 	TINGGI 	SEDANG

# 10 	MEDIUM 	MEDIUN 	BANYAK 	TINGGI 	SEDANG

# # Coding
# """

# !pip install -U scikit-fuzzy

# import numpy as np
# import skfuzzy
# import matplotlib.pyplot as plt
# from skfuzzy import control as ctrl

# """## Linguistic Variabel

# ### Range Masing-masing Variabel
# """

# luas_rumah = ctrl.Antecedent(np.arange(0, 250+1, 1), 'luas_rumah')
# daya_listrik = ctrl.Antecedent(np.arange(0, 2200+1, 1), 'daya_listrik')
# perlengkapan_elektronik = ctrl.Antecedent(np.arange(0, 18+1, 1), 'perlengkapan_elektronik')
# pendapatan_ekonomi = ctrl.Antecedent(np.arange(0, 10.5, 0.5), 'pendapatan_ekonomi')

# biaya_pemakaian = ctrl.Consequent(np.arange(0, 1200+1, 1), 'biaya_pemakaian')  # ribuan

# """### Himpunan Fuzzy"""

# # LINGUISTIC VARIABEL INPUT
# # luas_rumah
# luas_rumah['standard'] = skfuzzy.trapmf(luas_rumah.universe, [0, 0, 15, 55])
# luas_rumah['medium'] = skfuzzy.trimf(luas_rumah.universe, [40, 80, 120])
# luas_rumah['besar'] = skfuzzy.trapmf(luas_rumah.universe, [105, 145, 250, 250])

# # daya_listrik
# daya_listrik['rendah'] = skfuzzy.trapmf(daya_listrik.universe, [0, 0, 400, 900])
# daya_listrik['sedang'] = skfuzzy.trimf(daya_listrik.universe, [400, 900, 1400])
# daya_listrik['tinggi'] = skfuzzy.trapmf(daya_listrik.universe, [900, 1400, 2200, 2200])

# # perlengkapan_elektronik
# perlengkapan_elektronik['sedikit'] = skfuzzy.trapmf(perlengkapan_elektronik.universe, [0, 0, 5, 7])
# perlengkapan_elektronik['normal'] = skfuzzy.trimf(perlengkapan_elektronik.universe, [5, 9, 13])
# perlengkapan_elektronik['banyak'] = skfuzzy.trapmf(perlengkapan_elektronik.universe, [11, 13, 18, 18])

# # pendapatan_ekonomi
# pendapatan_ekonomi['rendah'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [0, 0, 1, 2.5])
# pendapatan_ekonomi['sedang'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [2, 4, 4.5, 6.5])
# pendapatan_ekonomi['tinggi'] = skfuzzy.trapmf(pendapatan_ekonomi.universe, [6, 7.5, 10, 10])

# # LINGUISTIC VARIABEL OUTPUT ->
# # biaya_pemakaian
# biaya_pemakaian['rendah'] = skfuzzy.trapmf(biaya_pemakaian.universe, [0, 0, 200, 300])
# biaya_pemakaian['sedang'] = skfuzzy.trapmf(biaya_pemakaian.universe, [200, 300, 400, 500])
# biaya_pemakaian['tinggi'] = skfuzzy.trapmf(biaya_pemakaian.universe, [400, 500, 1200, 1200])

# """### Display Himpunan Fuzzy"""

# luas_rumah.view()
# daya_listrik.view()
# perlengkapan_elektronik.view()
# pendapatan_ekonomi.view()
# biaya_pemakaian.view()

# """## Pembuatan Rules"""

# # No. | Luas Rumah | Daya Listrik | Perlengkapan Elektronik | Pendapatan Ekonomi | Biaya Pemakaian

# # 1.  STANDAR   RENDAH  SEDIKIT   RENDAH  RENDAH
# R1=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

# # 2.  STANDAR   RENDAH  SEDIKIT   SEDANG  RENDAH
# R2=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['rendah'])

# # 3.  STANDAR   RENDAH  SEDIKIT   TINGGI  RENDAH
# R3=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['rendah'])

# # 4.  STANDAR   RENDAH  NORMAL  RENDAH  RENDAH
# R4=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

# # 5.  STANDAR   RENDAH  NORMAL  SEDANG  RENDAH
# R5=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['rendah'])

# # 6.  STANDAR   RENDAH  NORMAL  TINGGI  SEDANG
# R6=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 7.  STANDAR   RENDAH  BANYAK  RENDAH  RENDAH
# R7=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

# # 8.  STANDAR   RENDAH  BANYAK  SEDANG  SEDANG
# R8=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 9.  STANDAR   RENDAH  BANYAK  TINGGI  SEDANG
# R9=ctrl.Rule(luas_rumah['standard']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 10.  STANDAR   SEDANG  SEDIKIT   RENDAH  RENDAH
# R10=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

# # 11.  STANDAR   SEDANG  SEDIKIT   SEDANG  RENDAH
# R11=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['rendah'])

# # 12.  STANDAR   SEDANG  SEDIKIT   TINGGI  SEDANG
# R12=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 13.  STANDAR   SEDANG  NORMAL  RENDAH  RENDAH
# R13=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

# # 14.  STANDAR   SEDANG  NORMAL  SEDANG  SEDANG
# R14=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 15.  STANDAR   SEDANG  NORMAL  TINGGI  SEDANG
# R15=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 16.  STANDAR   SEDANG  BANYAK  RENDAH  SEDANG
# R16=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 17.  STANDAR   SEDANG  BANYAK  SEDANG  SEDANG
# R17=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 18.  STANDAR   SEDANG  BANYAK  TINGGI  TINGGI
# R18=ctrl.Rule(luas_rumah['standard']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 19.  STANDAR   TINGGI  SEDIKIT   RENDAH  SEDANG
# R19=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 20.  STANDAR   TINGGI  SEDIKIT   SEDANG  SEDANG
# R20=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 21.  STANDAR   TINGGI  SEDIKIT   TINGGI  SEDANG
# R21=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 22.  STANDAR   TINGGI  NORMAL  RENDAH  SEDANG
# R22=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 23.  STANDAR   TINGGI  NORMAL  SEDANG  TINGGI
# R23=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 24.  STANDAR   TINGGI  NORMAL  TINGGI  TINGGI
# R24=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 25.  STANDAR   TINGGI  BANYAK  RENDAH  TINGGI
# R25=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

# # 26.  STANDAR   TINGGI  BANYAK  SEDANG  TINGGI
# R26=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 27.  STANDAR   TINGGI  BANYAK  TINGGI  TINGGI
# R27=ctrl.Rule(luas_rumah['standard']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 28.  MEDIUM   RENDAH  SEDIKIT   RENDAH  RENDAH
# R28=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

# # 29.  MEDIUM   RENDAH  SEDIKIT   SEDANG  RENDAH
# R29=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['rendah'])

# # 30.  MEDIUM   RENDAH  SEDIKIT   TINGGI  SEDANG
# R30=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 31.  MEDIUM   RENDAH  NORMAL  RENDAH  RENDAH
# R31=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

# # 32.  MEDIUM   RENDAH  NORMAL  SEDANG  SEDANG
# R32=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 33.  MEDIUM   RENDAH  NORMAL  TINGGI  SEDANG
# R33=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 34.  MEDIUM   RENDAH  BANYAK  RENDAH  SEDANG
# R34=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 35.  MEDIUM   RENDAH  BANYAK  SEDANG  SEDANG
# R35=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 36.  MEDIUM   RENDAH  BANYAK  TINGGI  TINGGI
# R36=ctrl.Rule(luas_rumah['medium']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 37.  MEDIUM   SEDANG  SEDIKIT   RENDAH  RENDAH
# R37=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['rendah'])

# # 38.  MEDIUM   SEDANG  SEDIKIT   SEDANG  SEDANG
# R38=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 39.  MEDIUM   SEDANG  SEDIKIT   TINGGI  SEDANG
# R39=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 40.  MEDIUM   SEDANG  NORMAL  RENDAH  SEDANG
# R40=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 41.  MEDIUM   SEDANG  NORMAL  SEDANG  SEDANG
# R41=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 42.  MEDIUM   SEDANG  NORMAL  TINGGI  TINGGI
# R42=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 43.  MEDIUM   SEDANG  BANYAK  RENDAH  SEDANG
# R43=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 44.  MEDIUM   SEDANG  BANYAK  SEDANG  TINGGI
# R44=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 45.  MEDIUM   SEDANG  BANYAK  TINGGI  TINGGI
# R45=ctrl.Rule(luas_rumah['medium']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 46.  MEDIUM   TINGGI  SEDIKIT   RENDAH  SEDANG
# R46=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 47.  MEDIUM   TINGGI  SEDIKIT   SEDANG  SEDANG
# R47=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 48.  MEDIUM   TINGGI  SEDIKIT   TINGGI  TINGGI
# R48=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 49.  MEDIUM   TINGGI  NORMAL  RENDAH  SEDANG
# R49=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 50.  MEDIUM   TINGGI  NORMAL  SEDANG  TINGGI
# R50=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 51.  MEDIUM   TINGGI  NORMAL  TINGGI  TINGGI
# R51=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 52.  MEDIUM   TINGGI  BANYAK  RENDAH  TINGGI
# R52=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

# # 53.  MEDIUM   TINGGI  BANYAK  SEDANG  TINGGI
# R53=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 54.  MEDIUM   TINGGI  BANYAK  TINGGI  TINGGI
# R54=ctrl.Rule(luas_rumah['medium']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 55.  BESAR   RENDAH  SEDIKIT   RENDAH  SEDANG
# R55=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 56.  BESAR   RENDAH  SEDIKIT   SEDANG  SEDANG
# R56=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 57.  BESAR   RENDAH  SEDIKIT   TINGGI  SEDANG
# R57=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['sedang'])

# # 58.  BESAR   RENDAH  NORMAL  RENDAH  SEDANG
# R58=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 59.  BESAR   RENDAH  NORMAL  SEDANG  SEDANG
# R59=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 60.  BESAR   RENDAH  NORMAL  TINGGI  TINGGI
# R60=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 61.  BESAR   RENDAH  BANYAK  RENDAH  SEDANG
# R61=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 62.  BESAR   RENDAH  BANYAK  SEDANG  TINGGI
# R62=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 63.  BESAR   RENDAH  BANYAK  TINGGI  TINGGI
# R63=ctrl.Rule(luas_rumah['besar']&daya_listrik['rendah']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 64.  BESAR   SEDANG  SEDIKIT   RENDAH  SEDANG
# R64=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 65.  BESAR   SEDANG  SEDIKIT   SEDANG  SEDANG
# R65=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['sedang'])

# # 66.  BESAR   SEDANG  SEDIKIT   TINGGI  TINGGI
# R66=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 67.  BESAR   SEDANG  NORMAL  RENDAH  SEDANG
# R67=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 68.  BESAR   SEDANG  NORMAL  SEDANG  TINGGI
# R68=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 69.  BESAR   SEDANG  NORMAL  TINGGI  TINGGI
# R69=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 70.  BESAR   SEDANG  BANYAK  RENDAH  TINGGI
# R70=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

# # 71.  BESAR   SEDANG  BANYAK  SEDANG  TINGGI
# R71=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 72.  BESAR   SEDANG  BANYAK  TINGGI  TINGGI
# R72=ctrl.Rule(luas_rumah['besar']&daya_listrik['sedang']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 73.  BESAR   TINGGI  SEDIKIT   RENDAH  SEDANG
# R73=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['rendah'], biaya_pemakaian['sedang'])

# # 74.  BESAR   TINGGI  SEDIKIT   SEDANG  TINGGI
# R74=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 75.  BESAR   TINGGI  SEDIKIT   TINGGI  TINGGI
# R75=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['sedikit']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 76.  BESAR   TINGGI  NORMAL  RENDAH  TINGGI
# R76=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

# # 77.  BESAR   TINGGI  NORMAL  SEDANG  TINGGI
# R77=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 78.  BESAR   TINGGI  NORMAL  TINGGI  TINGGI
# R78=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['normal']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# # 79.  BESAR   TINGGI  BANYAK  RENDAH  TINGGI
# R79=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['rendah'], biaya_pemakaian['tinggi'])

# # 80.  BESAR   TINGGI  BANYAK  SEDANG  TINGGI
# R80=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['sedang'], biaya_pemakaian['tinggi'])

# # 81.  BESAR   TINGGI  BANYAK  TINGGI  TINGGI
# R81=ctrl.Rule(luas_rumah['besar']&daya_listrik['tinggi']&perlengkapan_elektronik['banyak']&pendapatan_ekonomi['tinggi'], biaya_pemakaian['tinggi'])

# biaya_pemakaian_fuzzy=ctrl.ControlSystem([
#     R1, R2, R3, R4, R5, R6, R7, R8, R9,
#     R10, R11, R12, R13, R14, R15, R16, R17, R18,
#     R19, R20, R21, R22, R23, R24, R25, R26, R27,
#     R28, R29, R30, R31, R32, R33, R34, R35, R36,
#     R37, R38, R39, R40, R41, R42, R43, R44, R45,
#     R46, R47, R48, R49, R50, R51, R52, R53, R54,
#     R55, R56, R57, R58, R59, R60, R61, R62, R63,
#     R64, R65, R66, R67, R68, R69, R70, R71, R72,
#     R73, R74, R75, R76, R77, R78, R79, R80, R81
# ])
# biaya_pemakaian_fuzzy=ctrl.ControlSystemSimulation(biaya_pemakaian_fuzzy)

# """## Eksekusi Sistem

# ### Input Value
# """

# input_luas_rumah = 60
# input_daya_listrik = 1300
# input_perlengkapan_elektronik = 10
# input_pendapatan_ekonomi = 7

# biaya_pemakaian_fuzzy.input['luas_rumah']= input_luas_rumah
# biaya_pemakaian_fuzzy.input['daya_listrik']= input_daya_listrik
# biaya_pemakaian_fuzzy.input['perlengkapan_elektronik']= input_perlengkapan_elektronik
# biaya_pemakaian_fuzzy.input['pendapatan_ekonomi']= input_pendapatan_ekonomi

# """### Fuzzyfikasi"""

# # Fuzzyfikasi - Luas Rumah
# luas_rumah_standard = skfuzzy.interp_membership(luas_rumah.universe, luas_rumah['standard'].mf, input_luas_rumah)
# luas_rumah_medium = skfuzzy.interp_membership(luas_rumah.universe, luas_rumah['medium'].mf, input_luas_rumah)
# luas_rumah_besar = skfuzzy.interp_membership(luas_rumah.universe, luas_rumah['besar'].mf, input_luas_rumah)

# print(f'mu luas rumah standard = {luas_rumah_standard}')
# print(f'mu luas rumah medium = {luas_rumah_medium}')
# print(f'mu luas rumah besar = {luas_rumah_besar}')
# print("_"*22)

# # Fuzzyfikasi - Daya Listrik
# daya_listrik_rendah = skfuzzy.interp_membership(daya_listrik.universe, daya_listrik['rendah'].mf, input_daya_listrik)
# daya_listrik_sedang = skfuzzy.interp_membership(daya_listrik.universe, daya_listrik['sedang'].mf, input_daya_listrik)
# daya_listrik_tinggi = skfuzzy.interp_membership(daya_listrik.universe, daya_listrik['tinggi'].mf, input_daya_listrik)

# print(f'mu daya listrik rendah = {daya_listrik_rendah}')
# print(f'mu daya listrik sedang = {daya_listrik_sedang}')
# print(f'mu daya listrik tinggi = {daya_listrik_tinggi}')
# print("_"*22)

# # Fuzzyfikasi - Perlengkapan Elektronik
# perlengkapan_elektronik_sedikit = skfuzzy.interp_membership(perlengkapan_elektronik.universe, perlengkapan_elektronik['sedikit'].mf, input_perlengkapan_elektronik)
# perlengkapan_elektronik_normal = skfuzzy.interp_membership(perlengkapan_elektronik.universe, perlengkapan_elektronik['normal'].mf, input_perlengkapan_elektronik)
# perlengkapan_elektronik_banyak = skfuzzy.interp_membership(perlengkapan_elektronik.universe, perlengkapan_elektronik['banyak'].mf, input_perlengkapan_elektronik)

# print(f'mu perlengkapan elektronik sedikit = {perlengkapan_elektronik_sedikit}')
# print(f'mu perlengkapan elektronik normal = {perlengkapan_elektronik_normal}')
# print(f'mu perlengkapan elektronik banyak = {perlengkapan_elektronik_banyak}')
# print("_"*22)

# # pendapatan_ekonomi
# pendapatan_ekonomi_rendah=skfuzzy.interp_membership(pendapatan_ekonomi.universe, pendapatan_ekonomi['rendah'].mf, input_pendapatan_ekonomi)
# pendapatan_ekonomi_sedang=skfuzzy.interp_membership(pendapatan_ekonomi.universe, pendapatan_ekonomi['sedang'].mf, input_pendapatan_ekonomi)
# pendapatan_ekonomi_tinggi=skfuzzy.interp_membership(pendapatan_ekonomi.universe, pendapatan_ekonomi['tinggi'].mf, input_pendapatan_ekonomi)
# print(f'mu pendapatan ekonomi rendah={pendapatan_ekonomi_rendah}')
# print(f'mu pendapatan ekonomi sedang={pendapatan_ekonomi_sedang}')
# print(f'mu pendapatan ekonomi tinggi={pendapatan_ekonomi_tinggi}')
# print("_"*22)

# """### Inferencing"""

# r1 = min(luas_rumah_standard, daya_listrik_rendah,  perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)

# r2 = min(luas_rumah_standard, daya_listrik_rendah,  perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)

# r3 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)

# r4 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)

# r5 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)

# r6 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)

# r7 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)

# r8 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)

# r9 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# r10 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)


# r11 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)

# print(f'R1: {r1}')
# print(f'R2: {r2}')
# print(f'R3: {r3}')
# print(f'R4: {r4}')
# print(f'R5: {r5}')
# print(f'R6: {r6}')
# print(f'R7: {r7}')
# print(f'R8: {r8}')
# print(f'R9: {r9}')
# print(f'R10: {r10}')
# print(f'R11: {r11}')

# # Luas Rumah: STANDAR, Daya Listrik: RENDAH
# r1 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r2 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r3 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r4 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r5 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r6 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r7 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r8 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r9 = min(luas_rumah_standard, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # Luas Rumah: STANDAR, Daya Listrik: SEDANG
# r10 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r11 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r12 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r13 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r14 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r15 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r16 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r17 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r18 = min(luas_rumah_standard, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # Luas Rumah: STANDAR, Daya Listrik: TINGGI
# r19 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r20 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r21 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r22 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r23 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r24 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r25 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r26 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r27 = min(luas_rumah_standard, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # Luas Rumah: MEDIUM, Daya Listrik: RENDAH
# r28 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r29 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r30 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r31 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r32 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r33 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r34 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r35 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r36 = min(luas_rumah_medium, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # Luas Rumah: MEDIUM, Daya Listrik: SEDANG
# r37 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r38 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r39 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r40 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r41 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r42 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r43 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r44 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r45 = min(luas_rumah_medium, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # Luas Rumah: MEDIUM, Daya Listrik: TINGGI
# r46 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r47 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r48 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r49 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r50 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r51 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r52 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r53 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r54 = min(luas_rumah_medium, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # Luas Rumah: BESAR, Daya Listrik: RENDAH
# r55 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r56 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r57 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r58 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r59 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r60 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r61 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r62 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r63 = min(luas_rumah_besar, daya_listrik_rendah, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # Luas Rumah: BESAR, Daya Listrik: SEDANG
# r64 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r65 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r66 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r67 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r68 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r69 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r70 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r71 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r72 = min(luas_rumah_besar, daya_listrik_sedang, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # Luas Rumah: BESAR, Daya Listrik: TINGGI
# r73 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_rendah)
# r74 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_sedang)
# r75 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_sedikit, pendapatan_ekonomi_tinggi)
# r76 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_rendah)
# r77 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_sedang)
# r78 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_normal, pendapatan_ekonomi_tinggi)
# r79 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_rendah)
# r80 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_sedang)
# r81 = min(luas_rumah_besar, daya_listrik_tinggi, perlengkapan_elektronik_banyak, pendapatan_ekonomi_tinggi)

# # ---
# # Mencetak hasil inferensi untuk setiap aturan (jika variabel input sudah memiliki nilai numerik)

# print(f'R1: {r1}')
# print(f'R2: {r2}')
# print(f'R3: {r3}')
# print(f'R4: {r4}')
# print(f'R5: {r5}')
# print(f'R6: {r6}')
# print(f'R7: {r7}')
# print(f'R8: {r8}')
# print(f'R9: {r9}')
# print(f'R10: {r10}')
# print(f'R11: {r11}')
# print(f'R12: {r12}')
# print(f'R13: {r13}')
# print(f'R14: {r14}')
# print(f'R15: {r15}')
# print(f'R16: {r16}')
# print(f'R17: {r17}')
# print(f'R18: {r18}')
# print(f'R19: {r19}')
# print(f'R20: {r20}')
# print(f'R21: {r21}')
# print(f'R22: {r22}')
# print(f'R23: {r23}')
# print(f'R24: {r24}')
# print(f'R25: {r25}')
# print(f'R26: {r26}')
# print(f'R27: {r27}')
# print(f'R28: {r28}')
# print(f'R29: {r29}')
# print(f'R30: {r30}')
# print(f'R31: {r31}')
# print(f'R32: {r32}')
# print(f'R33: {r33}')
# print(f'R34: {r34}')
# print(f'R35: {r35}')
# print(f'R36: {r36}')
# print(f'R37: {r37}')
# print(f'R38: {r38}')
# print(f'R39: {r39}')
# print(f'R40: {r40}')
# print(f'R41: {r41}')
# print(f'R42: {r42}')
# print(f'R43: {r43}')
# print(f'R44: {r44}')
# print(f'R45: {r45}')
# print(f'R46: {r46}')
# print(f'R47: {r47}')
# print(f'R48: {r48}')
# print(f'R49: {r49}')
# print(f'R50: {r50}')
# print(f'R51: {r51}')
# print(f'R52: {r52}')
# print(f'R53: {r53}')
# print(f'R54: {r54}')
# print(f'R55: {r55}')
# print(f'R56: {r56}')
# print(f'R57: {r57}')
# print(f'R58: {r58}')
# print(f'R59: {r59}')
# print(f'R60: {r60}')
# print(f'R61: {r61}')
# print(f'R62: {r62}')
# print(f'R63: {r63}')
# print(f'R64: {r64}')
# print(f'R65: {r65}')
# print(f'R66: {r66}')
# print(f'R67: {r67}')
# print(f'R68: {r68}')
# print(f'R69: {r69}')
# print(f'R70: {r70}')
# print(f'R71: {r71}')
# print(f'R72: {r72}')
# print(f'R73: {r73}')
# print(f'R74: {r74}')
# print(f'R75: {r75}')
# print(f'R76: {r76}')
# print(f'R77: {r77}')
# print(f'R78: {r78}')
# print(f'R79: {r79}')
# print(f'R80: {r80}')
# print(f'R81: {r81}')

# """### Defuzzyfikasi"""

# biaya_pemakaian_fuzzy.compute()
# print(f"{biaya_pemakaian_fuzzy.output['biaya_pemakaian']:.2f}")
# print("Defuzzyfikasi pembulatan: ", round(biaya_pemakaian_fuzzy.output['biaya_pemakaian']))
# biaya_pemakaian.view(sim=biaya_pemakaian_fuzzy)