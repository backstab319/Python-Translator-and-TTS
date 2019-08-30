from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from os import name, system
from time import sleep
import language_check as lan

class Curse:
    translator = Translator()
    in_lan,out_lan,tts_status,tts_speed,feeder,feeder_status,grammar_in,grammar_out = "en","kn","on",False,[],"off","off","off"
    lang_av = [i for i in lan.get_languages()]
    def clrscr(self): system("cls") if name == "nt" else system("clear")
    def pause(self): input("Press any key to continue...")
    def change_tts(self,setter):
        if setter == 0: self.tts_status="off" if self.tts_status == "on" else "on"
        else: self.tts_speed = True if self.tts_speed == False else False

    def play_text(self,text):
        output_audio = gTTS(text=text,lang=self.out_lan,slow=self.tts_speed)
        output_audio.save("audio.mp3")
        playsound("audio.mp3")
        system("del audio.mp3 /f") if name == "nt" else system("rm -f audio.mp3")

    def lan_allocator(self,lan,io):
        if io == 0: self.in_lan = lan
        else: self.out_lan = lan

    def lan_selector(self,io,method):
        self.clrscr()
        status = 0
        if method == 0:
            x = input("1.English\n2.Hindi\n3.Kannada\n4.Telugu\n5.Malayalam\n6.Tamil\n7.Go back\n")
            if x == "1": self.lan_allocator("en",0) if io == 0 else self.lan_allocator("en",1)
            elif x == "2": self.lan_allocator("h1",0) if io == 0 else self.lan_allocator("hi",1)
            elif x == "3": self.lan_allocator("kn",0) if io == 0 else self.lan_allocator("kn",1)
            elif x == "4": self.lan_allocator("te",0) if io == 0 else self.lan_allocator("te",1)
            elif x == "5": self.lan_allocator("ml",0) if io == 0 else self.lan_allocator("ml",1)
            elif x == "6": self.lan_allocator("ta",0) if io == 0 else self.lan_allocator("ta",1)
            elif x == "7": return
            else:
                print("Invalid input!")
                self.pause()
                status = 1
        else:
            x = input("Warning! Please enter the language code carefully! Make sure the code is only two characters long.\n1.To go back\nEnter the code\n")
            if x == "1": return
            elif len(x) == 2 and io == 0: self.lan_allocator(x,0)
            elif len(x) == 2 and io == 1: self.lan_allocator(x,1)
            else:
                print("Invalid input")
                self.pause()
                status = 1
        if status == 0: return
        self.lan_selector(io,method)

    def change_IO(self,io):
        self.clrscr()
        x = input("1.Select from existing languages\n2.Enter language code manually\n3.Go back\n")
        if x == "1": self.lan_selector(io,0)
        elif x == "2": self.lan_selector(io,1)
        elif x == "3": return
        else:
            print("Invalid input!")
            self.pause()
        self.change_IO(io)

    def halt(self):
        self.clrscr()
        print("Thank you for using the translator application.")
        sleep(3)
        self.clrscr()

    def feeder_screen(self):
        self.clrscr()
        x,rek = input("Select the relevent seetings\n1.Toggle feeder\n2.Load Feeder with data\n3.Show content of feeder\n0.Go back\n"),0
        if x == "1": self.feeder_status,rek = ("on",1) if self.feeder_status == "off" else ("off",1)
        elif x == "2":
            self.feeder.clear()
            while True:
                x = input()
                if x: self.feeder.append(x)
                else: break
        elif x == "3": [print(i) if self.feeder != [] else 0 for i in self.feeder]
        elif x == "0": rek = 1
        else:
            print("Invalid Input!")
        if rek == 0:
            self.pause()
            self.feeder_screen()
        else: pass

    def grammar_toggle(self,toggle):
        if toggle in [1,3]: self.grammar_in = "on" if self.grammar_in == "off" else "off"
        if toggle in [2,3]: self.grammar_out = "on" if self.grammar_out == "off" else "off"

    def grammar_settings(self):
        self.clrscr()
        x = input("Attention! Only the supported languages grammar shall be checked!\n1.Toggle Input Grammar Check\n2.Toggle Output Grammar Check\n3.Toggle Both\n0.Go back\n")
        if x == "1": self.grammar_toggle(1)
        elif x == "2": self.grammar_toggle(2)
        elif x == "3": self.grammar_toggle(3)
        elif x == "0": return
        else:
            print("Invalid Input!")
            self.pause()
            self.grammar_settings()

    def main_screen(self):
        self.clrscr()
        x = input("Welcome to the translator application\nCurrent Input: "+self.in_lan+" Output: "+self.out_lan+" TTS: "+self.tts_status+" TTS Speed Slow: "+str(self.tts_speed)+" Feeder: "+self.feeder_status+" Chk input "+self.grammar_in+" Chk output "+self.grammar_out+"\n1.Translate\n2.Change the input language\n3.Change output language\n4.Toggle TTS\n5.Toggle TTS speed\n6.Feeder Settings\n7.Grammar Settings\n0.Exit\n")
        if x == "1": self.translate_method()
        elif x == "2": self.change_IO(0)
        elif x == "3": self.change_IO(1)
        elif x == "4": self.change_tts(0)
        elif x == "5": self.change_tts(1)
        elif x == "6": self.feeder_screen()
        elif x == "7": self.grammar_settings()
        elif x == "0":
            self.halt()
            return
        else:
            print("Invalid input!")
            self.pause()
        self.main_screen()

    def grammar_correction_in(self,data,datatype):
        if datatype == "in":
            lang = self.in_lan
            tool = lan.LanguageTool(language=lang)
            matches = tool.check(data)
            return lan.correct(data, matches)

    def grammar_correction_out(self,data,datatype):
        if datatype == "out":
            lang = self.out_lan
            tool = lan.LanguageTool(language=lang)
            matches = tool.check(data)
            return lan.correct(data, matches)

    def feeder_iterator(self,feeder):
        self.feeder = feeder
        for i in self.feeder:
            if (i != self.grammar_correction_in(i,"in")) and (len(feeder) == 1) and (self.grammar_in == "on") and self.in_lan in self.lang_av: print("Correction",self.grammar_correction_in(i,"in"))
            if (i != self.grammar_correction_in(i,"in")) and (len(feeder) != 1) and (self.grammar_in == "on") and self.in_lan in self.lang_av: print("Correction",self.grammar_correction_in(i,"in"))
            output = self.translator.translate(i,dest=self.out_lan,src=self.in_lan)
            if output.text != self.grammar_correction_out(output.text,"out") and len(feeder) == 1 and self.grammar_out == "on" and self.out_lan in self.lang_av: print("Correction",self.grammar_correction_out(output.text,"out"))
            if output.text != self.grammar_correction_out(output.text,"out") and len(feeder) != 1 and self.grammar_out == "on" and self.out_lan in self.lang_av: print("Correction",self.grammar_correction_out(output.text,"out"))
            print(output.text) if len(feeder) == 1 else print(i+"\n"+output.text)
            self.play_text(output.text) if self.tts_status == "on" else 0
        self.feeder.clear()

    def translate_method(self):
        self.clrscr()
        rek = 0
        if self.feeder_status == "on" and self.feeder: self.feeder_iterator(self.feeder)
        else:
            x = input("Enter 000 to go back\nPlease enter a string to translate\n").split("\n")
            if "000" in x: rek = 1
            elif x[0] != "": self.feeder_iterator(x)
            else: print("Cannot be an empty string")
        if rek == 1: pass
        else:
            self.pause()
            self.translate_method()

curse = Curse()
curse.main_screen()