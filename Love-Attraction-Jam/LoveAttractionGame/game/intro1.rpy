
label intro1:

    scene bg clothespizza

    show hum neutral at left

    # Human sits calmly alone.

    # They look left. They look right.
    
    # They suddenly talk aloud
    
    hum "Well here I am at Clothe's Pizza but...where are you...?"

    # They close their eyes.

    # Capybara silently shows up.

    show capy neutral at right

    hum "Feels like it was yesterday...Has it been so long that you've four taken...?"

    # Their eyes open, they look confused.
    hum "...four...taken?"
    # Their expressive fires up.
    hum "Forgotten!"
    # They look sad again.
    hum "Have you forgotten?"

    capy "You know...Mumbling to yourself is so last week."

    # Human turns around

    hum "Ahhh!!"

    # Capybara smiles

    capy "May I take your order?"

    hum "You...work here?!? I thought we passed a law against that recently...?"

    capy "Actually that law was passed ten years ago!"

    hum "So recent!"

    # Capybara frowns.

    capy "Pshh. I wish I worked here. Even though I've got plenty of relevant experience, they said my credit score inferred a trait of unreliability..."

    hum "Wait, what kind of a waitstaff position requires a credit score check...? Wait, what kind of a place doesn't deny you outright for being a kid???!"

    capy "I can't help it if I like to gamble on the weekends. It's their fault for letting me in!"

    hum "It really is!! Is everyone in this town so eerily soluble?!??" 

    capy "Hippo said they're gonna break my parent's legs at around...now-ish...if I don't pay up." 

    # Capybara smiles brightly.

    capy "I said, 'You just try! I'll be with my parent all day!'"

    # Capybara smiles at Human, who has an unnerved look on their face and then quickly looks back and forth.

    hum "Oh-...oh god no!!"

    capy "Just kidding!" 

    # They return to a neutral expression

    capy "Hahahahaha...mostly."

    capy "Anyway...what were you mumbling about?"

    hum "None of your business, subadult!"

    capy "WHAT?! But you gotta tell me!"

    hum "No! You are far too thigh-knee and you reek like floor candy!!"

    # Capybara turns sad.

    capy "Hmph. That's just because I mixed my parents' perfume and cologne together!"

    # They smile brightly

    capy "Don't I smell wonderful?"

    hum "You smell like a lemon lollipop left under a minor's hardhat!"
    
    capy "So rude!!"

    hum "I don't talk to strangers."

    capy "But I'm a kid!!"

    hum "Sorry but you've got to be tall to talk to me, juice aisle!"

    capy "...juice aisle?"

    hum "Urgh, I mean...uhhh..."
    
    capy "Do you have problems with your words? Mix'em up a lot?"
    
    hum "Err, well, sometimes."

    capy "Well, how's this? I'll teach you a little something to help keep your words straight that you can use for the rest of your life! And you tell me why you're mumbling so much!"

    hum "Hm. Depends. What's your suggestion?"

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