###########################################################################
#    Maths Tutor
#
#    Copyright (C) 2022-2023 Roopasree A P <roopasreeap@gmail.com>
#    Copyright (C) 2022-2023 Roopasree A P <roopasreeap@gmail.com>
#    
#    
#    This project is Supervised by Zendalona(2022-2023)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################


import gi
import time
import speechd
gi.require_version("Gtk", "3.0")
gi.require_version('Gst', '1.0')
from gi.repository import Gtk, Gdk, GObject, GLib,Pango
# Import GST
from gi.repository import Gst
import re

import threading

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Label and Text Field Example")
        self.set_border_width(10)
        #Create a vertical box layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # Add the VBox container to the main window
        self.add(vbox)
        
        welcome_message = "Welcome to maths tutor!\nPress enter to start "
        
        # create  a Gtk label
        self.label = Gtk.Label()
        # Set the text of the label to the value of welcome_message
        self.label.set_text(welcome_message)
        # Modify the font of the label
        self.modify_font(Pango.FontDescription("Sans 40"))
        
        
        # Define the font color
        font_color = "#0603f0"
        # Define the background color
        background_color = "#ffffff"
        # Set the font color
        self.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse(font_color))
        # Set the background color
        self.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse(background_color))
        # Add the label to the vbox container
        vbox.pack_start(self.label, True, True, 0)
        
        
        #Create a horizontal box layout 
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

        #fix1 = Gtk.Fixed()
        #hbox.pack_start(fix1, True, True, 0)
        # Add the hbox to the vbox container
        vbox.pack_start(hbox, False, False, 0)

       
        #Create a Gtk.Entry widget and assign it to self.entry
        self.entry = Gtk.Entry()
        # Connect the "activate" signal of the entry widget to the self.on_entry_activated method
        self.entry.connect("activate", self.on_entry_activated)
        #Add entry to horizontal box
        hbox.pack_start(self.entry, False, False, 0)

        #fix2 = Gtk.Fixed()
        #hbox.pack_start(fix2, True, True, 0)
        
        #hbox.set_hexpand(False)

        
        #Create multiple instances of GtkImage and add them to the vertical box
        self.image = Gtk.Image.new_from_file("/home/roopasree/Desktop/Game/Image/positive4.png")
        vbox.pack_start(self.image, True, True, 0)
        
        
        #Create a button
        about_button=Gtk.Button(label="About")
        about_button.connect("clicked",self.on_about_clicked)
        about_button.set_size_request(1,1)
        hbox.pack_start(about_button, True, True, 0)
        
        

        

        self.current_question_index = -1
        self.wrong=False
        # Create a playbin element with the name 'player' and assign it to self.player
        self.player = Gst.ElementFactory.make('playbin', 'player')
        
        # Playing starting sound
        self.play_file('start.ogg')
        
        
        # Initialize speechd client
        self.spd_cli = speechd.Client("MathTeacher")
        self.spd_cli.set_output_module("rhvoice")
        self.spd_cli.speak(welcome_message)
        
        self.connect('delete-event', self.on_destroy)
        self.connect('destroy', self.on_destroy)
        

    
    def play_file(self, filename):
        file_path_and_name = 'file:///home/roopasree/Desktop/Game/sounds/'+filename
        self.player.set_state(Gst.State.READY)
        self.player.set_property('uri',file_path_and_name)
        self.player.set_state(Gst.State.PLAYING)
        
    def on_read_files(self):
        filename = "/home/roopasree/project/calculation.txt"
        self.list = []

        with open(filename, "r") as file:
            for line in file:
                stripped_line = line.strip()
                self.list.append(stripped_line)

    def convert_signs(self, text):
        return text.replace("+"," plus ").replace("-"," minus ").replace("x"," multiply ").replace("/"," devided by ")

    def on_entry_activated(self,entry):
        

        
        if self.current_question_index == -1:
            self.next_question()
            
        else:
            answer = self.entry.get_text()
            correct_answer = self.answer
            
            if answer.lower() == correct_answer.lower():                
                time_end = time.time()
                
                time_taken = time_end - self.time_start
                
                time_alotted = int(self.list[self.current_question_index].split("===")[2])
                
                print(time_taken)
                if  time_taken < time_alotted:
                    self.spd_cli.speak("Excellent!")
                    self.label.set_text("Excellent!")
                    self.image.set_from_file("/home/roopasree/Desktop/Game/Image/positive2.png")
                    self.play_file('excellent.ogg')
                elif time_taken < time_alotted+2:
                    self.spd_cli.speak("Very good!")
                    self.label.set_text("Very good!")
                    self.image.set_from_file("/home/roopasree/Desktop/Game/Image/positive5.png")
                    self.play_file('very_good.ogg')
                elif time_taken < time_alotted+4:
                    self.spd_cli.speak("Good!")
                    self.label.set_text("Good!")
                    self.image.set_from_file("/home/roopasree/Desktop/Game/Image/positive9.png")
                    self.play_file('next_level_6.ogg')
                elif time_taken < time_alotted+6:
                    self.spd_cli.speak("Not bad!")
                    self.label.set_text("Not bad!")
                    self.image.set_from_file("/home/roopasree/Desktop/Game/Image/positive1.png")
                    self.play_file('ok.ogg')
                else :
                    self.spd_cli.speak("Okay!")
                    self.label.set_text("Okay!")
                    self.image.set_from_file("/home/roopasree/Desktop/Game/Image/neg3.png")
                    self.play_file('try_more_fast.ogg')

                GLib.timeout_add_seconds(3,self.next_question)
                
               

            else:
                
                self.label.set_text("sorry,lets try again")
                self.spd_cli.speak("Sorry!Let's try again")
                #self.image.set_from_file("/home/roopasree/Desktop/Game/Image/neg5.png")
                
                #time.sleep(3)
                self.wrong=True
                GLib.timeout_add_seconds(3,self.next_question)
                self.entry.set_text("")
            
            
    def next_question(self):
        self.time_start = time.time()
        
        if self.wrong==True:
            self.label.set_text(self.question)
            self.announce_question(self.question, self.make_sound)
            self.image.set_from_file("/home/roopasree/Desktop/Game/Image/neg5.png")
            self.wrong=False
        else:
            self.current_question_index = self.current_question_index + 1
            if self.current_question_index < len(self.list)-1:
                print(len(self.list))
                self.question = self.list[self.current_question_index].split("===")[0]
                self.answer = self.list[self.current_question_index].split("===")[1]
                self.make_sound = self.list[self.current_question_index].split("===")[3]
                self.label.set_text(self.question)
                #self.announce_question(self.question, self.make_sound)
                
                threading.Thread(target=self.announce_question,args=[self.question, self.make_sound]).start()
                
                self.entry.set_text("")
                self.image.set_from_file("/home/roopasree/Desktop/Game/Image/neg1.png")
            else:
                self.spd_cli.speak("Successfully finished!")
                self.label.set_text("Successfully finished!")
                self.image.set_from_file("/home/roopasree/Desktop/Game/Image/positive7.png")
                
                
    def announce_question(self, question, make_sound):
        print(question, make_sound)
        if(make_sound == '1'):
            item_list = re.split(r'(\d+)', question)[1:-1]
            for item in item_list:
                if item.isnumeric():
                    num = int(item)
                    while(num > 0):
                        num = num-1;
                        self.play_file('coin.ogg')
                        time.sleep(0.7)
                else:
                    self.spd_cli.speak(self.convert_signs(item))
                    time.sleep(0.7)
        else:
            self.spd_cli.speak(self.convert_signs(self.question))

    def on_destroy(self, widget=None, *data):
        print("CLOS")
        self.spd_cli.close()
        

    def show_about_dialog(self):
        about_dialog = Gtk.AboutDialog()

        # Set the relevant properties of the about dialog
        about_dialog.set_program_name("MATHS TUTOR GAME\n 0.1 \n\nMATHS TUTOR is a game to develop students calculation ability in maths and to judge themselves.\n Which is helpful to the students who have basic knowledge in maths. \n They  want to answer the questions they got and can lead into progress if they can answer the questions correctly.  \n\n   Copyright(C) 2022-2023 ROOPASREE A P <roopasreeap@gmail.com>\n\n   Supervised by  Zendalona(2022-2023)\n\n This program is free software you can redistribute it and or modify \nit under the terms of GNU General Public License as published by the free software foundation \n either gpl3 of the license.This program is distributed in the hope that it will be useful,\n but without any warranty without even the implied warranty of merchantability or fitness for a particular purpose.\n see the GNU General Public License for more details") 
        
        #self.set_version("")
        
        about_dialog.set_website_label("GNU General Public License,version 0.1\n\n" "Visit MATHS TUTOR Home page")
        
        about_dialog.set_website("http://wwww,zendalona.com//MATHS TUTOR")
        about_dialog.set_authors(["Roopasree A P"])
        about_dialog.set_documenters(["Roopasree A P"])
        about_dialog.set_artists(["Nalin Sathyan" ,"Dr.Saritha Namboodiri", "Subha I N", "Bhavya P V", "K.Sathyaseelan"])
        
        about_dialog.run()
        about_dialog.destroy()

    def on_about_clicked(self,button):
         self.show_about_dialog()


def main():
    Gst.init(None)
    win = MyWindow()
    win.set_default_size(500,700)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    win.on_read_files()
    Gtk.main()


if __name__ == "__main__":
    main()
