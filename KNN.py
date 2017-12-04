import re
from email import header
import nltk
import csv
from builtins import list

from matplotlib.dates import num2date
def Limpieza_KNN():
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
          if listatokenizada[i] in str(stopwords):
              listaEliminar.append(listatokenizada[i])
          if listatokenizada[i] in listaemojis2:
              listaEliminar.append(listatokenizada[i])
  
      listaEliminar= list(set(listaEliminar))
      textoprocesado = ''
      for x in range(len(listaEliminar)):
          listatokenizada.remove(listaEliminar[x])
      for j in range(len(listatokenizada)):
          textoprocesado = textoprocesado +  ' '+  listatokenizada[j]
      del listatokenizada, listaEliminar
      return textoprocesado
  
  def tokenizar(tweet):
      listatokenizada = preprocess(tweet)
      return listatokenizada
  
  #hasta aca
  C1_callcenter = []
  C2_tarifa = []
  C3_equipaje = []
  C4_servicio = []
  C5_sistema = []
  C6_otros = []
  stopwords = []
  with open("D:/Proyecto tesis/data/lista de stopwords.csv", 'r') as my_file:
      reader = csv.reader(my_file, delimiter=';')
      stopwords = list(reader)
  with open("D:/Proyecto tesis/data/Clusters.csv", 'r') as my_file:
      reader = csv.reader(my_file, delimiter=';')
      lista = list(reader)
  
  NUM =1
  for i in lista:
      texto = str(i)
      texto = str.replace(texto,"'","")
      texto = str.replace(texto, "[", "")
      texto = str.replace(texto, "]", "")
  
      clusters = list(texto.split(','))
      C1_callcenter.append(clusters[0])
      C2_tarifa.append(clusters[1])
      C3_equipaje.append(clusters[2])
      C4_servicio.append(clusters[3])
      C5_sistema.append(clusters[4])
  
  
  
  C1_callcenter = list(set(C1_callcenter))
  C2_tarifa = list(set(C2_tarifa))
  C3_equipaje = list(set(C3_equipaje))
  C4_servicio = list(set(C4_servicio))
  C5_sistema = list(set(C5_sistema))
  C6_otros = list(set(C6_otros))
  
  
  with open("D:/Proyecto tesis/data/Data_svm_id.csv", 'r') as my_file:
      reader = csv.reader(my_file, delimiter=';'  )

      tweets = list(reader)
      print(tweets)
      tweets.pop(0)
  Data_lista =[]
  for i in tweets:
      tweet = procesartexto(str(i)).upper()
      tweet_split = list(tweet.split(' '))
      c1 = 0
      c2 = 0
      c3 = 0
      c4 = 0
      c5 = 0
      c6 = 0
      for j in range(len(tweet_split)):
          if len(tweet_split[j]) > 3:
              if tweet_split[j] in str(C1_callcenter):
                  c1 = c1 +1
              if tweet_split[j] in str(C2_tarifa):
                  c2 = c2 +1
              if tweet_split[j] in str(C3_equipaje):
                  c3 = c3 +1
              if tweet_split[j] in str(C4_servicio):
                  c4 = c4 +1
              if tweet_split[j] in str(C5_sistema):
                  c5 = c5 +1
  
      mayor = []
      mayor.append(c1)
      mayor.append(c2)
      mayor.append(c3)
      mayor.append(c4)
      mayor.append(c5)
      aux = 0
      i=1
      for i in range(5):
          if aux <= mayor[i]:
              pos = i +1
              aux = mayor[i]
      if aux == 0 :
          pos=5
      Data_lista.append([tweet , c1, c2, c3 ,c4, c5, 'C' + str(pos)])
      NUM = NUM +1
      #Data_lista.append([tweet, aux ,str(pos)])
      del mayor
  for x in C1_callcenter:
      if x == ' ':
          C1_callcenter.remove(x)
      if x == '':
          C1_callcenter.remove(x)
  for x in C2_tarifa:
      if x == ' ':
          C2_tarifa.remove(x)
      if x == '':
          C2_tarifa.remove(x)
  for x in C3_equipaje:
      if x == ' ':
          C3_equipaje.remove(x)
      if x == '':
          C3_equipaje.remove(x)
  for x in C4_servicio:
      if x == ' ':
          C4_servicio.remove(x)
      if x == '':
          C4_servicio.remove(x)
  for x in C5_sistema:
      if x == ' ':
          C5_sistema.remove(x)
      if x == '':
          C5_sistema.remove(x)
  
  for x in Data_lista:
      print (x)
  
  with open('D:/Proyecto tesis/data/data_knn.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL , delimiter =';')
      wr.writerow(['Tweet', 'C1', 'C2','C3','C4','C5','CLUSTER'])
      #wr.writerow(['Tweet', 'mayor', 'grupo'])
      wr.writerows(Data_lista)

print("OKK")
