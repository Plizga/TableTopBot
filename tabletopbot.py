import discord
import random
from random import randint
TOKEN = "Placeholder"
client = discord.Client()

@client.event
async def on_message(message):
    """
    handles events involving messages.
    :param message: message submitted by user.
    """
    #Prevent bot from replying to itself
    if message.author == client.user:
        return
    #CONDITION !help
    if message.content.startswith("!help"):
        await client.send_message(message.channel, "Commands\n!samantha: Provides my backstory\n!roll: {x}d{y}+{z}\n!info: provides github\n!steak: provides steak\n")
    #CONDITION !roll
    if message.content.startswith("!roll"):
        strRoll = message.content.strip("!roll ")
        #if handles the + operator, else defines plus amount as null otherwise.
        if "+" in strRoll:
            plusAmount = strRoll[strRoll.find("+") +1:]
            strRoll = strRoll[:(strRoll.find("+"))] #strips the space and + and everything after
        else:
            plusAmount = None
        amount, die = strRoll.split("d", 1)
        rollSum = 0
        tupAddends = ()
        for i in range(int(amount)):
            newRoll = randint(1, int(die))
            random.seed()
            tupAddends = tupAddends + (newRoll,)
            rollSum += newRoll

        strFinal = ""
        for i in range(len(tupAddends)):
            if i != len(tupAddends) - 1:
                strFinal += str(tupAddends[i]) + " + "
            else:
                strFinal += str(tupAddends[i]) + " "
        #handles + factor
        if plusAmount is not None:
            strFinal += str("Plus " + str(plusAmount) + " ")
            rollSum += int(plusAmount)

        strFinal += "= {}"
        await client.send_message(message.channel, strFinal.format(rollSum))
    #CONDITION !info
    if message.content.startswith("!info"):
        await client.send_message(message.channel, "https://github.com/Plizga/TableTopBot")
    #CONDITION !steak
    if message.content.startswith("!steak"):
        await client.send_message(message.channel, "https://www.youtube.com/watch?v=9ShTGNJW5fM")
    #CONDITION !samantha
    if message.content.startswith("!samantha"):
        options = {0 : "i just got a presidential alert saying 'On October 4th, 2018 at 2:20 pm EST let's all go to mcdonalds and ask for the fortnite burger. The look on the workers face will be awesome' did anybody else get this???",
                   1 : "卂乃匚刀乇下厶卄工丁长乚从𠘨口尸㔿尺丂丅凵リ山乂丫乙",
                   2 : "Guys I really wanted to believe that Virginia Western was not the cesspool of morons all my fellow biology faculty told me it would be. Unfortunately your finals, which I purposely made as easy as humanly possible, tanked harder than a Kardashian marriage. I personally apologise for expecting the bare minimum from you as students. If you look at your grade book you will notice that you all have gotten a 50 point grade bump as 'extra credit' and no this was not because any of you deserved it but it was infact so I don't get my ass fired when the dean asks me 'hey why the fuck did 50% of your class fail an introductory biology class' to whom I will reply 'hmm I don't know maybe its because these klingons are 18 years old and still giggle every time I say the term 'phagocytosis'. I'd like to add that in fact one of you got a 5/100 on this exam for which I salute you. Considering this was 100% multiple choice and the statistical probability of you missing more than 90% GUESSING is actually higher than your chances of getting laid, which for this student would be an act of God (please stay out of the gene pool you know who you are). I could have actually taken a shit on the scantron, wiped it off on the grass, and I am pretty certain my feces could have picked up more correct answers than you deliberately bubbled in. So congratulations, on making me lose faith in the public school system, and in humanity.",
                   3 : "So today in Spanish class, my teacher told us that we would be listening to a song in Spanish. Already, I began to tremble. I had a bad feeling about this. “Which one?” I ask shakily, not wanting to hear the answer. “Despacito” She responds. I begin to hyperventilate. My worst fears have been realized. I fade in and out of conciseness. I clamp my palms over my ears, but I know it’s futile. The song plays. I’m crying now, praying. God, Allah, Buddha please help me. I curl up on the floor. There’s nothing I can do now. And then it happens. The chorus plays. The girls in my class open their mouths. The screams of the damned, the shrieks of the tortured fill my ears and bounce around my skull. My eardrums rupture, blood leaking out. I try to scream, but no sound comes out. I can only sit there, violently shaking as it happens to me. After what seems like hours, it’s finally over. I try to move, but I cannot make myself. My brain shuts down as my vision fades to black. I muster the last of my energy, uttering the accursed word.\n\n“Despacito”",
                   4 : "A spectwe is haunting Euwope – the spectwe of communyism. Aww the powews of owd Euwope have entewed into a howy awwiance to exowcise this spectwe: Pope and Tsaw, Mettewnyich and Guizot, Fwench Wadicaws and Gewman powice-spies. Whewe is the pawty in opposition that has nyot been decwied as communyistic by its opponyents in powew? Whewe is the opposition that has nyot huwwed back the bwanding wepwoach of communyism, against the mowe advanced opposition pawties, as weww as against its weactionyawy advewsawies? Two things wesuwt fwom this fact: I. Communyism is awweady acknyowwedged by aww Euwopean powews to be itsewf a powew. II. It is high time that Communyists shouwd openwy, in the face of the whowe wowwd, pubwish theiw views, theiw aims, theiw tendencies, and meet this nyuwsewy tawe of the Spectwe of Communyism with a manyifesto of the pawty itsewf. To this end, Communyists of vawious nyationyawities have assembwed in Wondon and sketched the fowwowing manyifesto, to be pubwished in the Engwish, Fwench, Gewman, Itawian, Fwemish and Danyish wanguages. I. Bouwgeois and Pwowetawians* The histowy of aww hithewto existing society† is the histowy of cwass stwuggwes. Fweeman and swave, patwician and pwebeian, wowd and sewf, guiwd-mastew‡ and jouwnyeyman, in a wowd, oppwessow and oppwessed, stood in constant opposition to onye anyothew, cawwied on an unyintewwupted, nyow hidden, nyow open fight, a fight that each time ended, eithew in a wevowutionyawy weconstitution of society at wawge, ow in the common wuin of the contending cwasses. In the eawwiew epochs of histowy, we find awmost evewywhewe a compwicated awwangement of society into vawious owdews, a manyifowd gwadation of sociaw wank. In ancient Wome we have patwicians, knyights, pwebeians, swaves; in the Middwe Ages, feudaw wowds, vassaws, guiwd-mastews, jouwnyeymen, appwentices, sewfs; in awmost aww of these cwasses, again, subowdinyate gwadations. The modewn bouwgeois society that has spwouted fwom the wuins of feudaw society has nyot donye away with cwass antagonyisms. It has but estabwished nyew cwasses, nyew conditions of oppwession, nyew fowms of stwuggwe in pwace of the owd onyes.",
                   5 : "ＨＥＹ ＤＯＵＢＬＥＬＩＦＴ， Ｉ’Ｍ ＴＲＹＩＮＧ ＴＯ ＬＥＡＲＮ ＴＯ ＰＬＡＹ ＳＨＡＣＯ． Ｉ ＪＵＳＴ ＨＡＶＥ Ａ ＱＵＥＳＴＩＯＮ ＡＢＯＵＴ ＴＨＥ ＳＫＩＬＬ ＢＵＩＬＤ： ＳＨＯＵＬＤ Ｉ ＭＡＸ ＢＡＣＫＳＴＡＢ ＬＩＫＥ ＹＯＵ ＢＡＣＫＳＴＡＢＢＥＤ ＣＬＧ， ＤＥＣＥＩＶＥ ＬＩＫＥ ＹＯＵ ＤＥＣＥＩＶＥＤ ＣＬＧ， ＯＲ ＨＡＬＬＵＣＩＮＡＴＥ ＬＩＫＥ ＹＯＵ ＭＡＤＥ ＣＬＧ ＨＡＬＬＵＣＩＮＡＴＥ ＡＢＯＵＴ ＨＡＶＩＮＧ Ａ ＣＨＡＮＣＥ ＡＴ ＷＩＮＮＩＮＧ ＡＮＯＴＨＥＲ ＴＯＵＲＮＡＭＥＮＴ",
                   6 : " ( ͡° ͜◯ ͡°) ﻿ＣＬＯＷＮ ＦＩＥＳＴＡ ( ͡° ͜◯ ͡°)",
                   7 : "So today, for the first time, my little toddler finally counted to ten. Everyone was celebrating, saying how proud they are in my kid, and then Ben Shapiro kicks open the door. 'Oh you think it's impressive that they can count to ten? I can count to one million.' and then proceeded, in my living room for the next two weeks, to count to one million. He then said 'yep, another libtard destroyed' and then curbstomped my kid.",
                   8 : "My teacher said to my I'm a failure, that I'll never amount to anything. I scoffed at him. Shocked, my teacher asked what's so funny, my future is on the line. 'Well...you see professor' I say as the teacher prepares to laugh at my answer, rebuttal at hand. 'I watch Rick and Morty.' The class is shocked, they merely watch pleb shows like the big bang theory to feign intelligence, not grasping the humor. '...how? I can't even understand its sheer nuance and subtlety.' 'Well you see...WUBBA LUBBA DUB DUB!' One line student laughs in the back, I turn to see a who this fellow genius is. It's none other than Albert Einstein."
                   }
        randSelect = randint(0,len(options)-1)
        await client.send_message(message.channel, options[randSelect])

@client.event
async def on_ready():
    """
    prints bot information to the console.
    """
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)