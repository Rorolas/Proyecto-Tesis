Extraccion <- function(){
  library(twitteR)
  library (ROAuth)
  library(httr)
  library(devtools)
  library(plyr)
  library(corpus)
  library(tm)
  library(tmap)
  library(SnowballC)
  library(NLP)
  
  consumer_key <- 'gGbrR5p9xzmuPG73gkaAnhY6F'
  consumer_secret <- 'EMKZWePzKpC5x9j52cODVmcg7GZTUTf24LmWldi9k53HeAGZ7U'
  access_token <- '4742183426-GOFDXTnOToUb3S6q1Cd6hyguqUHhcsaFO56WhWn'
  access_secret <- 'RJ9uwoO3Ta2tPZo5cLBovP14rGmAn23KoENdz1Mu0klUb'
  setup_twitter_oauth(consumer_key, consumer_secret,access_token,access_secret)
  bcp_tweets <-  searchTwitter('denunciaslatam', n = 1000)
  
  tweets.df = ldply(bcp_tweets, function(t) t$toDataFrame())
  write.csv(tweets.df$text, file = "../data/Data_Original2.csv")
  
}
Extraccion()
