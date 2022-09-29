import datetime
while True:
    try:
        userb = input("Enter your birthday in September 17 2002 form: ")
        birth = datetime.datetime.strptime(userb, "%B %d %Y")
        break
    except:
        print("Format is incorrect please try in September 17 2002 format!")
dayof = datetime.datetime.today()
answer = (dayof - birth).total_seconds()
print("You are ",answer, " seconds old")
# Enter your birthday as I have it formatted for script to work.
