#On indique ou est l'interpreteur
import aiy.audio #On importe la fonction qui lit des sons
import aiy.voicehat

button = aiy.voicehat.get_button()
button.wait_for_press() #On attend jusqu'à ce que le bouton soit appuyé
aiy.audio.say("Naval battle with vocal command, a table's ronde project")
button.wait_for_press()
aiy.audio.say("MVP VERSION 0, NAVAL BATTLE AGAINST A RANDOMLY GENERATED GRID OF BOATS TEXTUALLY WITH TERMINAL DISPLAY")
button.wait_for_press()
aiy.audio.say("MVP VERSION 1, NAVAL BATTLE AGAINST A RANDOMLY GENERATED GRID OF BOATS WITH GRAPHICAL DISPLAY")
button.wait_for_press()
aiy.audio.say("MVP VERSION 2, NAVAL BATTLE AGAINST A RANDOMLY GENERATED GRID OF BOATS WITH GRAPHICAL DISPLAY AND VOCAL COMMAND")
button.wait_for_press()
aiy.audio.say("MVP VERSION 3, NAVAL BATTLE AGAINST A MACHINE WITH GRAPHICAL DISPLAY AND VOCAL COMMAND")
button.wait_for_press()
aiy.audio.say("thank you for your attention")
