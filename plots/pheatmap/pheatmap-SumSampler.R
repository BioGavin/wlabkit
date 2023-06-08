rm(list=ls())
library(pheatmap)
data<-read.csv("gnps.csv", check.names = F)
# Prepration,新建一个只剩数值的数据表data1
data1 <- data[,-c(1:2)]
# 新建丰度前50的数据表data2
data1Sum <- apply(data1,2,sum)
data1SumSort <- sort(data1Sum, decreasing = T)
Top <- data1SumSort[1:50]
data2 <- data1[,names(data1) %in% names(Top)]
# 标注分组和标签
rownames(data2) = paste(data$ID)
# colnames(data2) = paste("C", 1:50, sep = "")
anno_col=data.frame(Group=factor(data$Group))
rownames(anno_col)=paste(data$ID)
pheatmap(t(data2),cluster_row=F,cluster_col=F,border=F,annotation_col=anno_col)

