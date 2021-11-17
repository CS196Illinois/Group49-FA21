install.packages("ggplot2")
install.packages("dplyr")
install.packages("broom")
install.packages("ggpubr")

library(ggplot2)
library(dplyr)
library(broom)
library(ggpubr)


#Tree Cover Loss
treeCoverLossData = read.csv("/Users/Viven/Group49CSVData/Tree_Cover_Loss_in_Alaska.csv")
TreeCoverLoss.year.lm <- lm(Forest.Cover.Loss.in.Alaska..Square.Meters. ~ Year, data = treeCoverLossData)
summary(TreeCoverLoss.year.lm)
TreeCoverLoss.graph<-ggplot(treeCoverLossData, aes(x=Year, y=Forest.Cover.Loss.in.Alaska..Square.Meters.))+ geom_point()
TreeCoverLoss.graph <- TreeCoverLoss.graph + geom_smooth(method="lm", col="red")
TreeCoverLoss.graph

#Snowfall
snowfallData = read.csv("/Users/Viven/Group49CSVData/snowfall.csv")
snowfall.year.lm <- lm(Snowfall..mm. ~ Year, data = snowfallData)
summary(snowfall.year.lm)
snowfall.graph<-ggplot(snowfallData, aes(x=Year, y=Snowfall..mm.))+ geom_point()
snowfall.graph <- snowfall.graph + geom_smooth(method="lm", col="red")
snowfall.graph

#Greenhouse Gas Emissions Per Capita
emissionsData = read.csv("/Users/Viven/Group49CSVData/greenhouse_gas_emissions_per_capita.csv")
emissions.year.lm <- lm(Total.GHG.excl..LULUCF.per.capita..KG. ~ Year, data = emissionsData)
summary(emissions.year.lm)
emissions.graph<-ggplot(emissionsData, aes(x=Year, y=Total.GHG.excl..LULUCF.per.capita..KG.))+ geom_point()
emissions.graph <- emissions.graph + geom_smooth(method="lm", col="red")
emissions.graph

#Surface Temperature in Celcius
surfaceTemperatureData = read.csv("/Users/Viven/Group49CSVData/combinedData.csv")
surfaceTemperature.year.lm <- lm(Surface.Temperature..C. ~ Year, data = surfaceTemperatureData)
summary(surfaceTemperature.year.lm)
surfaceTemperature.graph<-ggplot(surfaceTemperatureData, aes(x=Year, y=Surface.Temperature..C.))+ geom_point()
surfaceTemperature.graph <- surfaceTemperature.graph + geom_smooth(method="lm", col="red")
surfaceTemperature.graph

#Coombined data
combinedData = read.csv("/Users/Viven/Group49CSVData/combinedData.csv")
summary(combinedData)