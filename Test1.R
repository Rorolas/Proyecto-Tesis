install.packages("RJSONIO")
install.packages("devtools")
install("D:/Proyecto tesis/Librerias/rPython")

  


FuncionFinal_svm <- function(x){
  library(devtools)
  library(NLP)
  library(RJSONIO)
  library(rPython)
  require(rPython) 
  library(NLP)
  library(tm)
  library(ggplot2)
  library(lattice)
  library(caret)
  python.load("D:/Proyecto tesis/SVM.py")
  python.call("Stemmer_SVM")
  data_original <- read.csv('D:/Proyecto tesis/Data/Data_Original.csv', sep = ';', header = T)
  tweets <- read.csv('D:/Proyecto tesis/Data/Data_Stemmizada.csv', sep = ';', header = T)
  tweets$Sentiment <- data_original$Sentiment
  tweets$id <- data_original$id
  colnames(tweets)[1] <- "text"
  Algotirmo_svm(tweets = tweets)
}


Algotirmo_svm <- function(tweets) {
  stopWords <- read.csv('D:/Proyecto tesis/data/lista de stopwords.csv', header = F)
  corpus = Corpus(VectorSource(tweets$text))
  corpus_low <- tm_map(corpus, content_transformer(tolower))
  length(corpus)
  corpus <- corpus_low
  corpus <- tm_map(corpus, removeWords, stopWords[,1])
  corpus <- tm_map(corpus, removePunctuation)
  frequencies <-  DocumentTermMatrix(corpus)
  findFreqTerms(frequencies, lowfreq = 600)
  sparse <- removeSparseTerms(frequencies, 0.995)
  tweetsSparse <- as.data.frame(as.matrix(sparse))
  colnames(tweetsSparse) = make.names(colnames(tweetsSparse))
  tweetsSparse$sentiment <- tweets$Sentiment
  tweetsSparse$id <- tweets$id
  library(caTools)
  set.seed(12)
  split <- sample.split(tweetsSparse$sentiment, SplitRatio = 0.8334027836)
  trainSparse <- subset(tweetsSparse, split == TRUE)
  testSparse <- subset(tweetsSparse, split == FALSE)
  library(e1071)
  SVM <- svm(as.factor(sentiment)~.,data=trainSparse) 
  predict_SVM <- predict(SVM, newdata = testSparse)
  confusionMatrix(predict_SVM, testSparse$sentiment)
  aux <- as.character(predict_SVM)
  Listafinal_id <- vector('integer') 
  Listafinal_tweet <- vector('integer')
  Listafinal_Sentimiento <- aux
  Listafinal_id <- testSparse$id
  data_original <- read.csv('D:/Proyecto tesis/data/Data_Original.csv', sep = ';', header = T)
  for(i in 1:length(Listafinal_id)){
    Listafinal_tweet[i] = as.character(data_original$Texto[i])
  }
  ListaFinal <- cbind(Listafinal_tweet,Listafinal_id, Listafinal_Sentimiento)
  
  for(i in 1:length(Listafinal_id)){
    print(data_original$Texto[i])
    Listafinal_tweet[i] = as.character(data_original$Texto[i])
  }
  write.table(ListaFinal, file = "D:/Proyecto tesis/Data/Data_svm_id.csv", sep = ";", row.names=FALSE, col.names = F)
  print('CSV CREADO, OK!!!')
}
#EJECUTAR***************************************
FuncionFinal_svm()

