#This ask date to know your zodiac sign
import requests
from bs4 import BeautifulSoup
from cfonts import render, say

output = render('Zodiac Sign', colors=['blue', 'yellow'], align='center')
print(output)
start_over='true'
while start_over =='true': 
  while True:
    print("Please enter your birthday to know your zodiac sign:")
    date = int(input("Enter your  birth date: \n"))

    if date >32:
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

    user =input("\nWhat do you want to know? \n1 Personality \n2 Prediction \n3 Compatability \nInput what you want to know:")
    start_over='true'
    while start_over =='true': 
      if user == "1" :
        print("Here is your Personality!!!!")

      if sign == "Sagittarius":
        print("\nYou hate people telling you what to do. However, rarely do you do anything, \n"
              "other than complain. You take your own path even if the Google/Apple Maps is \n"
              "showing you that you are heading towards a landfill.\n")
      elif sign == 'Capricorn':
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
      break

    if user == "2":
      import requests
      from bs4 import BeautifulSoup


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



          zodiac_sign = dic[sign]
          print("On which day you want to know your horoscope ?\n",
                "Yesterday\n", "Today\n", "Tomorrow\n")

          day = input("Input the day : ").lower()
          horoscope_text = horoscope(zodiac_sign, day)
          print(horoscope_text)
      break

    if user == "3": 
      print("Here is your Compatability")   
      if sign == "Sagittarius":
        print("Another Sagittarius or a Gemini would definitely be able to vibe with that type of inquisitive and energetic lifestyle. \nAries, another sign that loves to be active, may also be able to provide a firm, guiding hand where one is needed.")
        print("\nHere is your Non-Compatability")
        print("Sagittarius is too rambunctious for the likes of Capricorn and Taurus and isn’t skilled enough at communicating emotions to successfully date a Pisces.")
      
      elif sign == 'Capricorn':
        print("\nVirgos and other Capricorns appreciate and respect the drive this sign has, and they sympathize with the desire to be perfect.\nScorpios know that there is more to this sign than meets the eye, as they are often misunderstood themselves.")
        print("\nHere is your Non-Compatability")
        print("\nOn the other hand, Leo, Gemini, and Sagittarius view Capricorn as being overly serious and stodgy.")
      
      elif sign == "Aquarius":
        print("Aquarius will be best off with its own kind or with a Gemini, who is similarly energetic and nimble-minded. Libra,\n a proponent of fairness and lover of research, also lives up to the humanitarian inclinations of an Aquarius.")
        print("\nHere is your Non-Compatability")
        print("Scorpio’s way of thinking can be too convoluted for Aquarius, who prefers logic and openness to emotions and secrecy. Cancer,\n another water sign, won’t have much luck either for this reason. A Taurus definitely won’t jive with Aquarius either, since this is a sign that loves to turn everything on its head.")
      
      elif sign == "Pisces":
        print("Scorpio and Cancer are like Pisces in that they are deeply invested in emotional connections. Scorpio has a special fondness for this sign’s ability to think and to live abstractly,\n which fits Ridout’s assessment that Pisces needs “a partner who can navigate the world with them while diving deep into spiritual and artistic endeavors.”\n And while it may come as a surprise, it turns out that Capricorn is also a wonderful companion for Pisces—the ultimate example of how opposites attract.")
        print("\nHere is your Non-Compatability")
        print("Outgoing signs like Gemini, Sagittarius, and Leo don’t really speak the same language as contemplative Pisces, who can be gentle and shy.")
      
      elif sign == "Aries":
        print("Sagittarius is a great companion because people of this sign are adventurous and outgoing; the two will sustain each other’s energy.\n Gemini is a good match for similar reasons, while Libra could also forge a bond based on mutual respect and understanding.")
        print("\nHere is your Non-Compatability")
        print("Aries is too bullish for signs like Scorpio and Cancer. Virgo would also be an improper pairing because the two would constantly\n clash over what they see as the right course of action. The last thing you want is to be stressed in your relationship.")
      
      elif sign == "Taurus":
        print("The other earth signs, Capricorn and Virgo, make a great match for Taurus, as they share the same fundamental nature.\n (That’s basically the essence of zodiac compatibility.) Cancer is also a good choice, too, because they are just as passionate and caring as Taurus,\n and they take their dedication to their loved ones equally seriously.")
        print("\nHere is your Non-Compatability")
        print("For as much as Taurus loves opulence and sensuality, this sign does not appreciate show-offs when it comes to relationships.\n Leo, Aquarius, and Sagittarius are too excitable for Taurus, who prefers a more grounded temperament.")
      
      elif sign == "Gemini":
        print("As someone who can see two sides to any argument, Libra is perfectly suited to Gemini, the sign of the Twins.\n Where some might call Gemini two-faced, Libra understands that there is more to them than meets the eye. Additionally,\n Sagittarius and Aquarius share the same intellectual curiosity and need for exploration as Gemini.")
        print("\nHere is your Non-Compatability")
        print("Capricorn and Taurus do not like the unpredictable nature of this sign, which they see as flighty.\n Scorpio may also feel naturally distrustful of Gemini. While we’re on the subject.")
      
      elif sign == "Cancer":
        print("Scorpio and Pisces, two very intuitive and emotional signs, will deeply appreciate Cancer’s love and dedication. \nVirgo also loves to nurture and cherishes a reliable partner like Cancer.")
        print("\nHere is your Non-Compatability")
        print("Gemini, Sagittarius, and Leo are too independent and won’t satisfy Cancer, who needs to be needed.\n They’re not necessarily selfish, but they don’t crave that same level of domesticity.")
      
      elif sign == "Leo":
        print("Sagittarius, Aquarius, and Gemini share Leo’s aspirations and excitement, making them very suitable matches.\n Of course, zodiac compatibility isn’t always enough to avoid an argument—but knowing the best days to do certain things may help you avoid some of those bumps in the road.")
        print("\nHere is your Non-Compatability")
        print("Capricorn, Taurus, and Virgo can be too regimented for Leo, who may feel bogged down by their rules. \nThe earth signs tend to feel like Leos should get over themselves.")
      
      elif sign == "Virgo":
        print("Capricorn shares Virgo’s love for hard work and setting goals. Taurus and Scorpio are passionate and trusted potential partners.\n While they may not share the same North Star, Virgo admires the fact that these signs have their own code of conduct to live by.")
        print("\nHere is your Non-Compatability")
        print("Sagittarius, Gemini, and Aquarius would likely wear on Virgo’s patience by testing boundaries or acting in a way that is unexpected.\n Believe it or not, there’s a similar process when picking the right pet for you.")
      
      elif sign == "Libra":
        print("Because Libra is so measured, partnering with another Libra is probably the most logical choice.\n People of this zodiac sign can also do well with an Aries or an Aquarius, who provide an intriguing challenge and mental stimulation.")
        print("\nHere is your Non-Compatability")
        print("One part of what makes love so wonderful is that initial spark, and Libra doesn’t usually feel that energy from Virgo or Capricorn.\nPisces can also be a poor fit by being too untethered to reality, preferring instead to live in a world of art, feeling, and dreams.")
      
      elif sign == "Scorpio":
        print("The other two water signs, Pisces and Cancer, also experience the world primarily through their emotions and can match the intensity of Scorpio. \nThese signs are willing to forge the powerful bonds that Scorpio secretly craves. Virgo loves trying to solve the puzzle that is Scorpio, and they also find that kind of long-term investment worthwhile. This thoughtful, nurturing earth sign is the kind of dedicated partner Scorpio needs.")
        print("\nHere is your Non-Compatability")
        print("Just as the head and the heart don’t always see eye to eye, Aquarius can be too cerebral for the sensual Scorpio. Leo and Aries are also ill-advised matches for Scorpio,\n whose determination to fulfill their own ambitions would cause conflict. If you’re looking to be more productive, there’s a right way and a wrong way to do it, depending on your zodiac sign.")
      break
  print("Do you interest in other plans of compound interest?")
  userResponse = input("Continue?(y/n): ")
  if userResponse =='y':
        start_over='true'
  else:
        start_over='false'
        from cfonts import render, say

        output = render('Thank You', colors=['green', 'yellow'], align='center')
        print(output)