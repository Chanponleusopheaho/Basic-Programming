import requests
from bs4 import BeautifulSoup
while True:
  print("This is a program to know your horoscope:")
  date = int(input("Enter your  birth date: \n"))

  if date > 31:
    print("Please enter the correct date. The date should not exceed 31\n")
    continue

  month = int(input("Enter your birthday month in number format ( for example 1 for January, 2 for February,..... and  12 for December ): \n"))

  if month > 12:
    print("Please enter the correct month. The month should not exceed 12\n")
    continue


  if month == 12:
    if (date < 22): sign = 'Sagittarius'
    else: 'Capricorn'
  elif month == 1:
    if (date < 20): sign = 'Capricorn'
    else: 'Aquarius'
  elif month == 2:
    if (date < 19): sign = 'Aquarius'
    else: 'Pisces'
  elif month == 3:
    if (date < 21): sign = 'Pisces'
    else: 'Aries'
  elif month == 4:
    if (date < 20): sign = 'Aries'
    else: 'Taurus'
  elif month == 5:
    if (date < 21): sign = 'Taurus'
    else: 'Gemini'
  elif month == 6:
    if (date < 21): sign = 'Gemini'
    else: 'Cancer'
  elif month == 7:
    if (date < 23):sign = 'Cancer'
    else: 'Leo'
  elif month == 8:
    if (date < 23): sign = 'Leo'
    else: 'Virgo'
  elif month == 9:
    if (date < 23): sign = 'Virgo'
    else: 'Libra'
  elif month == 10:
    if (date < 23): sign = 'Libra'
    else: 'Scorpio'
  elif month == 11:
    if (date < 22): sign = 'Scorpio'
    else: 'Sagittarius'

  print("\nYour Astrological sign is :",sign)

  user=input("\nDo you want to read your horoscope?\nEnter Y to read your scope and N to exit\n")


  def horoscope(zodiac_sign: int, day: str) -> str:
      url = (
          "https://www.horoscope.com/us/horoscopes/general/"
          f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
      )
      soup = BeautifulSoup(requests.get(url).content,
                          "html.parser")

      # print(soup.find("div", class_="main-horoscope").p.text)
      return soup.find("div", class_="main-horoscope").p.text


  if __name__ == "__main__":
      dic = {'Aries': 1, 'Taurus': 2, 'Gemini': 3,
            'Cancer': 4, 'Leo': 5, 'Virgo': 6,
            'Libra': 7, 'Scorpio': 8, 'Sagittarius': 9,
            'Capricorn': 10, 'Aquarius': 11, 'Pisces': 12}

      print('Choose your zodiac sign from below list : \n',
            '[Aries,Taurus,Gemini,Cancer,Leo,Virgo,Libra,\
            Scorpio,Sagittarius,Capricorn,Aquarius,Pisces]')

      zodiac_sign = dic[input("Input your zodiac sign : ")]
      print("On which day you want to know your horoscope ?\n",
            "Yesterday\n", "Today\n", "Tomorrow\n")

      day = input("Input the day : ").lower()
      horoscope_text = horoscope(zodiac_sign, day)
      print(horoscope_text)

  if user=='Y':
    print("Here is your horoscope!!!!")

    if sign=="Sagittarius":
      print("\nYou hate people telling you what to do. However, rarely do you do anything, \n"
          "other than complain. You take your own path even if the Google/Apple Maps is \n"
          "showing you that you are heading towards a landfill.\n")
    elif sign=='Capricorn':
      print("\nYou are too calculative for the people around you. The reason you get ahead is\n"
          "not because you are smarter, but because you are a perfect con. The karma is \n"
          "around and it is watching you.\n")
    elif sign == "Aquarius":
      print("\nFocus on one thing in your life for once! Stop being a flake and actually do one\n"
          "thing you promised people. Your communication skills this week are worse than\n"
          "Babu Bhaiyaa. Speak up!\n")
    elif sign == "Pisces":
      print("\nYou need to come back to earth. datedreaming and maxing your credit card won’t make \n"
          "you happy. Neither would alcohol dependence to drown your sorrows. You are popular \n"
          "among your friends because you have a free stash.\n")
    elif sign == "Aries":
      print("\nYour impulsive nature gets you into a lot of trouble. It has also created a hole in \n"
          "your pocket. Do yourself a favor and get on that bus that goes nowhere.Since you are\n"
          "very ambitious and loud, there will surely be a way out.\n")
    elif sign == "Taurus":
      print("\nYou are often called stubborn. There is a reason for it. You want to win an argument \n"
          "even if it’s with a child. You will also be chased by the street dog on the way home \n"
          "this week. Keep your eyes open.\n")
    elif sign == "Gemini":
      print("\nThe voices in your head are getting louder and your neighbors are starting to notice.\n"
          "Your positive karmic cycle is all wrong kinds of screwed up. You will spot your crush \n"
          "or the love of your life. With someone ELSE.\n")
    elif sign == "Cancer":
      print("\nYou need to stop crying about why that waiter gave you cold food. You crustaceans are \n"
          "moody enough to make stale cheese. You claim yourself to be a wanderer and a dreamer, \n"
          "however, you never leave your stinky shell to do anything risky or new.\n")
    elif sign == "Leo":
      print("\nYou will miss all your deadlines this week. While you are running to be on time for that\n"
          "one meeting, your shoes will fall apart. Also, a child beggar on the street will harass \n"
          "you till you lose your faith in humanity.\n")
    elif sign == "Virgo":
      print("\nYou need to stop waiting for your mom to clean your laundry. You stink, literally. Your \n"
          "watchman thinks of garbage collector whenever you are around. Take a shower, and do planet\n"
          "earth a favor.\n")
    elif sign == "Libra":
      print("\nTalking your way out of problems does not mean the problems are resolved. When you are done\n"
          "deciding what to eat for lunch, you need to get back to life. Your constant confusion\n"
          "is showing, clearly!\n")
    elif sign == "Scorpio":
      print("\nThere is one thing that you love more than your reflection. Your photograph. Strangers think\n"
          "you are mysterious, but they don’t realize that you are a creep, waiting to be found out. \n"
          "You think you are smooth and can be the life of the party, but you aren’t getting invited to the right ones.\n")

  elif user=="N":
    print('Thank You for your time!!')
    break

  else:
    print("Invalid Input, Please enter the correct input.")


