rm(list=ls())


library(MetaboAnalystR)

mSet<-InitDataObjects("conc", "stat", FALSE)
mSet<-Read.TextData(mSet, "gnps.csv", "rowu", "disc");
mSet<-SanityCheckData(mSet)
mSet<-ReplaceMin(mSet);
mSet<-SanityCheckData(mSet)
mSet<-FilterVariable(mSet, "none", "F", 25)
mSet<-PreparePrenormData(mSet)
mSet<-Normalization(mSet, "NULL", "NULL", "NULL", ratio=FALSE, ratioNum=20)
mSet <- MetaboAnalystR::ANOVA.Anal(mSetObj = mSet)


pvalue_df <- data.frame(cmpd = mSet$dataSet$cmpd,
                   pvalue = mSet$analSet$aov$p.value)
pvalue_df <- pvalue_df[order(pvalue_df$pvalue),]

top_pvalue_df <- pvalue_df[1:50,]


library('readxl')
library(pheatmap)
data <- read.csv('gnps.csv', check.names = F)

data2 <- data[,names(data) %in% top_pvalue_df$cmpd]

# 标注分组和标签
rownames(data2) = paste(data$ID)
# colnames(data2) = paste("C", 1:50, sep = "")
anno_col=data.frame(Group=factor(data$Group))
rownames(anno_col)=paste(data$ID)
pheatmap(t(data2),cluster_row=F,cluster_col=F,border=F,annotation_col=anno_col)

