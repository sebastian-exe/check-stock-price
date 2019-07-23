# check-stock-price
Checks the price of apple stock and send an email when the stock has reached the desired price. To change the stock 
another stock just change the ticker symbol in line 18. 


Code explanation:
Line 11 - 15 I was just debugging to make sure that the import stock info was actually working throuhg the terminal.

Future functionality:
I will be adding future functionality such as cryptos and showing what stock was the biggest gainer/loser of the day. 

To customize:
(Line 18)feel free to change the name of the applePrice variable to just simply price or to the desired company name.
(Lines 32 -33) to change the subject just change the contents within the colons, do the same to change the message within
the body.
(Lines 41-43) remember to change to the correct parameters in the server.sendmail. The first parameter is the from 
address,the second parrameter is the to addrress, and the third parameter is the message.
(Line 48)The value within the time.sleep() is in seconds, the default time is to check every minute, Feel free to change 
this to whatever you feel is appropiate.
