This code piece check ther location of International Space Station and if it going above the user house it will notify the user via email
Put on cloud for real time updates

                                PROGRAME STRUCTURE IS AS FOLLOW;

- Variables (location points, credentials)
- function (inrange) that checks for the inrange of the iss after retreiving the location info of iss through iss api
- funciton (sstime) that gets the sunrise and sunset time using api converts it to the utc standard time and then converts it to the pakistan local time
- funtion (msgbody) that uses the time variables from the sstime and constructs the message body for the mail
- final a while loop to check and sent the mail to the target if the iss satisfies the inrange function
- dynamically place the daytime or nighttime scnerio in the message
