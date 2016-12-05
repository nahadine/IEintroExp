rm(list = ls(all = TRUE)) # erase everything before start

# Before running first time, check that packages are installed
library(lme4) # Stats (mixed models)
library(plyr) # fancy ways to reorganize data frames
library(ggplot2) # graphs
source("http://semanticsarchive.net/Archive/GRhZmM4N/ParsimoniousMM.R") # more stats

# Two ways to assign stuf: <- or =
y<-c("date","IP","controller","itemNB", "elementNB","itemID","group","content","answer")
data<-read.csv("/Users/alexandrecremers/Dropbox/Temp/results.csv",comment.char="#",header=F,col.names=y)

# Look at the data:

head(data)
summary(data)
table(data$itemID)

# Look at specific parts of it:
subset(data,itemID=="instructions")


data2<-subset(data,!itemID%in%c("instructions","training1","training2","training3","training4","training5"))

#redefine factors to remove unused levels:

data2$itemID<-factor(data2$itemID)


#### NOTE FOR LATER: CHECK RT #####

data2<-subset(data2,content!="_REACTION_TIME_")

# Convert to character, and split along the _
tmp<-data.frame(do.call('rbind', strsplit(as.character(data2$content),split="_",fixed=T)))
tmp$X2<-sub("item=","",tmp$X2)
tmp$X3<-sub("role=","",tmp$X3)

names(tmp)<-c("Player","Item","Role")

data2<-cbind(data2,tmp)

# Clean it up later

table(factor(data2$answer))
data2$Answer<-(data2$answer=="yes")
table(data2$Answer)

plot.data<-aggregate(Answer~Role+Item+date,FUN=mean,data=subset(data2,Item%in%c("UA","OA","OD","UD")))

plot.data.agg<-ddply(plot.data,c("Role","Item"),function(df)c(response=mean(df$Answer),se=se(df$Answer)))

p<-ggplot(data=plot.data.agg,aes(x=Role,y=response,fill=Role))+
facet_grid(.~Item)+
geom_bar(position=position_dodge(), stat="identity",colour="black")+
geom_errorbar(aes(ymin=response-se, ymax=response+se),
                  width=.2,                    # Width of the error bars
                  position=position_dodge(.9))

print(p)


#########
# Stats
#########

stat.data<-subset(data2,Item%in%c("UA","OA","OD","UD")&Role=="target")

# Basic linear model:
model1<-lm(Answer~Item+Role,data= stat.data)
summary(model1)

# Generalized linear model:
model2<-glm(Answer~Item+Role,family=binomial,data= stat.data)
summary(model2)
# Mixed-effects:
lmer

# Mixed-effect generalized:
model4<-glmer(Answer~Item+(1+Item|date),family=binomial,data= stat.data)
summary(model4)
stat.data$Item<-factor(stat.data$Item)
contrasts(stat.data$Item)

contrasts(stat.data$Item)

stat.data$IE<-ifelse(stat.data$Item=="UD",1,0)
stat.data$WE<-ifelse(stat.data$Item=="UD"|stat.data$Item=="OA",1,0)
stat.data$MS<-ifelse(stat.data$Item=="UD"|stat.data$Item=="UA",1,0)

model5<-glmer(Answer~(1+IE+WE+MS)*Version+(1+IE+WE+MS|date),family=binomial,data=stat.data)
summary(model5)





