import time
import winsound
class DECODE:
    def process(self,*numlist):
        morse = []
        for i in numlist:
            if i == 0:
                continue
            if i <= 5 and i > 0:
                morse.append('.')
            if i > 5 and i <= 25:
                morse.append('-')
            if i < 0 and i >= -25:
                morse.append(' ')
            if i < -25 and i >= -60:
                morse.append('/t')
            if i < -60:
                morse.append('/t/n/t')
        print(morse)
        str = ''
        for i in morse:
            if i == ' ':
                continue
            str = str + i
        print(str)
        code = str.split("/t")
        self.res = self.decode(*code)
        return self.res

    def decode(self,*code):
        code_dict = {'-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                     '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                     '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
                     '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
                     '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                     '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z',
                     '.-.-.-': '.', '---...': ':', '--..--': ',', '-.-.-.': ';', '..--..': '?',
                     '-...-': '=', '.----.': "'", '-..-.': '/', '-.-.--': '!', '-....-': '--',
                     '..--.-': '-', '.-..-.': '"', '-.--.': '(', '-.--.-': ')'}
        res = ''
        UpandLow = 1
        for i in code:
            if i == '/n':
                UpandLow = 1
            graphme = code_dict.get(i)
            if graphme is None:
                continue
            if UpandLow == 1:
                graphme = graphme.upper()
                UpandLow = 0
                res = res + ' '
            res = res + graphme
        return res.replace(' ', '', 1)


class ENCODE:
    def __init__(self,text):
        self.text = text.upper()
    def encode(self):
        freq1 = 1500  # 短音发声频率
        freq2 = 2000  # 长音发声频率

        interv_short = 100  # 短音“.”的发声时长
        interv_long = 300  # 长音“-”的发声时长
        str = ''
        code_dict = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                     'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                     'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                     'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                     'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                     '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.', '?': '..--..',
                     '=': '-...-', "'": '.----.', '/': '-..-.', '!': '-.-.--', '--': '-....-',
                     '-': '..--.-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-'}
        for graphme in self.text:
            print('graphme:', graphme)
            code = code_dict.get(graphme)
            if code is None:
                print('该符号不在字典中')
                continue
            print('code', code)

            for c in code:
                if c == '.':
                    ret = winsound.Beep(freq1, interv_short)
                    print('ret = ', ret)
                    time.sleep(0.1)  # 加入0.1s延时
                elif c == '-':
                    ret = winsound.Beep(freq2, interv_long)
                    print('ret = ', ret)
                    time.sleep(0.1)
                else:
                    print('错误编码')

                time.sleep(0.5)


