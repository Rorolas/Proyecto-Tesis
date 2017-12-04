#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  tags$head(tags$script(src = "message-handler.js")),

  
  
  sidebarLayout(
 sidebarPanel(
   titlePanel("Sistema de analisis y clasificación LATAM"),
   hr(),
   
   p('1. Extraccion de los tweets'),
   actionButton("b1", label = "Extraer los tweets"),
   hr(),
   p('2. Analisis de Sentimiento (SVM)'),
   actionButton("b2", label = "Procesar"),
   hr(),
   p('3. Clasificación (KNN)'),
   actionButton("b3", label = "Procesar"),
   hr()  
    ),
    mainPanel(
      plotOutput(outputId = "distPlot")
    
    )
  )
)
  
)
