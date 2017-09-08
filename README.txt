###################################
######   nate's project 1   #######
###################################

I implemented everything for this lab except the third extra credit assignment. 
As far as bugs go, I think the only bug or only major bug is in my mult func which doesnt work for some values
I tried finding other bugs for other functions but I think I already solved them. 

Some of my functions may seem longer than what you may expect but I tried making my functions as streamlined as possible in terms
of complexity or calling break after everything I needed to be done in a function was performed. 

As far as error checking goes, I implemeted some of the more major error checkings you would expect.
I handled these approiatly by making either negative numbers positive or calling sys exit.

Interestingly enough I used a throw catch statement to test if a number was negative. I did this by catching the error "index error"
and that could only happend for a negative number. 

Lastly I created some of my functions OUTSIDE of my class then called them in my class. I did this because I dont want to run recursion
on a crazy amount of bigint and have all the over head from constructing a new bigint. So my functions are designed to minimize this and
work with the basic array.