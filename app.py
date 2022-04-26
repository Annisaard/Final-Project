from flask import Flask
from flask import render_template, url_for, request, redirect, session, flash
import csv
from joblib import load
import numpy as np
import os
from test_dass import DASS
import logging
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret"
nb_model = load('model.joblib')

questions = {}
questions['D_score'] = 0
questions['A_score'] = 0
questions['S_score'] = 0
questions['current_q'] = 1
questions['nama'] = ""

dass = DASS()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hasiltest"
    )

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/info' , methods=['POST', 'GET'])
def info():
    ip_addr = request.remote_addr
    if request.method == 'POST':
        answer = request.form.get('username')
        if not answer:
            flash('Jangan Lupa Isi Nama ', 'error')
        else:
            print(answer)
            #print(ip_addr)
            ketemu = False
            mycursor = mydb.cursor()

            sql = "SELECT * from user"

            mycursor.execute(sql)
            # get all records
            records = mycursor.fetchall()
            #print(records)
            mycursor.close()
            for find in records:
                if ip_addr == find[0] and find[6]==0:
                    if not find[7] or answer != find[7]:
                        ReplaceSql(ip_addr,answer)
                    ketemu = True
                
            if not ketemu :
                insertsql(ip_addr,answer)

            return redirect(url_for('test'))
    return render_template('info.html',ip_addr=ip_addr)

@app.route('/hasil', methods=['GET'])
def hasil():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.environ['REMOTE_ADDR'])
    final_features = np.array([questions['D_score'],  questions['A_score'], questions['S_score']])
    prediction = nb_model.predict([final_features])
    if prediction[0] == 'A':
        prediction = 'Jaga Kesehatan Mental'
        explain = 'Tetap jaga Kesehatan mental kamu dan hindari hal yang membuat depressi,anxiety atau stress. '
    elif prediction[0] == 'AB':
        prediction = 'Jaga Kesehatan Mental dan Nutrisi Makanan'
        explain = 'Makan dengan baik penting untuk kesehatan fisik dan mental kamu. Jaga pola makan serta makan-makanan yg sehat dan bergizi seperti alpukat, oatmeal, sayuran, atau dark cokelat.'
    elif prediction[0] == 'AC':
        prediction = 'Jaga Kesehatan Mental dan Olahraga'
        explain = 'Dengan berolahraga teratur dapat mengurangi tingkat distres kamu, cukup dengan berjalan kaki, melakukan aktivitasi aerobik setiap hari selama 30 hingga 60 menit.'
    elif prediction[0] == 'AD':
        prediction = 'Jaga Kesehatan Mental dan Tidur yang Cukup'
        explain = 'Kurang tidur memiliki efek negatif yang signifikan pada suasana hati. Cobalah atur jam tidur kamu dan jangan sering bergadang.'
    elif prediction[0] == 'AE':
        prediction = 'Jaga Kesehatan Mental dan Kegiatan yang menyenangkan'
        explain = 'Luangkan waktu kamu untuk kegiatan santai seperti healing di tempat bernuansa alam, menonton komedi, memasak atau bermain game.'
    elif prediction[0] == 'AF':
        prediction = 'Jaga Kesehatan Mental dan Journaling'
        explain = 'Journaling/menulis buku harian  adalah cara yang tepat untuk lebih mengenal diri sendiri dengan mengungkapkan ketakutan, pikiran, dan perasaan yang terdalam. Melakukan journaling secara rutin dapat membantu kamu merasakan keteraturan di dalam hidup'
    elif prediction[0] == 'AG':
        prediction = 'Jaga Kesehatan Mental dan Yoga'
        explain = 'Dengan memfokuskan pikiran kamu pada gerakan dan pernapasan, yoga akan membantu kamu menjernihkan pikiran dan membuat kamu lebih relax'
    elif prediction[0] == 'AH':
        prediction = 'Jaga Kesehatan Mental dan Meditasi'
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu'
    elif prediction[0] == 'AI':
        prediction = 'Jaga Kesehatan Mental dan Art Terapi'
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat'
    elif prediction[0] == 'AL':
        prediction = 'Jaga Kesehatan Mental dan Terapi Musik'
        explain = 'Dengan mendengarkan musik klasik atau bernyanyi bersama dengan musik dapat membantu kamu menjadi lebih relax dan tenang.'
    elif prediction[0] == 'AM':
        prediction = 'Jaga Kesehatan Mental dan Menggunakan Aroma therapy'
        explain = 'Menggunakan aroma therapy saat tidur seperti esensial oil dapat membantu menenangkan pikiran kamu'
    elif prediction[0] == 'AN':
        prediction = 'Jaga Kesehatan Mental dan Manajemen waktu dengan baik'
        explain = 'Manajemen waktu yang baik dapat mengurangi distress kamu dan jangan terlalu memaksakan diri terhadap aktivitas yang terlalu banyak. '
    elif prediction[0] == 'AO':
        prediction = 'Jaga Kesehatan Mental dan Gaya Hidup sehat'
        explain = 'Pola hidup yang sehat, Makan makanan yang sehat, kurangi kafein dan gula, Hindari alkohol, rokok, dan obat-obatan '
    elif prediction[0] == 'HA':
        prediction = 'Meditasi dan Jaga Kesehatan Mental  '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu. '
    elif prediction[0] == 'HB   ':
        prediction = 'Meditasi dan Nutrisi Makanan '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu serta jangan lupa diimbangi dengan makan-makanan yang bergizi'
    elif prediction[0] == 'HC':
        prediction = 'Meditasi dan Olahraga  '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu serta jangan lupa berolahraga 30 sampai 60 menit. '
    elif prediction[0] == 'HD':
        prediction = 'Meditasi dan Tidur yang cukup  '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu dan tidur yang cukup.'
    elif prediction[0] == 'HE':
        prediction = 'Meditasi dan Kegiatan yang menyenangkan  '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu dan Luangkan waktu kamu untuk kegiatan santai seperti healing di tempat bernuansa alam, menonton komedi, memasak atau bermain game'
    elif prediction[0] == 'HF':
        prediction = 'Meditasi dan Jounaling  '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu dan melakukan journaling/menulis buku harian untuk mengungkapkan ketakutan, pikiran, dan perasaan terdalam. '
    elif prediction[0] == 'HG':
        prediction = 'Meditasi dan Yoga  '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu '
    elif prediction[0] == 'HI':
        prediction = 'Meditasi dan Art Terapi  '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu dan melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat'
    elif prediction[0] == 'HL':
        prediction = 'Meditasi dan Terapi Musik '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu dan dengarkan musik klasik yang akan membantu kamu menjadi relax dan tenang '
    elif prediction[0] == 'HM':
        prediction = 'Meditasi dan Menggunakan Aroma Terapi '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu dan gunakan aroma therapy saat meditasi seperti esensial oil dapat membantu menenangkan pikiran kamu'
    elif prediction[0] == 'HN':
        prediction = 'Meditasi dan Manajemen waktu dengan baik '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu dan jangan terlalu memaksakan diri terhadap aktivitas yang terlalu banyak. '
    elif prediction[0] == 'HO':
        prediction = 'Meditasi dan Gaya hidup sehat  '
        explain = 'Meditasi bekerja untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan. Pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu dan atur pola hidup yang sehat, Makan makanan yang sehat, kurangi kafein dan gula, Hindari alkohol, rokok, dan obat-obatan'
    elif prediction[0] == 'IA':
        prediction = 'Art Terapi dan Tetap jaga kesehatan Mental  '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat'
    elif prediction[0] == 'IB':
        prediction = 'Art Terapi dan Nutrisi Makanan  '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai serta berkreasi dengan tanah liat dan makan-makanan yg sehat dan bergizi seperti alpukat, oatmeal, sayuran, atau dark cokelat.'
    elif prediction[0] == 'IC':
        prediction = 'Art Terapi dan Olahraga '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai serta berkreasi dengan tanah liat dan berolahraga teratur cukup dengan berjalan kaki, melakukan aktivitasi aerobik setiap hari selama 30 hingga 60 menit.'
    elif prediction[0] == 'ID':
        prediction = 'Art Terapi dan Tidur yan cukup '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai serta berkreasi dengan tanah liat dan tidur yang cukup'
    elif prediction[0] == 'IE':
        prediction = 'Art Terapi dan Kegiatan yang menyenangkan '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat dan Luangkan waktu kamu untuk kegiatan santai seperti healing di tempat bernuansa alam, menonton komedi, memasak atau bermain game'
    elif prediction[0] == 'IF':
        prediction = 'Art Terapi dan Journaling  '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat dan melakukan journaling/menulis buku harian untuk mengungkapkan ketakutan, pikiran, dan perasaan terdalam.'
    elif prediction[0] == 'IG':
        prediction = 'Art Terapi dan Yoga  '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat dan lakukan yoga untuk membantu menjernihkan pikiran dan membuat kamu lebih relax'
    elif prediction[0] == 'IL':
        prediction = 'Art Terapi dan Terapi Musik  '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat dan mendengarkan musik klasik atau bernyanyi bersama dengan musik dapat membantu kamu menjadi lebih relax dan tenang'
    elif prediction[0] == 'IM':
        prediction = 'Art Terapi  dan Menggunakan aroma terapi  '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat dan gunakan aroma therapy seperti esensial oil dapat membantu menenangkan pikiran kamu'
    elif prediction[0] == 'IN':
        prediction = 'Art Terapi dan Manajemen waktu dengan baik  '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat dan jangan terlalu memaksakan diri terhadap aktivitas yang terlalu banyak.'
    elif prediction[0] == 'IO':
        prediction = 'Art Terapi  dan Gaya hidup sehat '
        explain = 'Art therapy memberikan ruang untuk mengekspresikan kesedihan dan perasaan melalui media menggambar seni yang menjadi sulit apabila digambarkan melalui kata-kata. Kamu bisa melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat dan atur pola hidup yang sehat, Makan makanan yang sehat, kurangi kafein dan gula, Hindari alkohol, rokok, dan obat-obatan'
    elif prediction[0] == 'KA':
        prediction = 'Tulis kekhawatiran kamu dan Tetap jaga kesehatan Mental  '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti.'
    elif prediction[0] == 'KB':
        prediction = 'Tulis kekhawatiran kamu dan Nutrisi Makanan '
        explain = 'jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan makan-makanan yg sehat dan bergizi seperti alpukat, oatmeal, sayuran, atau dark cokelat.'
    elif prediction[0] == 'KC':
        prediction = 'Tulis kekhawatiran kamu dan Olahraga  '
        explain = 'jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan berolahraga teratur cukup dengan berjalan kaki, melakukan aktivitasi aerobik setiap hari selama 30 hingga 60 menit.'
    elif prediction[0] == 'KD':
        prediction = 'Tulis kekhawatiran kamu dan Tidur yang cukup  '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan tidur yang cukup.'
    elif prediction[0] == 'KE':
        prediction = 'Tulis kekhawatiran kamu dan Kegiatan yang menyenangkan  '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan Luangkan waktu kamu untuk kegiatan santai seperti healing di tempat bernuansa alam, menonton komedi, memasak atau bermain game.'
    elif prediction[0] == 'KF':
        prediction = 'Tulis kekhawatiran kamu dan Journaling '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan melakukan journaling/menulis buku harian untuk mengungkapkan ketakutan, pikiran, dan perasaan terdalam.'
    elif prediction[0] == 'KG':
        prediction = 'Tulis kekhawatiran kamu dan Yoga'
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan lakukan yoga untuk membantu menjernihkan pikiran dan membuat kamu lebih relax.'
    elif prediction[0] == 'KH':
        prediction = 'Tulis kekhawatiran kamu dan Meditasi '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan lakukan meditasi untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan dan pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu.'
    elif prediction[0] == 'KI':
        prediction = 'Tulis kekhawatiran kamu dan Art Terapi  '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat.'
    elif prediction[0] == 'KJ':
        prediction = 'Tulis kekhawatiran kamu dan Tetap bangun hubungan '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan saat stres kamu lebih sering mengasingkan diri, kamu bisa curhat dengan teman tentang perasaan kamu atau hangout dengan teman, atau nongkrong.'
    elif prediction[0] == 'KL':
        prediction = 'Tulis kekhawatiran kamu dan Terapi Musik'
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan mendengarkan musik klasik atau bernyanyi bersama dengan musik dapat membantu kamu menjadi lebih relax dan tenang.'
    elif prediction[0] == 'KM':
        prediction = 'Tulis kekhawatiran kamu dan Menggunakan Aroma Terapi '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan gunakan aroma therapy saat meditasi seperti esensial oil dapat membantu menenangkan pikiran kamu.'
    elif prediction[0] == 'KN':
        prediction = 'Tulis kekhawatiran kamu dan Manajemen waktu dengan baik '
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan jangan terlalu memaksakan diri terhadap aktivitas yang terlalu banyak.'
    elif prediction[0] == 'KO':
        prediction = 'Tulis kekhawatiran kamu dan Gaya Hidup Sehat'
        explain = 'Jika pikiran kamu cemas, coba buat catatan singkat tentang kekhawatiran kamu. Jangan buang-buang tenaga untuk memikirkan sesuatu yang belum pasti dan atur pola hidup yang sehat, Makan makanan yang sehat, kurangi kafein dan gula, Hindari alkohol, rokok, dan obat-obatan.'
    elif prediction[0] == 'PA':
        prediction = 'Latihan pernapasan kamu dan Tetap jaga kesehatan Mental  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif'
    elif prediction[0] == 'PB':
        prediction = 'Latihan pernapasan kamu dan Nutrisi Makanan  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Serta jangan lupa diimbangi dengan makan-makanan yang bergizi'
    elif prediction[0] == 'PC':
        prediction = 'Latihan pernapasan kamu dan Olahraga '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Serta berolahraga teratur cukup dengan berjalan kaki, melakukan aktivitasi aerobik setiap hari selama 30 hingga 60 menit.'
    elif prediction[0] == 'PD':
        prediction = 'Latihan pernapasan kamu dan Tidur yang cukup  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif, Serta tidur yang cukup'
    elif prediction[0] == 'PE':
        prediction = 'Latihan pernapasan kamu dan Kegiatan yang menyenangkan '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Serta Luangkan waktu kamu untuk kegiatan santai seperti healing di tempat bernuansa alam, menonton komedi, memasak atau bermain game'
    elif prediction[0] == 'PF':
        prediction = 'Latihan pernapasan kamu dan Journaling  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Serta melakukan journaling/menulis buku harian untuk mengungkapkan ketakutan, pikiran, dan perasaan terdalam.'
    elif prediction[0] == 'PG':
        prediction = 'Latihan pernapasan kamu dan Yoga '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Serta melakukan yoga untuk membantu menjernihkan pikiran dan membuat kamu lebih relax.'
    elif prediction[0] == 'PH':
        prediction = 'Latihan pernapasan kamu dan Tetap Meditasi  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Serta lakukan meditasi untuk mengalihkan pikiran kamu dari mengkhawatirkan masa depan dan pilih tempat yang nyaman dan tenang dan gunakan aplikasi meditasi yang dapat memandu kamu.'
    elif prediction[0] == 'PI':
        prediction = 'Latihan pernapasan kamu dan Art terapi '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Serta melakukan kegiatan menggambar, melukis, mewarnai dan berkreasi dengan tanah liat.'
    elif prediction[0] == 'PJ':
        prediction = 'Latihan pernapasan kamu dan Tetap bangun hubungan  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Saat stres kamu lebih sering mengasingkan diri, kamu bisa curhat dengan teman tentang perasaan kamu atau hangout dengan teman, atau nongkrong.'
    elif prediction[0] == 'PL':
        prediction = 'Latihan pernapasan kamu dan Terapi musik  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif dan mendengarkan musik klasik atau bernyanyi bersama dengan musik dapat membantu kamu menjadi lebih relax dan tenang.'
    elif prediction[0] == 'PM':
        prediction = 'Latihan pernapasan kamu dan Menggunakan Aroma Terapi  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif.Serta gunakan aroma therapy seperti esensial oil dapat membantu menenangkan pikiran kamu'
    elif prediction[0] == 'PN':
        prediction = 'Latihan pernapasan kamu dan Manajemen waktu dengan baik '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Jangan terlalu memaksakan diri terhadap aktivitas yang terlalu banyak.'
    elif prediction[0] == 'PO':
        prediction = 'Latihan pernapasan kamu dan Gaya hidup sehat  '
        explain = 'Ketika kamu khawatir, kamu menjadi cemas dan bernapas lebih cepat, sering kali menyebabkan kecemasan lebih lanjut. Tetapi dengan berlatih latihan pernapasan dalam, kamu dapat menenangkan pikiran dan menenangkan pikiran negatif. Atur pola hidup yang sehat, Makan makanan yang sehat, kurangi kafein dan gula, Hindari alkohol, rokok, dan obat-obatan.'
    
    
    #Depresi
    if questions['D_score'] >= 0 and questions['D_score'] <= 9:
        questions['d_score'] = "Normal"
    if questions['D_score'] >= 10 and questions['D_score'] <= 13:
        questions['d_score'] = "Ringan"
    if questions['D_score'] >= 14 and questions['D_score'] <= 20:
        questions['d_score'] = "Sedang"
    if questions['D_score'] >= 21 and questions['D_score'] <= 27:
        questions['d_score'] = "Parah"
    if questions['D_score'] >= 28:
        questions['d_score'] = "Sangat Parah"

    #Ax
    if questions['A_score'] >= 0 and questions['A_score'] <= 7:
        questions['a_score'] = "normal"
    if questions['A_score'] >= 8 and questions['A_score'] <= 9:
        questions['a_score'] = "ringan"
    if questions['A_score'] >= 10 and questions['A_score'] <= 14:
        questions['a_score'] = "sedang"
    if questions['A_score'] >= 15 and questions['A_score'] <= 19:
        questions['a_score'] = "parah"
    if questions['A_score'] >= 20:
        questions['a_score'] = "sangat parah"

    #Stress
    if questions['S_score'] >= 0 and questions['S_score'] <= 14:
        questions['s_score'] = "normal"
    if questions['S_score'] >= 15 and questions['S_score'] <= 18:
        questions['s_score'] = "ringan"
    if questions['S_score'] >= 19 and questions['S_score'] <= 25:
        questions['s_score'] = "sedang"
    if questions['S_score'] >= 26 and questions['S_score'] <= 33:
        questions['s_score'] = "parah"
    if questions['S_score'] >= 33:
        questions['s_score'] = "sangat parah"

    dass = DASS()
    update_to_sql(ip_addr,questions['nama'],questions['D_score'],questions['A_score'],questions['S_score'],questions['d_score'],questions['a_score'],questions['s_score'],prediction,explain)
    return render_template('hasil.html', 
    questions=questions, 
    prediction=prediction, 
    explain=explain,ip_addr=ip_addr
    )


@app.route('/test', methods=['POST', 'GET'])
def test():
    back = False
    ip_addr = request.environ['REMOTE_ADDR']
    dass.getalldata(ip_addr)
    total = dass.total
    if request.method == 'POST':
        answer = request.form.get('rad')#variabel untk menyimpan jwbn yg diwebsite
        answer1 = request.form.get('rad1')
        answer2 = request.form.get('rad2')
        answer3 = request.form.get('rad3')
        answer4 = request.form.get('rad4')
        choice = request.form.get('tombol')
        if choice != "Lanjut":
            output,jawaban0,jawaban1,jawaban2,jawaban3,jawaban4 = dass.back_question(ip_addr)
            if not output:
                flash('Anda tidak bisa kembali', 'error')
            else: 
                back = True
        else:
            if not answer:
                flash('Pertanyaan pertama belum dijawab', 'error')
            elif not answer1:
                flash('Pertanyaan kedua belum dijawab', 'error')
            elif not answer2 and total < 40:
                flash('Pertanyaan ketiga belum dijawab', 'error')
            elif not answer3 and total < 40:
                flash('Pertanyaan keempat belum dijawab', 'error')
            elif not answer4 and total < 40:
                flash('Pertanyaan kelima belum dijawab', 'error')
            else:
                if answer:
                    dass.input_answer(int(answer),ip_addr)
                    #dass.add_score(int(answer),ip_addr) #tiap jwbwn di cek di test_dass
                if answer1:
                    dass.input_answer(int(answer1),ip_addr)
                    #dass.add_score(int(answer1),ip_addr)    
                if answer2:
                    dass.input_answer(int(answer2),ip_addr)
                    #dass.add_score(int(answer2),ip_addr)
                if answer3:
                    dass.input_answer(int(answer3),ip_addr)
                    #dass.add_score(int(answer3),ip_addr)
                if answer4:
                    dass.input_answer(int(answer4),ip_addr)
                    #dass.add_score(int(answer4),ip_addr)
                
                dass.next_question(ip_addr)
        
        if dass.is_finished(ip_addr): #ngecek apa soal sudah dijwb semua
            questions['D_score'],  questions['A_score'], questions['S_score'], questions['nama'] = dass.get_score(ip_addr)
            return redirect(url_for('hasil'))
    qnum = 42
    quest = dass.question_num
    qnum = qnum - quest
    soal = dass.total
    if(qnum == 2):
        return render_template('test.html',
                            quest_num=qnum,
                            question_num=dass.question_num + 2,
                            total_num=len(dass.question_bank),
                            question=dass.get_question_text(0),
                            soal = soal,
                            question1=dass.get_question_text(1),ip_addr=ip_addr) 
    elif(back):
        return render_template('test.html',
                                quest_num=qnum,
                                question_num=dass.question_num + 5,
                                total_num=len(dass.question_bank),
                                question=dass.get_question_text(0),
                                question1=dass.get_question_text(1),
                                question2=dass.get_question_text(2),
                                question3=dass.get_question_text(3),
                                jawaban0 = jawaban0,
                                jawaban1 = jawaban1,
                                jawaban2 = jawaban2,
                                jawaban3 = jawaban3,
                                jawaban4 = jawaban4,
                                soal = soal,
                                question4=dass.get_question_text(4),ip_addr=ip_addr)
    else:
        return render_template('test.html',
                                quest_num=qnum,
                                soal = soal,
                                question_num=dass.question_num + 5,
                                total_num=len(dass.question_bank),
                                question=dass.get_question_text(0),
                                question1=dass.get_question_text(1),
                                question2=dass.get_question_text(2),
                                question3=dass.get_question_text(3),
                                question4=dass.get_question_text(4),ip_addr=ip_addr)

#MYSQL FUNCTION
def insertsql(ip,nama):
    cur = mydb.cursor()
    cur.execute("INSERT INTO user (IP,nama) VALUES (%s,%s)", (
        ip,nama
    ))
    mydb.commit()

def update_to_sql(dat0,dat1,dat2,dat3,dat4,dat5,dat6,dat7,dat8,dat9):
    mycursor = mydb.cursor()

    sql = "INSERT INTO depresi (IP,nama,Score_Depresi, Score_Anxiety, Score_Stress, TK_Depresi, TK_Anxiety, TK_Stress, Prediksi, Penjelasan) VALUES (%s,%s, %s,%s, %s,%s, %s,%s,%s,%s)"
    val = (dat0,dat1,dat2,dat3,dat4,dat5,dat6,dat7,dat8,dat9)

    mycursor.execute(sql, val)

    mydb.commit()

def ReplaceSql(ip,nama):
    cur = mydb.cursor()
    cur.execute("UPDATE user SET nama = %s WHERE IP=%s AND HASIL = 0", (
        nama, ip
    ))
    mydb.commit()

#SETTING HOST
if __name__ == "__main__":
   app.run(host="0.0.0.0", port = 8080)
