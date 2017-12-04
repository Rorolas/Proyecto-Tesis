library(rPython)
librari
FuncionFinal_KNN <- function(x){
  python.load("D:/Proyecto tesis/KNN.py")
  python.call("Limpieza_KNN")
  KNN_FUNCION()  
  }

#cambiar directorio
KNN_FUNCION <- function(){
  data <- read.csv("D:/Proyecto tesis/data/data_knn.csv",header=T, sep =';',stringsAsFactors = FALSE)
  stringsAsFactors = FALSE 
  str(data)
  as.numeric(data$c1) 
  library(class)
  data$clasificacion <- factor(data$CLUSTER, levels = c("C1", "C2", "C3", "C4", "C5"), labels = c("1","2","3","4","5"))
  round(prop.table(table(data$Cluster)) * 100, digits = 1) 
  data_n <- as.data.frame(lapply(data[2:6], normalize))
  summary(data_n$radius)
  data_train <- data_n[1:1500,]
  data_test <- data_n[1501:1998,]
  
  data_train_labels <- data[1:1500, 6]
  data_test_labels <- data[1501:1998, 6]
  summary(data_n)
  set.seed(123)
  data_test_pred <- knn(train =data_train, test =  data_test, cl =  data_train_labels, k=3)
  knn3 <- knn(train =data_train, test =  data_test,cl =  data_train_labels, k=3)
  100 * sum(data_test_labels == knn3)/100
  table(knn3, data_test_labels)
  library(gmodels)
  summary(data_test_pred)
  CrossTable(x=data_test_labels, y= data_test_pred, prop.chisq = FALSE)
  data_test_cluster = data[1501:1998,]
  data_test_cluster = data_test_cluster[-2:-7]
  write.table(data_test_cluster, file = "D:/Proyecto tesis/Data/Informe_Final.csv", sep = ";", row.names=FALSE)
  print('CSV CREADO!!!!********************************')
  
}
KNN_FUNCION()
FuncionFinal_KNN()
normalize <- function(x) {
  return ((x - min(x)) / (max(x) - min(x))) }
 