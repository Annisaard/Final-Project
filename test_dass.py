from sklearn.metrics import get_scorer
from question import Question
import mysql.connector


class DASS:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hasiltest"
        )
        self.question_num = 0
        self.D_score = 0
        self.A_score = 0
        self.S_score = 0
        self.total = 0
        self.nama = ""

        self.question_bank =[
        Question('1. Saya merasa bahwa diri saya menjadi marah karena hal-hal sepele','S'),
        Question('2. Saya merasa bibir saya sering kering','A'),
        Question('3. Saya sama sekali tidak dapat merasakan perasaan positif','D'),
        Question('4. Saya mengalami kesulitan bernafas (misalnya: seringkali terengah-engah atau tidak dapat bernafas padahal tidak melakukan aktivitas fisik sebelumnya)','A'),
        Question('5. Saya sepertinya tidak kuat lagi untuk melakukan suatu kegiatan.','D'),
        Question('6. Saya cenderung bereaksi berlebihan terhadap suatu situasi','S'),
        Question('7. Saya merasa goyah (misalnya, kaki terasa mau copot)','A'),
        Question('8. Saya merasa sulit untuk bersantai','S'),
        Question('9. Saya menemukan diri saya berada dalam situasi yang membuat saya merasa sangat cemas dan saya akan merasa sangat lega jika semua ini berakhir','A'),
        Question('10. Saya merasa tidak ada hal yang dapat diharapkan di masa depan','D'),
        Question('11. Saya menemukan diri saya mudah merasa kesal','S'),
        Question('12. Saya merasa telah menghabiskan banyak energi untuk merasa cemas','S'),
        Question('13. Saya merasa sedih dan tertekan','D'),
        Question('14. Saya menemukan diri saya menjadi tidak sabar ketika mengalami penundaan (misalnya: kemacetan lalu lintas, menunggu sesuatu)','S'),
        Question('15. Saya merasa lemas seperti mau pingsan','A'),
        Question('16. Saya merasa saya kehilangan minat akan segala hal','D'),
        Question('17. Saya merasa bahwa saya tidak berharga sebagai seorang manusia','D'),
        Question('18. Saya merasa bahwa saya mudah tersinggung','S'),
        Question('19. Saya berkeringat secara berlebihan (misalnya: tangan berkeringat), padahal temperatur tidak panas atau tidak melakukan aktivitas fisik sebelumnya','A'),
        Question('20. Saya merasa takut tanpa alasan yang jelas','A'),
        Question('21. Saya merasa bahwa hidup tidak bermanfaat','D'),
        Question('22. Saya merasa sulit untuk beristirahat','S'),
        Question('23. Saya mengalami kesulitan dalam menelan','A'),
        Question('24. Saya tidak dapat merasakan kenikmatan dari berbagai hal yang saya lakukan','D'),
        Question('25. Saya menyadari kegiatan jantung, walaupun saya tidak sehabis melakukan aktivitas fisik (misalnya: merasa detak jantung meningkat atau melemah)','A'),
        Question('26. Saya merasa putus asa dan sedih','D'),
        Question('27. Saya merasa bahwa saya sangat mudah marah','S'),
        Question('28. Saya merasa saya hampir panik','A'),
        Question('29. Saya merasa sulit untuk tenang setelah sesuatu membuat saya kesal.','S'),
        Question('30. Saya takut bahwa saya akan terhambat oleh tugas-tugas sepele yang tidak biasa saya lakukan','A'),
        Question('31. Saya tidak merasa antusias dalam hal apapun','D'),
        Question('32. Saya sulit untuk sabar dalam menghadapi gangguan terhadap hal yang sedang saya lakukan.','S'),
        Question('33. Saya sedang merasa gelisah','S'),
        Question('34. Saya merasa bahwa saya tidak berharga','D'),
        Question('35. Saya tidak dapat memaklumi hal apapun yang menghalangi saya untuk menyelesaikan hal yang sedang saya lakukan.','S'),
        Question('36. Saya merasa sangat ketakutan','A'),
        Question('37. Saya melihat tidak ada harapan untuk masa depan','D'),
        Question('38. Saya merasa bahwa hidup tidak berarti','D'),
        Question('39. Saya menemukan diri saya mudah gelisah','S'),
        Question('40. Saya merasa khawatir dengan situasi dimana saya mungkin menjadi panik dan mempermalukan diri sendiri','A'),
        Question('41. Saya merasa gemetar (misalnya: pada tangan)','A'),
        Question('42. Saya merasa sulit untuk meningkatkan inisiatif dalam melakukan sesuatu','D'),
        ]

    def getalldata(self,ip, hasil = False):
        mycursor = self.mydb.cursor()
        ketemu = False
        sql = "SELECT * from user"

        mycursor.execute(sql)
        # get all records
        records = mycursor.fetchall()
        #print(records)
        mycursor.close()
        for find in records:
            if ip == find[0] and find[6]==0:
                ketemu = True
                self.total = find[1]
                self.question_num = find[2]
                self.D_score = find[3] #D_Score
                self.A_score = find[4] #A_Score
                self.S_score = find[5] #S_Score
                self.nama = find[7]
        if not ketemu and not hasil:
            cur = self.mydb.cursor()
            cur.execute("INSERT INTO user (IP) VALUES (%s)", (
                ip,
            ))
            self.mydb.commit()
            cur.close()
            self.getalldata(ip)
        records.clear()

    def sendValue(self,quest_num,D_Score,A_Score,S_Score,Total):
        self.question_num = quest_num
        self.D_score = D_Score
        self.A_score = A_Score
        self.S_score = S_Score
        self.total = Total
    
    def back_question(self,ip):
        if(self.total != 0):
            output = True
            self.question_num -= 5
            self.total -= 5
            cur = self.mydb.cursor()
            cur.execute("UPDATE user SET Total_Jawaban= %s, Quest_num=%s WHERE IP=%s AND Hasil= 0", (
                self.total,self.question_num,ip,
            ))
            self.mydb.commit()
            cur.close()
            self.getalldata(ip)
            getdata = self.mydb.cursor()
            getdata.execute("SELECT * from answer WHERE IP=%s AND Hasil=0",(
                ip,
            ))
            records = getdata.fetchall()
            print(records)
            for find in records:
                if ip == find[0] and find[1]==0:
                    jawaban0 = find[self.total + 2]
                    jawaban1 = find[self.total + 3]
                    jawaban2 = find[self.total + 4]
                    jawaban3 = find[self.total + 5]
                    jawaban4 = find[self.total + 6]
            getdata.close()
        else:
            output = False
        return output,jawaban0,jawaban1,jawaban2,jawaban3,jawaban4
        

    def next_question(self,ip):
        if (self.question_num < len(self.question_bank) - 5):
            self.question_num += 5
            print("Self Quest Num: ", str(self.question_num))
            cur = self.mydb.cursor()
            cur.execute("UPDATE user SET Quest_num=%s WHERE IP=%s AND Hasil= 0", (
                self.question_num,ip,
            ))
            self.mydb.commit()
            cur.close()
            mycursor = self.mydb.cursor()

            sql = "SELECT * from user"

            mycursor.execute(sql)
            # get all records
            records = mycursor.fetchall()
            print(records)
            mycursor.close()


    def get_question_text(self,num):
        return self.question_bank[self.question_num + num].item
    
    def deletedata(self,ip):
        
        cur = self.mydb.cursor()
        cur.execute("DELETE FROM answer WHERE IP= %s", (
            ip,
        ))
        self.mydb.commit()
        cur.close()

    def get_score(self,ip):
        self.count_all_score(ip)
        self.deletedata(ip)
        self.getalldata(ip, True)
        return self.D_score, self.A_score, self.S_score, self.nama

    def count_all_score(self,ip):
        count = 0
        getdata = self.mydb.cursor()
        getdata.execute("SELECT * from answer WHERE IP=%s AND Hasil=0",(
            ip,
        ))
        records = getdata.fetchall()
        print(records)
        data = 0
        for find in records:
            for data in range(45):
                if(data != 0 and data != 1):
                    if(count >= 42):
                        break
                    else:
                        self.add_score(find[data],ip,count)
                        count += 1
        getdata.close()

    def input_answer(self, answer,ip):
        mycursor = self.mydb.cursor()
        ketemu = False
        sql = "SELECT * from answer"

        mycursor.execute(sql)
        # get all records
        records = mycursor.fetchall()
        #print(records)
        mycursor.close()
        for find in records:
            if ip == find[0] and find[1] == 0:
                ketemu = True
                data = "UPDATE answer SET " + "P" + str(self.total) + "=%s WHERE IP=%s AND Hasil= 0"
                curs = self.mydb.cursor()
                curs.execute(data, (
                    answer, ip,
                ))
                self.mydb.commit()
                curs.close()
                self.total += 1
                curs = self.mydb.cursor()# buat buka database
                curs.execute("UPDATE user SET Total_Jawaban=%s,D_Score=%s, A_Score=%s,S_Score=%s WHERE IP=%s AND Hasil= 0", (
                    self.total, self.D_score,self.A_score,self.S_score,ip,#nyimpen data score ke database
                ))
                self.mydb.commit()#eksekusi line 162
                curs.close()
        if not ketemu:
            cur = self.mydb.cursor()
            cur.execute("INSERT INTO answer (IP) VALUES (%s)", (
                ip,
            ))
            self.mydb.commit()
            cur.close()
            self.input_answer(answer,ip)
        records.clear()


    def add_score(self, answer,ip,counts):
        if answer == 0:
            if self.question_bank[counts].label == 'D':
                self.D_score += 0
            elif self.question_bank[counts].label == 'A':
                self.A_score += 0
            elif self.question_bank[counts].label == 'S':
                self.S_score += 0
        elif answer == 1:
            if self.question_bank[counts].label == 'D':
                self.D_score += 1
            elif self.question_bank[counts].label == 'A':
                self.A_score += 1
            elif self.question_bank[counts].label == 'S':
                self.S_score += 1
        elif answer == 2:
            if self.question_bank[counts].label == 'D':
                self.D_score += 2
            elif self.question_bank[counts].label == 'A':
                self.A_score += 2
            elif self.question_bank[counts].label == 'S':
                self.S_score += 2
        elif answer == 3:
            if self.question_bank[counts].label == 'D':
                self.D_score += 3
            elif self.question_bank[counts].label == 'A':
                self.A_score += 3
            elif self.question_bank[counts].label == 'S':
                self.S_score += 3
        #self.total += 1
        print("S Score: " + str(self.S_score) + " A Score: " + str(self.A_score) + " D Score: " + str(self.D_score))
        curs = self.mydb.cursor()# buat buka database
        curs.execute("UPDATE user SET D_Score=%s, A_Score=%s,S_Score=%s WHERE IP=%s AND Hasil= 0", (
            self.D_score,self.A_score,self.S_score,ip,#nyimpen data score ke database
        ))
        self.mydb.commit()#eksekusi line 162
        curs.close()
        #return(self.D_score, self.A_score, self.)

    def is_finished(self,ip):
        if self.total == len(self.question_bank):
            print("Now returning true")
            #count allscore
            curs = self.mydb.cursor()
            curs.execute("UPDATE user SET Hasil=%s WHERE IP=%s AND Hasil= 0", (
                1,ip,
            ))
            self.mydb.commit()
            curs.close()
            return True
        else:
            print("Pertanyaan yang sudah dijawab: " + str(self.total))
            return False

    def reset(self):
        self.question_num = 0
        self.question_num = 0
        self.D_score = 0
        self.A_score = 0
        self.S_score = 0
        self.total = 0


# dass = DASS()

# dass.get_score("127.0.0.1")