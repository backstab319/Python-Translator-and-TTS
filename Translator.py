from googletrans import Translator
from os import name, system
from time import sleep

class Curse:
    translator = Translator()
    in_lan,out_lan = "en","kn"
    def clrscr(self): system("cls") if name == "nt" else system("clear")
    def pause(self): input("Press any key to continue...")

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
            if len(x) == 2 and io == 0: self.lan_allocator(x,0)
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

    def main_screen(self):
        self.clrscr()
        x = input("Welcome to the translator application\nCurrent Input "+self.in_lan+" Output "+self.out_lan+"\n1.Translate\n2.Change the input language\n3.Change output language\n4.Exit\n")
        if x == "1": self.translate_method()
        elif x == "2": self.change_IO(0)
        elif x == "3": self.change_IO(1)
        elif x == "4":
            self.halt()
            return
        else:
            print("Invalid input!")
            self.pause()
        self.main_screen()

    def translate_method(self):
        self.clrscr()
        x = input("Enter 000 to go back\nPlease enter a string to translate\n")
        if x == "000":
            return
        output = self.translator.translate(x,dest=self.out_lan,src=self.in_lan)
        print(output.text)
        self.pause()
        self.translate_method()

curse = Curse()
curse.main_screen()