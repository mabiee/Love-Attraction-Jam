label intro1:

   scene bg clothespizza

   show human neutral at left

   # Human sits calmly alone.

   hum "..."

   # They look left. They look right.
   show human:
     linear 0.5 xzoom -1.0 yzoom 1.0
     pause 0.5
     linear 0.5 xzoom 1.0 yzoom 1.0
     pause 0.5
     linear 0.5 xzoom -1.0 yzoom 1.0

   # They suddenly talk aloud
   
   hum "Well here I am at Clothe's Pizza but...where are you...?"

   # They close their eyes.
   show human eyesclosed
   pause

   # Capybara silently shows up.

   show capy neutral at right:
     alpha 0.5

   hum "Feels like it was yesterday...Has it been so long that you've four taken...?"

   show human confused
   hum "...four...taken?"
   show human firedup
   hum "Forgotten!"
   show human sad
   hum "Have you forgotten?"

   show capy:
      alpha 1.0
   capy "You know...Mumbling to yourself is so last week."

   # Human turns around
   show human surprised:
     linear 0.5 xzoom 1.0 yzoom 1.0

   hum "Ahhh!!"

   # Capybara smiles
   show capy happy:
     alpha 1.0
   show human:
      alpha 0.5

   capy "May I take your order?"

   show human:
     alpha 1.0
   show capy:
      alpha 0.5
   hum "You...work here?!? I thought we passed a law against that recently...?"

   show capy:
      alpha 1.0
   show human:
      alpha 0.5
   capy "Actually that law was passed ten years ago!"

   show human:
     alpha 1.0
   show capy:
      alpha 0.5
   hum "So recent!"

   # Capybara frowns.
   show capy sad:
      alpha 1.0
   show human:
      alpha 0.5
   capy "Pshh. I wish I worked here. Even though I've got plenty of relevant experience, they said my credit score inferred a trait of unreliability..."

   show human:
     alpha 1.0
   show capy:
      alpha 0.5
   hum "Wait, what kind of a waitstaff position requires a credit score check...? Wait, what kind of a place doesn't deny you outright for being a kid???!"

   show capy neutral:
      alpha 1.0
   show human:
      alpha 0.5
   capy "I can't help it if I like to gamble on the weekends. It's their fault for letting me in!"

   show human:
     alpha 1.0
   show capy:
      alpha 0.5
   hum "It really is!! Is everyone in this town so eerily soluble?!??" 

   show capy:
      alpha 1.0
   show human:
      alpha 0.5
   capy "Hippo said they're gonna break my parent's legs at around...now-ish...if I don't pay up." 

   # Capybara smiles brightly.
   show capy laugh
   capy "I said, 'You just try! I'll be with my parent all day!'"

   # Capybara smiles at Human, who has an unnerved look on their face and then quickly looks back and forth.

   show human scared:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "Oh-...oh god no!!"

   show capy:
      alpha 1.0
   show human:
      alpha 0.5
   capy "Just kidding!" 

   # They return to a neutral expression
   show capy happy
   capy "Hahahahaha...mostly."
   capy "Anyway...what were you mumbling about?"

   show human neutral:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "None of your business, subadult!"

   show capy:
      alpha 1.0
   show human:
      alpha 0.5
   capy "WHAT?! But you gotta tell me!"

   show human:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "No! You are far too thigh-knee and you reek like floor candy!!"

   # Capybara turns sad.
   show capy sad:
      alpha 1.0
   show human:
      alpha 0.5
   capy "Hmph. That's just because I mixed my parents' perfume and cologne together!"
   # They smile brightly
   show capy laugh
   capy "Don't I smell wonderful?"

   show human:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "You smell like a lemon lollipop left under a minor's hardhat!"

   show capy angry:
      alpha 1.0
   show human:
      alpha 0.5
   capy "So rude!!"

   show human:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "I don't talk to strangers."

   show capy:
      alpha 1.0
   show human:
      alpha 0.5
   capy "But I'm a kid!!"

   show human:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "Sorry but you've got to be tall to talk to me, juice aisle!"

   show capy confused:
      alpha 1.0
   show human:
      alpha 0.5
   capy "...juice aisle?"

   show human confused:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "Urgh, I mean...uhhh..."

   show capy neutral:
      alpha 1.0
   show human:
      alpha 0.5
   capy "Do you have problems with your words? Mix'em up a lot?"

   show human:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "Err, well, sometimes."

   show capy:
      alpha 1.0
   show human:
      alpha 0.5
   capy "Well, how's this? I'll teach you a little something to help keep your words straight that you can use for the rest of your life! And you tell me why you're mumbling so much!"

   show human:
      alpha 1.0
   show capy:
      alpha 0.5
   hum "Hm. Depends. What's your suggestion?"

   show capy:
      alpha 1.0
   show human:
      alpha 0.5
   capy "Duh, didn't you ever learn about the Catachresis system in school? Like...first grade?"

   menu:
    "Do you want to play through the tutorial?"
    "Yes":
      # The player can now choose either to go through the tutorial or not
      # If they choose yes:
      capy "Well, now it's time for you to get educated!"
      # If they choose no:
    "No":
      hum "Ugh, useless, I already know that technique! I took it twice in remedial classes!"
      capy "Then use it."
      hum "Fine. Ugh, this little kid is looking down on me. Looks like I have no choice, I'm going to just have to use...the Catachresis System!!"
   
   # initialise CATACHRESIS MODE

   capy "As you already know, everyone in this world has exactly three personality traits."
   capy "When using the Catachresis system, you decide upon which of your personality traits you want to shine through!"
   capy "For example, if you ask me what I want for lunch, I could be BLASE (the Cap) and tell you 'floor candy' or DAREDEVILISH and tell you 'human meat'."
   capy "And th way you decide this is by (playig the minigame)"

   # prompt: "So will you tell me what you were mumbling about?"
   # curious: YES "Sure, I'll tell you"
   # cautious: NO "It doesn't concern you... but I'll tell you anyway"
   # casual: MAYBE "Eh, whatever, might as well tell you."

   return