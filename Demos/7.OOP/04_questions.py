
# Question

import random

class Questions:
    def __init__(self, question, choice,answer, subject):
        self.question = question
        self.choice = choice
        self.answer = answer
        self.subject = subject

    def showQuestion(self):
        print('******************************************************')
        print("Soru:", self.question)
        print("Seçenekler:")
        for secenek, cevap in self.choice:
            print(secenek + ":", cevap)  

    def checkAnswer(self, selectAnswer):
        return selectAnswer == self.answer        
 

          
soru_seti = {

        "Soru 1": {
            "soru_metni": "8 * 4 kaçtir?",
            "secenekler": {
                "A": "24",
                "B": "32",
                "C": "36",
                "D": "40"
            },
            "dogru_cevap": "B",
            "konu":"Matematik"
        },
        "Soru 2": {
            "soru_metni": "Karekökü 25 olan sayi hangisidir?",
            "secenekler": {
                "A": "3",
                "B": "5",
                "C": "7",
                "D": "9"
            },
            "dogru_cevap": "B",
            "konu":"Matematik"
        },
        "Soru 3": {
            "soru_metni": "Türkiye'nin başkenti hangi şehirdir?",
            "secenekler": {
                "A": "İstanbul",
                "B": "Ankara",
                "C": "İzmir",
                "D": "Antalya"
            },
            "dogru_cevap": "B",
            "konu":"Coğrafya"
        },
        "Soru 4": {
            "soru_metni": "Dünyanin en yüksek daği hangisidir?",
            "secenekler": {
                "A": "Mont Blanc",
                "B": "Everest",
                "C": "Kilimanjaro",
                "D": "K2"
            },
            "dogru_cevap": "B",
            "konu":"Coğrafya"
        },
        "Soru 5": {
            "soru_metni": "Osmanli İmparatorluğu'nun son dönem padişahi kimdir?",
            "secenekler": {
                "A": "II. Mahmud",
                "B": "III. Mustafa",
                "C": "II. Abdülhamid",
                "D": "V. Mehmed Reşad"
            },
            "dogru_cevap": "D",
            "konu":"Tarih"
        },
        "Soru 6": {
            "soru_metni": "I. Dünya Savaşi'nin başlangiç tarihi nedir?",
            "secenekler": {
                "A": "1912",
                "B": "1914",
                "C": "1916",
                "D": "1918"
            },
            "dogru_cevap": "B",
            "konu":"Tarih"
        },
        "Soru 7": {
            "soru_metni": "Hangisi William Shakespeare'in oyunlarndan biridir?",
            "secenekler": {
                "A": "Hamlet",
                "B": "Don Kişot",
                "C": "Suç ve Ceza",
                "D": "Sefiller"
            },
            "dogru_cevap": "A",
            "konu":"Edebiyat"
        },
       "Soru 8": {
            "soru_metni": "Türk edebiyatinda 'Halit Ziya Uşakligil' hangi dönemin yazaridir?",
            "secenekler": {
                "A": "Tanzimat Dönemi",
                "B": "Servet-i Fünun Dönemi",
                "C": "Milli Edebiyat Dönemi",
                "D": "Cumhuriyet Dönemi"
            },
            "dogru_cevap": "A",
            "konu":"Edebiyat"
        }
}


def processMain():
    for soruSec in range(4):
        # Rastgele soru seçer
        soruSec = random.choice(list(soru_seti.keys()))

        question = soru_seti[soruSec]['soru_metni']
        choices = soru_seti[soruSec]['secenekler'].items()
        answer = soru_seti[soruSec]['dogru_cevap']
        subject = soru_seti[soruSec]['konu']

        q1 = Questions(question,choices,answer,subject)
        q1.showQuestion()
        del soru_seti[soruSec]
        answerQuestion(q1)

    
def answerQuestion(question):
    selectAnswer = str(input("Cevap şikkini giriniz : "))
    if question.checkAnswer(selectAnswer):
        print('Tebrikler. cevabi bildiniz')
    else:
        print(f'Maalesef, yanliş cevap.. DOĞRU CEVAP {question.answer}')       



processMain()



