import re
import nltk
import csv
from builtins import list
def Stemmer_SVM ():
    sno = nltk.stem.SnowballStemmer('spanish')
    listaemojis =[':)', ':-)', '=)', ':]', ':D', ':-D', '=D', '>:o', '>:-o', ':o', ':-o ', ':(', ':-(', '=(', ':[ ',
                  ';)', ';-) ', ':( ', ':*', ':-* ', ':p', ':-p ', '>:(', '>:-( ', '<3 ', ':3  ', '^_^  ', '-_-  ', 'O:)',
                  'O:-) ', '3:)', '3:-) ', ':v ', ':|]', '8)', '8-)', 'B)', '8-) ', '8|', '8-|', 'B|', 'B-|', ':/', ':-/',
                  'o.O', 'O.o', ':‐)' , ':-]' ,':]' , ':-3' ,  ':3' ,  ':->' ,  ':>' ,  '8-)' ,  '8)' ,  ':-}' ,  ':}' ,
                  ':o)' ,  ':c)' ,  ':^)' ,  '=]' ,  '=)' ,  ':D' ,  'B^D' ,  'xD' ,  '8D' ,  'x‐D' ,  '8‐D' ,  'X‐D' ,
                  ':‐D' ,  '=D' ,  '=3' ,  'XD' ,  ':-))' ,  ':‐(' ,  ':(' ,  ':‐c' ,  ':c' ,  ':‐<' ,  ':<' ,  ':‐[' ,
                  ':[' ,  ':-||' ,  '>:[' ,  ':{' ,  ':@' ,  '>:(' ,  'D:<' ,   'D:' ,  'D8' ,  'D;' ,  'D=' ,  'DX' ,
                  ':‐O' ,  ':O' ,  ':‐o' ,  ':o' ,  ':-0' ,  '8‐0' ,  '>:O' ,  ':-*' ,  ':*' ,  ':×' ,  ';‐)' ,  ';)' ,
                  '*-)' ,  '*)' ,  ';‐]' ,  ';]' ,  ';^)' ,  ':‐,' ,  'D' ,  ':‐P' ,  ':P' ,  ':‐p' ,  ':p' ,  ':‐b' ,
                  ':b' ,  '=p' ,  'd:' ,  ':S'  ,  '=/' ,  '=/' ,  'O:‐)' ,  'O:)' ,  '|;‐)' ,  '</3'  ,  '<3' ]
    listaemojis2 =[':)', ':-)', '=)', ':]', ':d', ':-d', '=d', '>:o', '>:-o', ':o', ':-o ', ':(', ':-(', '=(', ':[ ',
                  ';)', ';-) ', ':( ', ':*', ':-* ', ':p', ':-p ', '>:(', '>:-( ', '<3 ', ':3  ', '^_^  ', '-_-  ', 'o:)',
                  'o:-) ', '3:)', '3:-) ', ':v ', ':|]', '8)', '8-)', 'b)', '8-) ', '8|', '8-|', 'b|', 'b-|', ':/', ':-/',
                  'o.o', 'o.o', ':‐)' , ':-]' ,':]' , ':-3' ,  ':3' ,  ':->' ,  ':>' ,  '8-)' ,  '8)' ,  ':-}' ,  ':}' ,
                  ':o)' ,  ':c)' ,  ':^)' ,  '=]' ,  '=)' ,  ':d' ,  'b^d' ,  'xd' ,  '8d' ,  'x‐d' ,  '8‐d' ,  'x‐d' ,
                  ':‐d' ,  '=d' ,  '=3' ,  'xd' ,  ':-))' ,  ':‐(' ,  ':(' ,  ':‐c' ,  ':c' ,  ':‐<' ,  ':<' ,  ':‐[' ,
                  ':[' ,  ':-||' ,  '>:[' ,  ':{' ,  ':@' ,  '>:(' ,  'd:<' ,   'd:' ,  'd8' ,  'd;' ,  'd=' ,  'dx' ,
                  ':‐o' ,  ':o' ,  ':‐o' ,  ':o' ,  ':-0' ,  '8‐0' ,  '>:o' ,  ':-*' ,  ':*' ,  ':×' ,  ';‐)' ,  ';)' ,
                  '*-)' ,  '*)' ,  ';‐]' ,  ';]' ,  ';^)' ,  ':‐,' ,  'd' ,  ':‐p' ,  ':p' ,  ':‐p' ,  ':p' ,  ':‐b' ,
                  ':b' ,  '=p' ,  'd:' ,  ':s'  ,  '=/' ,  '=/' ,  'o:‐)' ,  'o:)' ,  '|;‐)' ,  '</3'  ,  '<3' ]
    stopwords=['rt', 'para','e-mail', 'email', 'vez' ,'te','si','de', 'fe','latam','un', 'una', 'unas', 'uno', 'unos', 'usa', 'usais', 'usamos', 'usan', 'usar', 'usas', 'uso', 'usted',
               'ustedes', 'va', 'vais', 'valor', 'vamos', 'van', 'varias', 'varios', 'vaya', 'verdad', 'verdadera',
               'vosotras', 'vosotros', 'voy', 'vuestra', 'vuestras', 'vuestro', 'vuestros', 'y', 'ya', 'yo', 'un', 'una',
               'unas', 'unos', 'uno', 'sobre', 'todo', 'también', 'tras', 'otro', 'algún', 'alguno', 'alguna', 'algunos',
               'algunas', 'ser', 'es', 'soy', 'eres', 'somos', 'sois', 'estoy', 'esta', 'estamos', 'estais', 'estan',
               'como', 'en', 'para', 'atras', 'porque', 'por qué', 'estado', 'estaba', 'ante', 'antes', 'siendo', 'ambos',
               'pero', 'por', 'poder', 'puede', 'puedo', 'podemos', 'podeis', 'pueden', 'fui', 'fue', 'fuimos', 'fueron',
               'hacer', 'hago', 'hace', 'hacemos', 'haceis', 'hacen', 'cada', 'fin', 'incluso', 'primero'	, 'desde',
               'conseguir', 'consigo', 'consigue', '', 'conseguimos', 'consiguen', 'ir', 'voy', 'va', 'vamos',
               'vais', 'van', 'vaya', 'gueno', 'ha', 'tener', 'tengo', 'tiene', 'tenemos', 'teneis', 'tienen', 'el',
               'la', 'lo', 'las', 'los', 'su', 'aqui', 'mio', 'tuyo', 'ellos', 'ellas', 'nos', 'nosotros', 'vosotros',
               'vosotras', 'si', 'dentro', 'solo', 'solamente', 'saber', 'sabes', 'sabe', 'sabemos', 'sabeis', 'saben',
               'ultimo', 'largo', 'bastante', 'haces', 'muchos', 'aquellos', 'aconsiguesquellas', 'sus', 'entonces', 'tiempo',
               'verdad', 'verdadero', 'verdadera'	, 'cierto', 'ciertos', 'cierta', 'ciertas', 'intentar', 'intento',
               'intenta', 'intentas', 'intentamos', 'intentais', 'intentan', 'dos', 'bajo', 'arriba', 'encima', 'usar',
               'uso', 'usas', 'usa', 'usamos', 'usais', 'usan', 'emplear', 'empleo', 'empleas', 'emplean', 'empleamos',
               'empleais', 'valor', 'muy', 'era', 'eras', 'eramos', 'eran', 'modo', 'bien', 'cual', 'cuando', 'donde',
               'mientras', 'quien', 'con', 'entre', 'sin', 'trabajo', 'trabajar', 'trabajas', 'trabaja', 'trabajamos',
               'trabajais', 'trabajan', 'podria', 'podrias', 'podriamos', 'podrian', 'podriais', 'yo', 'aquel']
    emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""
    regex_str = [
        emoticons_str,
        r'<[^>]+>',  # HTML tags
        r'(?:@[\w_]+)',  # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

        r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
        r'(?:[\w_]+)',  # other words
        r'(?:\S)'  # anything else
    ]
    tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
    emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

    def tokenize(s):
        return tokens_re.findall(s)
    def preprocess(s, lowercase=False):
        tokens = tokenize(s)
        if lowercase:
            tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens
    def es_numero(n):
        try:
            float(n)
        except ValueError:
            return False
        return True

    def procesartexto(tweet):
        listatokenizada = preprocess(tweet)
        listatokenizada = list(set(listatokenizada))
        listaEliminar=[]

        for i in range(len(listatokenizada)):
            if es_numero(listatokenizada[i]):
               listaEliminar.append(listatokenizada[i])
            if len(listatokenizada[i])<=1:
                listaEliminar.append(listatokenizada[i])
            if listatokenizada[i].startswith('@'):
                listaEliminar.append(listatokenizada[i])
            if listatokenizada[i].startswith('x'):
                listaEliminar.append(listatokenizada[i])
            if listatokenizada[i].startswith('#'):
                listaEliminar.append(listatokenizada[i])
            if listatokenizada[i].startswith('http'):
                listaEliminar.append(listatokenizada[i])

        listaEliminar= list(set(listaEliminar))
        textoprocesado = ''
        for x in range(len(listaEliminar)):
            valor_eliminar = listaEliminar[x]
            listatokenizada.remove(listaEliminar[x])
        for j in range(len(listatokenizada)):
            textoprocesado = textoprocesado +  ' '+  sno.stem(listatokenizada[j])
        print(textoprocesado)
        del listatokenizada, listaEliminar
        return textoprocesado

    # CSV CON DATA PROCESADA
    csvsalida = open('D:/Proyecto tesis/data\Data_Stemmizada.csv', 'a', newline='')
    salida = csv.writer(csvsalida)
    
    contador = 1
    #Leer csv
    with open('D:/Proyecto tesis/data\Data_Original.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            tweet = ' '.join(row)
            tweet = tweet.lower()
            texto_procesado= procesartexto(tweet)
            salida.writerow([texto_procesado])
            contador =contador + 1
            print(contador)
    csvsalida.close()
