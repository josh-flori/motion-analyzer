# the purpose of this script is to read the centroid values from tracking.py
# and basically created an animated plot as shown in the example in the readme.

library(gapminder)
library(ggplot2)

# centroid_values.csv should have two columns, labeled x and y.
# x should be an index from n:length(y) and y should be the concatenated
# list of centroid values provided by all runs of tracking.py

# adjust parameters to your liking
p=read.csv('/users/user/centroid_values.csv')
for (i in 1:nrow(p)) {
  # the following section helps create a moving plot.
  # if you want to change the values around, the first and fourth values (set as 130 and 21)
  # should sum up to 1 more than the second value (set as 150). the third values (set as 129)
  # should be 1 less than the first value.
  if (i<130){b=1
  e=150}
  else{b=i-129
  e=i+21}
  
  t=head(p,i)
  q<-ggplot(data=t, aes(x=x, y=y)) +
    geom_bar(stat="identity",width=1,color = "#D366E2",fill="#D366E2")+
    #ylim(min(p$y)-3,max(p$x)+3)+
    xlab("time (frames)")+
    ylab("distance moved (pixels)")+
    theme(axis.text.x=element_blank(),
          #axis.title.x=element_blank(),
          axis.ticks.x=element_blank(),
          #axis.text.y=element_blank(),
          #axis.title.y=element_blank(),
          axis.ticks.y=element_blank(),
          panel.background = element_rect(fill = 'black', colour = 'black'),
          panel.grid.major = element_line(colour="black"),
          panel.grid.minor = element_line(colour="black"))+
    scale_y_continuous(limits = c(min(p$y)-10,max(p$y)+10), expand = c(0, 0))+      
    scale_x_continuous(limits = c(b,e), expand = c(0, 0))
    ggsave(paste('/users/user/plot_output/output',i,'.jpg'),height=2,width=12,units="in")
}



















q<-ggplot(data=p, aes(x=x, y=y)) +
  geom_bar(stat="identity",width=1,color = "#D366E2",fill="#D366E2")+
  #ylim(min(p$y)-3,max(p$x)+3)+
  
  xlab("time (frames)")+
  ylab("distance moved (pixels)")+
  ggtitle("...") +
  theme(axis.text.x=element_blank(),
        #axis.title.x=element_blank(),
        axis.ticks.x=element_blank(),
        #axis.text.y=element_blank(),
        #axis.title.y=element_blank(),
        axis.ticks.y=element_blank(),
        panel.background = element_rect(fill = 'black', colour = 'black'),
        panel.grid.major = element_line(colour="black"),
        panel.grid.minor = element_line(colour="black"))
#scale_y_continuous(limits = c(min(p$y)-10,max(p$y)+10), expand = c(0, 0))+      
#scale_x_continuous(limits = c(b,e), expand = c(0, 0))
q
# ggsave(paste('/users/josh.flori/desktop/NEW.jpg'),height=3,width=17,units="in")
