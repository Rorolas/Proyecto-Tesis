
library(shiny)


shinyServer(function(input, output, session) {  # You can access the value of the widget with input$file, e.g.
  observeEvent(input$b1, {
    
    bcp_tweets <-  searchTwitter('latamairlines', n = 50)
    tweets.df = ldply(bcp_tweets, function(t) t$toDataFrame())
    write.csv(tweets.df$text, file = "../data/Data_Original2.csv")
    RPTA='Tweets Extraidos correctamente'
    session$sendCustomMessage(type = 'testmessage',
                              message = RPTA)
    
  })
  observeEvent(input$b2, {
    FuncionFinal_svm()
    session$sendCustomMessage(type = 'testmessage',
                              message = 'Proceso Terminado (SVM)')
  })
  observeEvent(input$b3, {
    FuncionFinal_KNN()
    
    output$distPlot <- renderPlot({
      
      #x    <- faithful$waiting
      #bins <- seq(min(x), max(x), length.out = input$bins + 1)
      inf_finak <- read.csv('D:/Proyecto tesis/Data/Informe_Final.csv', sep = ';', header = T)
      x    <- inf_finak$clasificacion
      bins <-inf_finak$clasificacion
      hist(x, breaks = 5, col = "#75AADB", border = "white",
           xlab = "Histograma de frecuencias de los clusters",
           main = "Clusters")
      
    })
    session$sendCustomMessage(type = 'testmessage',
                              message = 'Proceso Terminado (KNN), Gráfico actualizado')
  })


})
