rm(list = ls(all = TRUE)) # erase everything before start

# Before running first time, check that packages are installed
library(lme4) # Stats (mixed models)
library(plyr) # fancy ways to reorganize data frames
library(ggplot2) # graphs
source("http://semanticsarchive.net/Archive/GRhZmM4N/ParsimoniousMM.R") # more stats


FOLDERA <- "/Users/alexandrecremers/Dropbox/introspection/Analysis/"
FOLDERN <- "/home/nadine/Dropbox/experiments/introspection/Analysis/" # Path to your dropbox analysis folder

if (file.exists(FOLDERA)) {FOLDER <- FOLDERA} else {FOLDER<-FOLDERN}


# Two ways to assign stuff: <- or =
y<-c("date","IP","controller","itemNB", "elementNB","itemID","group","content","answer")
dataA<-read.csv(paste(FOLDER,"resultsA.csv",sep=""),comment.char="#",header=F,col.names=y)
dataB<-read.csv(paste(FOLDER,"resultsB.csv",sep=""),comment.char="#",header=F,col.names=y)

dataA$Version<-"A"
dataB$Version<-"B"
data<-rbind(dataA,dataB)

# Look at the data:

head(data)
summary(data)
table(data$itemID)

# Look at specific parts of it: (don't do that with 100 participants: too big)
#subset(data,itemID=="instructions")

# Remove our own runs:
data<-subset(data,!IP%in%c("ec4ccfbb0a757ef81fa06de8b6e5a2b6","c55158f2c494e4d3a515dc8279b5459c","5147a6f6b82e2e021e4ce3368d729868"))
data$IP<-factor(data$IP)

################
# Participants
################

# Align response times with answers:

data<-ddply(data,c("IP","itemID"),function(df){
	df1<-df;
	df1$RT<-df1$answer[df1$content=="_REACTION_TIME_"];
	df1<-df1[!df1$content=="_REACTION_TIME_",];
	return(df1)
})
data$RT<-as.numeric(data$RT)

data$answer<-as.character(data$answer)
infos.subjects<-ddply(data, c("IP"),function(df)c(
		DATE = as.character(df$Date)[1],
		IP =  as.character(df$IP)[1],
		MTURKID =  df$answer[df$content=="mturkid"][1],
		AGE =  as.numeric(df$answer[df$content=="age"])[1],
		LANG =  df$answer[df$content=="language"][1],
		VERSION = as.character(df$Version)[1],
		MeanRT = mean(df$RT[!df$itemID%in%c("questionnaire","instructions")])/1000,
		MedianRT = round(median(df$RT[!df$itemID%in%c("questionnaire","instructions")])/1000,1)	
		))
infos.subjects$MeanRT<-as.numeric(infos.subjects$MeanRT)
infos.subjects$MedianRT<-as.numeric(infos.subjects$MedianRT)


plot(sort(infos.subjects$MedianRT),ylim=c(0,15))

# They all speak English, but so many are just unable to write "English" properly...
#other.lang<-subset(infos.subjects$IP,!infos.subjects$LANG %in% c("English", "english","ENglish",'Eglish',"ENGLISH",'en', 'Enlish',"English "))
other.lang<-NULL

############################
# Compare to MTurk data and
# find missing participants
############################

MTurkData<-read.csv(paste(FOLDER,"Batch_2621448_batch_results.csv",sep=""))

infos.subjects$MTURKID[infos.subjects$MTURKID==" A36BQYQGN6OWVU"]<-"A36BQYQGN6OWVU"
setdiff(MTurkData$WorkerId,infos.subjects$MTURKID)

# Missing two participants:
length(unique(infos.subjects$MTURKID))
"A299CU7U9QX3E7"%in%infos.subjects$MTURKID
sort(infos.subjects$MTURKID)


#########################
# Filter useless things
#########################


data2<-subset(data,!IP%in%other.lang&!itemID%in%c("instructions","questionnaire","training1","training2","training3","training4","training5"),select=c(-controller,-elementNB))

#redefine factors to remove unused levels:
data2$itemID<-factor(data2$itemID)

# Convert to character, and split along the _
tmp<-data.frame(do.call('rbind', strsplit(as.character(data2$content),split="_",fixed=T)))
tmp$X2<-sub("item=","",tmp$X2)
tmp$X3<-sub("role=","",tmp$X3)
names(tmp)<-c("Player","Item","Role")
data2<-cbind(data2,tmp)
data2<-subset(data2,select=-content)

# Make 'answer' logical
table(factor(data2$answer))
data2$Answer<-(data2$answer=="yes")
table(data2$Answer)

####################
# Errors on fillers
####################

fill.data<-subset(data2,!Item%in%c("UA","OA","OD","UD"))
fill.data$Expected<-NA
fill.data$Expected[fill.data$Item=="TrueTrueFalseFiller"]<-ifelse(fill.data$Role[fill.data$Item=="TrueTrueFalseFiller"]=='false',F,T)
# Sometimes the "truecontrolSE" is wrong about the shape. How can we tell when?
fill.data$Expected[fill.data$Item=="whichSymbolFiller"&fill.data$Role=="UDtargetTrue"]<-T
fill.data$Expected[fill.data$Item=="whichSymbolFiller"&fill.data$Role=="falsecontrol"]<-F
fill.data$Expected[fill.data$Item=="winFiller"&grepl('lose',fill.data$itemID)&fill.data$Role=='truecontrol']<-T
fill.data$Expected[fill.data$Item=="winFiller"&grepl('lose',fill.data$itemID)&fill.data$Role=='falsecontrolSE']<-F
fill.data$Expected[fill.data$Item=="winFiller"&grepl('win',fill.data$itemID)&fill.data$Role=='falsecontrol']<-F
fill.data$Expected[fill.data$Item=="winFiller"&grepl('win',fill.data$itemID)&fill.data$Role=='truecontrolSE']<-T

table(fill.data$Expected,useNA="ifany")
unique(paste(fill.data$itemID[is.na(fill.data$Expected)],fill.data$Role[is.na(fill.data$Expected)]))

fill.data$Correct<-fill.data$Answer==fill.data$Expected
mean(fill.data$Correct,na.rm=T)

infos.subjects$ER<-100-100*tapply(fill.data$Correct,fill.data$IP,mean,na.rm=T)

# 
accER<-mean(infos.subjects$ER)+sd(infos.subjects$ER)

excluded<-infos.subjects$IP[infos.subjects$ER>accER]
plot(ER~MeanRT,data=infos.subjects,log="x");abline(h=accER,col="red")

length(excluded)


#################
# Graph Fillers:
#################

fill.data$Item[grepl("lose",fill.data$itemID)]<-'loseFiller'

plot.data.Fill<-aggregate(Correct~Role+Item+Version+IP,FUN=mean,data=subset(fill.data,!Item%in%c("UA","OA","OD","UD")))
plot.data.Fill.agg<-ddply(subset(plot.data.Fill),c("Role","Version","Item"),function(df)c(response=100*mean(df$Correct),se=100*se(df$Correct)))

pFill<-ggplot(data= plot.data.Fill.agg,aes(x=Role,y=response,fill=Version))+
facet_grid(.~Item,scale="free")+
geom_bar(position=position_dodge(), stat="identity",colour="black")+
geom_errorbar(aes(ymin=response-se, ymax=response+se),
                  width=.2,                    # Width of the error bars
                  position=position_dodge(.9)) +
theme(axis.text.x = element_text(angle=90))+
ylab("% Correct")
print(pFill)

# Look at error rate on the "lose" fillers:

loseFill.byPart<-aggregate(Correct~IP,FUN=mean,data=subset(fill.data,Item=="loseFiller"))
plot(sort(loseFill.byPart$Correct))

good.losers<-loseFill.byPart$IP[loseFill.byPart$Correct>.6]
length(good.losers)


# Look at effects of Version on win/lose, for participants who paid attention only.
plot.data.Win<-aggregate(Answer~Role+Item+Version+IP,FUN=mean,data=subset(fill.data,!Item%in%c("UA","OA","OD","UD")))
plot.data.Win.agg<-ddply(subset(plot.data.Win,Item%in%c("winFiller","loseFiller")&IP%in%good.losers),c("Role","Version","Item"),function(df)c(response=100*mean(df$Answer),se=100*se(df$Answer)))
pWin<-ggplot(data= plot.data.Win.agg,aes(x=Role,y=response,fill=Version))+
facet_grid(.~Item,scale="free")+
geom_bar(position=position_dodge(), stat="identity",colour="black")+
geom_errorbar(aes(ymin=response-se, ymax=response+se),
                  width=.2,                    # Width of the error bars
                  position=position_dodge(.9)) +
theme(axis.text.x = element_text(angle=90))+
ylab("% Select")
print(pWin)

#############
# Remove excluded

data2.bak<-data2
data2<-subset(data2,!IP%in%excluded & IP%in% good.losers)


#################
# Graph targets:
#################

plot.data<-aggregate(Answer~Role+Item+Version+IP,FUN=mean,data=subset(data2,Item%in%c("UA","OA","OD","UD")))
plot.data.agg<-ddply(plot.data,c("Role","Version","Item"),function(df)c(response=100*mean(df$Answer),se=100*se(df$Answer)))

p<-ggplot(data=plot.data.agg,aes(x=Role,y=response,fill=Version))+
facet_grid(.~Item)+
geom_bar(position=position_dodge(), stat="identity",colour="black")+
geom_errorbar(aes(ymin=response-se, ymax=response+se),
                  width=.2,                    # Width of the error bars
                  position=position_dodge(.9))

print(p)

# Aggregate all control conditions together:

plot.data2<-plot.data
plot.data2$Role[plot.data2$Role=="target"]<-paste(plot.data2$Item[plot.data2$Role=="target"],plot.data2$Role[plot.data2$Role=="target"],sep="-")

plot.data.agg2<-ddply(plot.data2,c("Role","Version"),function(df)c(response=100*mean(df$Answer),se=100*se(df$Answer)))
plot.data.agg2$Role<-factor(plot.data.agg2$Role,levels=c("truecontrolSE","UD-target","OA-target","UA-target","OD-target","falsecontrol"),labels=c("True","UD","OA","UA","OD","False"))
p2<-ggplot(data=plot.data.agg2,aes(x=Role,y=response,fill=Version))+
geom_bar(position=position_dodge(), stat="identity",colour="black")+
geom_errorbar(aes(ymin=response-se, ymax=response+se),
                  width=.2,                    # Width of the error bars
                  position=position_dodge(.9))
print(p2)




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
model4<-glmer(Answer~Item+(1+Item|date),family=binomial(),data= stat.data)
summary(model4)
stat.data$Item<-factor(stat.data$Item)
contrasts(stat.data$Item)

contrasts(stat.data$Item)

stat.data$IE<-ifelse(stat.data$Item=="UD",1,0)
stat.data$WE<-ifelse(stat.data$Item=="UD"|stat.data$Item=="OA",1,0)
stat.data$MS<-ifelse(stat.data$Item=="UD"|stat.data$Item=="UA",1,0)
# Mamy participants actually seem to have this "weak non-exhaustive" reading:
stat.data$WNE<-ifelse(stat.data$Item=="OD",0,1)

stat.data$Version<-factor(stat.data$Version,levels=c("B","A"))

model5<-glmer(Answer~(1+IE+WE+WNE)*Version+(1+IE+WE+ WNE |IP),family=binomial(),data=stat.data)
summary(model5) # Most likely won't work

model5b<-parsimonious(model5)
summary(model5b) # Don't trust those p-values

# Tests for all possible effects of Version on possible readings:
model5b<-update(model5b,data=model.frame(model5b),REML=T)
model5b0<-update(model5b,.~.-(1+IE+WE+MS)*Version+(1+IE+WE+MS)+Version)
anova(model5b,model5b0)


##########################
# Categorize participants
##########################

by.subject<-ddply(stat.data,c("IP","Item","Version"),function(df)c(Answer=mean(df$Answer)))
by.subject<-reshape(by.subject,timevar="Item",idvar=c("IP","Version"),v.names="Answer",direction="wide")
names(by.subject)<-c("IP","Version","OA","OD",'UA',"UD")
by.subject$Category<-NA
by.subject$Category[pmax(by.subject$OA,by.subject$OD,by.subject$UA,by.subject$UD)<.5]<-"SE"
by.subject$Category[pmax(by.subject$OA,by.subject$OD,by.subject$UA)<.5&by.subject$UD>.5]<-"IE"
by.subject$Category[pmax(by.subject$OD,by.subject$UA)<.5&pmin(by.subject$OA,by.subject$UD)>.5]<-"WE"
by.subject$Category[pmax(by.subject$OA,by.subject$OD)<.5&pmin(by.subject$UA,by.subject$UD)>.5]<-"MS"
by.subject$Category[pmax(by.subject$OA)<.5&pmin(by.subject$UA,by.subject$UD)>.5]<-"MS+OD"
by.subject$Category[pmax(by.subject$OD)<.5&pmin(by.subject$UA,by.subject$UD,by.subject$OA)>.5]<-"WE+UA"
table(by.subject$Category,by.subject$Version,useNA="ifany")

