#Thomas Livshits
#CS-370
import random
import re
#Starting Message
print("I am Jaxbot. I am a bot that has certain knowledge on The 2007 Giants.")
#name
botname = 'Jax'
WName = ['what is your name','whats your name',"what's your name"]
WResponse = "My name is " + str(botname)
QJob = ["what do you do","who are you","what is your job","how can you help me","purpose"]
Job = "I am a bot that has certain knowledge on The 2007 Giants."
#Greetings
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey','Hello','Sup','sup','Yo','yo','hello jaxbot','hello jax']
question = ['how are you','how are you doing',"what's up","Whats up", "whats up"]
responses = ['Okay',"I'm fine","Alright","Not Bad"]
#Love
Wlove_question = ['what is love','Watt is love']
Wlove_response = "Baby don't Hertz me,don't Hertz me. No Morse."
#life
life_question = ['what is life','what is the purpose of life']
life_response = ['42','To live','To Repoduce','How should I know? Ask another question']
#why?
Qwhy = "why"
Rwhy = "Why Not?"
#exit
exitthis = ["bye","cya","have a nice day","goodbye","exit"]
#2007 Giants

#players
QPlayers = ["who are the players","players","roster","team roster"]
RPlayers = "The rooster for the 2007 Giants is Jay Alford,Adrian Awasom,Chase Blackburn,Kevin Boothe,Kevin Boss,Ahmad Bradshaw,Plaxico Burress,James Butler,Barry Cofield,Craig Dahl,Torrance Daniels,Russell Davis,Zak DeOssie,David Diehl,Kevin Dockery,Robert Douglas,Reuben Droughns,Jeff Feagles,Madison Hedgecock,Domenik Hixon,Brandon Jacobs,Michael Johnson,Mathias Kiwanuka,Adam Koets,Jared Lorenzen,Sam Madison,Eli Manning,Michael Matthews,Kareem McKenzie,R.W. McQuarters,Kawika Mitchell,Anthony Mix,Sinorice Moss,Shaun O'Hara,Patrick Pass,Antonio Pierce,Geoffrey Pope,Fred Robbins,Aaron Ross,Grey Ruegamer,Rich Seubert,Jeremy Shockey,Steve Smith,Chris Snee,Michael Strahan,Dave Tollefson,Amani Toomer,Reggie Torbo,Justin Tuck,Lawrence Tynes,David Tyree,Osi Umenyiora,Derrick Ward,Danny Ware,Corey Webster,Guy Whimper,Gerris Wilkinson,Gibril Wilson,Anthony Wright,Manuel Wright"

#player stats
QPlayerstats = ["player stats","What are the player stats"]
RPlayerstats = "Just type the name of the player."

Qjayalford = "jay alford"

Qadrianawasom = "adrian awasom"

Qchaseblackburn = "chase blackburn"
	
Qkevinboothe = "kevin boothe"	

Qkevinboss = "kevin boss"	

Qahmadbradshaw = "ahmad bradshaw"
	
Qplaxicoburress = "plaxico burress"
Rplaxicoburress	= "Age:30 Pos:WR Summary: 70 catches for 1,025 yards, 12 td	Drafted: Pittsburgh Steelers / 1st / 8th pick / 2000"	

Qjamesbutler = "james butler"	
Rjamesbutler = "Age:25 Pos:SS Summary: 0.0 sacks, 1 interception, 1 fumble recovered"	

Qbarrycofield = "barry cofield"	
Rbarrycofield = "Age:23 Pos:NT Summary:1.0 sacks, 0 interceptions, 0 fumbles recovered	Drafted: New York Giants / 4th / 124th pick / 2006"

Qcraigdahl = "craig dahl"

Qtorrancedaniels = "torrance daniels"

Qrusselldavis	= "russell davis"
	
Qzakdeossie = "zak deossie"	

Qdaviddiehl = "david diehl"
Rdaviddiehl = "Age:27 Pos:LT Drafted:New York Giants / 5th / 160th pick / 2003"
	
Qkevindockery = "kevin dockery"	

Qrobertdouglas = "robert douglas"
	
Qreubendroughns = "reuben droughns"
	
Qjefffeagles = "jeff feagles"	
Rjefffeagles = "Age:41 Pos:P Summary: 71 punts for a 40.4 average, 1 blocked"	

Qmadisonhedgecock = "madison hedgecock"	
Rmadisonhedgecock= "Age: 26 Pos:FB Summary:0 rushes for yards, 0 td, & 6 catches for 45 yards and 0 td	Drafted: St. Louis Rams / 7th / 251st pick / 2005"

Qdomenikhixon	= "domenik hixon"
	
Qbrandonjacobs = "brandon jacobs"
Rbrandonjacobs ="Age: 25 Pos:RB Summary: 202 rushes for 1,009 yards, 4 td, & 23 catches for 174 yards and 2 td	Drafted: New York Giants / 4th / 110th pick / 2005"
	
Qmichaeljohnson = "michael johnson"
	
Qmathiaskiwanuka = "mathias kiwanuka"
Rmathiaskiwanuka = "Age:24 Pos:LB Drafted:New York Giants / 1st / 32nd pick / 2006"
	
Qadamkoets = "adam koets"
	
Qjaredlorenzen = "jared lorenzen"
	
Qsammadison = "sam madison"
Rsammadison = "Age:33 Pos:RCB Summary:1.0 sacks, 4 interceptions, 1 fumble recovered	Drafted: Miami Dolphins / 2nd / 44th pick / 1997"
	
Qelimanning = "eli manning"
Relimanning = "Age: 26 Pos: QB Summary: 297 for 529, 3,336 yards, 23 td, 20 int, & 29 rushes for 69 yards and 1 td Drafted : San Diego Chargers / 1st / 1st pick / 2004"	

Qmichaelmatthews = "michael matthews"	

Qkareemmckenzie = "kareem mckenzie"
RkareemmcKenzie	= "Age:28 Pos:RT Summary:1 fumble recovered Drafted: New York Jets / 3rd / 79th pick / 2001"
	
RQrwmcquarters = "r.w. mcquarters"
	
Qkawikamitchell = "kawika mitchell"
Rkawikamitchell = "Age:28 Pos:LB Drafted:Kansas City Chiefs / 2nd / 47th pick / 2003"
	
Qanthonymix = "anthony mix"	

Qsinoricemoss	 = "sinorice moss"
	
Qshaunohara = "shaun ohara"	
Rshaunohara = "Age:30 Pos:C"	

Qpatrickpass = "patrick pass"	

Qantoniopierce = "antonio pierce"
Rantoniopierce= "Age:29 Pos:MLB 1.0 sacks, 1 interception, 2 fumbles recovered"
	
Qgeoffreypope = "geoffrey pope"	

Qfredrobbins = "fred robbins"	
Rfredrobbins= "Age:30 Pos:DT Drafted:Minnesota Vikings / 2nd / 55th pick / 2000"

Qaaronross = "aaron ross"	
Raaronross= "Age:25 Pos:LCB 1.5 sacks, 3 interceptions, 0 fumbles recovered	Drafted:New York Giants / 1st / 20th pick / 2007"
Qgreyruegamer	 = "grey ruegamer"	

Qrichseubert = "rich seubert"	
Rrichseubert= "Age:28 	Pos:LG"	

Qjeremyshockey = "jeremy shockey"	
Rjeremyshockey= "Age:27 Pos:TE 57 catches for 619 yards, 3 td, & 1 rush for 6 yards and 0 td	Drafted:New York Giants / 1st / 14th pick / 2002"

Qstevesmith = "steve smith"	

Qchrissnee = "chris snee"
Rchrissnee= "Age:25 Pos:RG 1 fumble recovered	Drafted:New York Giants / 2nd / 34th pick / 2004"
	
Qmichaelstrahan = "michael strahan"	
Rmichaelstrahan= "Age:36 Pos:DE Drafted:New York Giants / 2nd / 40th pick / 1993"

Qdavetollefson = "dave tollefson"
	
Qamanitoomer = "amani toomer"	
Ramanitoomer = "Age: 33 Pos:WR Summary:59 catches for 760 yards, 3 td	Drafted: New York Giants / 2nd / 34th pick / 1996"

Qreggietorbor = "reggie torbor"	

Qjustintuck = "justin tuck"
	
Qlawrencetynes = "lawrence tynes"
	
Qdavidtyree = "david tyree"	

Qosiumenyiora = "osi umenyiora"	
Rosiumenyiora = "Age:26 Pos:DE Drafted:New York Giants / 2nd / 56th pick / 2003"

Qderrickward = "derrick ward"	

Qdannyware = "danny ware"

Qcoreywebster = "corey webster"	

Qguywhimper = "guy whimper"	

Qgerriswilkinson = "gerris wilkinson"	

Qgibrilwilson = "gibril wilson"	
Rgibrilwilson = "Age:26	Pos:FS Summary:0.0 sacks, 4 interceptions, 1 fumble recovered	Drafted:New York Giants / 5th / 136th pick / 2004"

Qanthonywright = "anthony wright"

Qmanuelwright = "manuel wright"	

#Games

GameInfo = ["games","games played","what are the games played by the Gaints"]
RGameInfo = "Week 1: VS Dallas Cowboys,Week 2: VS Green Bay Packers,Week 3: VS Washington Redskins,Week 4: VS Philadelphia Eagles, Week 5: VS New York Jets, Week 6: VS Atlanta Falcons,Week 7: VS San Francisco 49ers, Week 8: VS Miami Dolphins, Week 9: BYE Week ( no game), Week 10: VS Dallas Cowboys, Week 11: VS Detroit Lions, Week 12: VS Minnesota Vikings, Week 13: VS Chicago Bears, Week 14: VS Philadelphia Eagles, Week 15: VS Washington Redskins, Week 16: VS Buffalo Bills, Week 17: VS New England Patriots, Wild Card: VS Tampa Bay Buccaneers, Division: VS Dallas Cowboys, Conf. Champ: VS Green Bay Packers, SuperBowl: VS New England Patriots"
InfoGameInfo = "Enter a week to get more info. Example: Week 1."

week1 = "week 1"
Rweek1 = "Opp: Cowboys Result:L Score:35-45 Date:Sept 9"
week2 = "week 2"
Rweek2 = "Opp: Packers Result:L Score:13-35 Date:Sept 16"
week3 = "week 3"
Rweek3 = "Opp: Redskins Result:W Score:24-17 Date:Sept 23"
week4 = "week 4"
Rweek4 = "Opp: Eagles Result:W Score:16-3 Date:Sept 30"
week5 = "week 5"
Rweek5 = "Opp: Jets Result:W Score:16-3 Date:Oct 7"
week6 = "week 6"
Rweek6 = "Opp: Falcons Result:W Score:31-10 Date:Oct 15"
week7 = "week 7"
Rweek7 = "Opp: 49ers Result:W Score:33-15 Date:Oct 21"
week8 = "week 8"
Rweek8 = "Opp: Dolphins Result:W Score:13-10 Date:Oct 28"
week9 = "week 9"
Rweek9 = "BYE Week, No Game"
week10 = "week 10"
Rweek10 = "Opp: Cowboys Result:L Score:20-31 Date:Nov 11"
week11 = "week 11"
Rweek11 = "Opp: Lions Result:W Score:16-10 Date:Nov 18"
week12 = "week 12"
Rweek12 = "Opp: Vikings Result:L Score:17-41 Date:Nov 25"
week13 = "week 13"
Rweek13 = "Opp: Bears Result:W Score:21-16 Date:Dec 2"
week14 = "week 14"
Rweek14 = "Opp: Eagles Result:W Score:16-13 Date:Dec 9"
week15 = "week 15"
Rweek15 = "Opp: Redskins Result:L Score:10-22 Date:Dec 16"
week16 = "week 16"
Rweek16 = "Opp: Bills Result:W Score:38-21 Date:Dec 23"
week17 = "week 17"
Rweek17 = "Opp: Patriots Result:L Score:35-38 Date:Dec 29"
WildCard = "wild card"
RWildCard = "Opp: Buccaneers Result:W Score:24-14 Date:Jan 6"
Division = "division"
RDivision = "Opp: Cowboys Result:W Score:21-17 Date:Jan 13"
ConfChamp = ["conf. champ","conf champ","conference champion","conference champ"]
RConfChamp = "Opp: Packers Result:W in OT Score:23-20 Date:Jan 20"
SuperBowl = "superbowl"	
RSuperBowl = "Opp: Patriots Result:W Score:17-14 Date:Feb 3"
#start of the wall of if-else statements		
while True:
	userrawInput = raw_input(">>> ")
	userlowerInput = userrawInput.lower()
	userInput = re.sub('!.?','', userlowerInput)
	userInput = userInput.strip('?')
	userInput = userInput.strip('.')
	if userInput in greetings:
		random_greeting = random.choice(greetings)
		print(random_greeting)
	elif userInput in question:
		random_response = random.choice(responses)
		print(random_response)
	elif userInput in Qwhy:
		print(Rwhy)
	elif userInput in Wlove_question:
		response = Wlove_response
		print(response)
	elif userInput in WName:
		print(WResponse)
	elif userInput in life_question:
		random_life = random.choice(life_response)
		print(random_life)
	elif userInput in QJob:
		print(Job)
	elif userInput in QPlayers:
		print(RPlayers)
	elif userInput in QPlayerstats:
		print(RPlayerstats)
	elif userInput.lower() == Qplaxicoburress:
		print(Rplaxicoburress)
	elif userInput.lower() == Qjamesbutler:
		print(RQjamesbutler)
	elif userInput.lower() == Qbarrycofield:
		print(Rbarrycofield)
	elif userInput.lower() == Qdaviddiehl:
		print(Rdaviddiehl)
	elif userInput.lower() == Qjefffeagles:
		print(Rjefffeagles)
	elif userInput.lower() == Qmadisonhedgecock:
		print(Rmadisonhedgecock)
	elif userInput.lower() == Qosiumenyiora:
		print(Rosiumenyiora)
	elif userInput.lower() == Qamanitoomer:
		print(Ramanitoomer)
	elif userInput.lower() == Qmichaelstrahan:
		print(Rmichaelstrahan)
	elif userInput.lower() == Qchrissnee:
		print(Rchrissnee)
	elif userInput.lower() == Qjeremyshockey:
		print(Rjeremyshockey)
	elif userInput.lower() == Qrichseubert:
		print(Rrichseubert)
	elif userInput.lower() == Qaaronross:
		print(Raaronross)
	elif userInput.lower() == Qfredrobbins:
		print(Rfredrobbins)
	elif userInput.lower() == Qantoniopierce:
		print(Rantoniopierce)
	elif userInput.lower() == Qshaunohara:
		print(Rshaunohara)
	elif userInput.lower() == Qkawikamitchell:
		print(Rkawikamitchell)
	elif userInput.lower() == Qkareemmckenzie:
		print(Rkareemmckenzie)
	elif userInput.lower() == Qelimanning:
		print(Relimanning)
	elif userInput.lower() == Qsammadison:
		print(Rsammadison)
	elif userInput.lower() == Qmathiaskiwanuka:
		print(Rjefffeagles)
	elif userInput.lower() == Qbrandonjacobs:
		print(Rbrandonjacobs)
	elif userInput.lower() == week1:
		print(Rweek1)
	elif userInput.lower() == week2:
		print(Rweek2)
	elif userInput.lower() == week3:
		print(Rweek3)
	elif userInput.lower() == week4:
		print(Rweek4)
	elif userInput.lower() == week5:
		print(Rweek5)
	elif userInput.lower() == week6:
		print(Rweek6)
	elif userInput.lower() == week7:
		print(Rweek7)
	elif userInput.lower() == week8:
		print(Rweek8)
	elif userInput.lower() == week9:
		print(Rweek9)
	elif userInput.lower() == week10:
		print(Rweek10)
	elif userInput.lower() == week11:
		print(Rweek11)
	elif userInput.lower() == week12:
		print(Rweek12)
	elif userInput.lower() == week13:
		print(Rweek13)
	elif userInput.lower() == week14:
		print(Rweek14)
	elif userInput.lower() == week15:
		print(Rweek15)
	elif userInput.lower() == week16:
		print(Rweek16)
	elif userInput.lower() == week17:
		print(Rweek17)
	elif userInput.lower() == WildCard:
		print(RWildCard)
	elif userInput.lower() == Division:
		print(RDivision)
	elif userInput in ConfChamp:
		print(RConfChamp)
	elif userInput.lower() == SuperBowl:
		print(RSuperBowl)
	elif userInput in GameInfo:
		print(RGameInfo)
		print(InfoGameInfo)
	elif userInput in exitthis:
		print("Bye")
		exit()
	else:
		print("I did not understand what you said.")
		print('Reminder: I only have knownledge on subjects involving The 2007 Giants')
