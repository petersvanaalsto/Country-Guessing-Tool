from tkinter import *
from tkinter import Toplevel
from countries import check_guess, get_remaining, reset_cntrylst, get_guessed, reset_guessed_score, get_country_capital
import pygame

# text in entry field and current correct countries
entry = ''
current_score = 0
current_guessed = []


def clear_text(e):
    """
    Deletes all text in entry field
    e: GUI entry field
    """
    e.delete(0, END)


def change_text(r, countries):
    """
    Gets list of countries to create a label for each item and place labels on window
    r: Window root
    countries: list of countries
    """
    labels = []
    count = 0

    for key in countries:
        labels.append(Label(r, text=key, font=('Helvetica', 12)))
        labels[count].grid(row=count, column=1)
        count += 1

    for i in range(count):
        labels[i].place(x=320, y=20 * i)


class GUI_Menu:
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.current_score = current_score
        self.max_score = 0
        self.score_count = 0
        self.giveup_button = None

        master.geometry('500x500')
        master.configure(background='maroon')
        master.title('Geography Games')

        self.label = Label(master, text='Pick a game-mode below')
        self.label.pack(pady=60)

        self.north_button = Button(master, text='Countries North America', command=self._north)
        self.north_button.pack()

        self.south_button = Button(master, text='Countries South America', command=self._south)
        self.south_button.pack()

        self.europe_button = Button(master, text='Countries of Europe', command=self._europe)
        self.europe_button.pack()

        self.asia_button = Button(master, text='Countries of Asia', command=self._asia)
        self.asia_button.pack()

        self.australia_button = Button(master, text='Countries of Australia and Oceania', command=self._australia)
        self.australia_button.pack()

        self.africa_button = Button(master, text='Countries of Africa', command=self._africa)
        self.africa_button.pack()

        self.all_button = Button(master, text='Countries of the world', command=self._all)
        self.all_button.pack()

        self.close_button = Button(master, text='Close all', command=quit)
        self.close_button.pack()

        pygame.mixer.init()
        master.mainloop()

    def make_top_window(self, r, mode):
        """
        Create new window with game of given game mode
        r: Top window root
        mode: game mode
        """
        self.entry = Entry(r, font='Helvetica', width=30)
        self.entry.configure(bg='black', bd=0)
        self.entry.place(x=20, y=20)

        pygame.mixer.music.load('music 2.mp3')
        pygame.mixer.music.play(loops=10)

        self.close_button = Button(r, text='Close all', command=r.quit)
        self.close_button.place(x=500, y=20)

        self.submit_button = Button(r, text='Enter', command=lambda: [(self.get_check_guess(r, self.entry.get(), mode),
                                                                       clear_text(self.entry), self.show_correct(r))])
        self.submit_button.place(x=20, y=50)

        self.giveup_button = Button(r, text='Give up', command=lambda: self.stop(r, mode))
        self.giveup_button.place(x=130, y=50)

        self.mute_button = Button(r, text='Mute', command=lambda: pygame.mixer.music.stop())
        self.mute_button.place(x=10, y=570)

    def make_studyguide(self, mode):
        """
        Create new window with listbox to display list of keys and items in dictionary for given country set
        mode: Game mode
        """
        self.top = Toplevel()
        self.top.title('Study Guide')
        self.top.geometry('600x600')
        self.top.configure(background='light pink')

        self.label = Label(self.top, text='All countries and their respective capitals are provided below: ')
        self.label.pack()

        d = get_country_capital(mode)

        self.listbox = Listbox(self.top, width=35, height=50, font=('Georgia', 12))
        self.listbox.place(x=160, y=30)

        for item in d.items():
            self.listbox.insert(0, list(item))

        self.listbox.insert(0, 'country, capital')

    def get_check_guess(self, _root_, s, m):
        """
        Takes user entry from entry field, checks if string matches valid country options, updates score
        _root_: Current window root
        s: entry from GUI entry field
        m: game mode
        """
        try:
            b, scr = check_guess(s, m)
        except TypeError:
            return
        print(b, scr)
        if b:
            self.update_score(_root_, scr)

    def update_score(self, r, points):
        """
        Update score with new point value and run update_scoreboard function
        r: Window root
        points: Correct country guesses
        """
        global current_score
        self.update_scoreboard(r, points)
        current_score = points
        self.current_score = current_score

    def update_scoreboard(self, r, points):
        """
        Update score count label with new point value and check if player won
        r: Window root
        points: Correct country guesses
        """
        self.score_count = Label(r, text=f'{points}/{self.max_score}', font='Arial')
        self.score_count.place(x=270, y=20)
        if points == self.max_score:
            self.win(r)

    def show_correct(self, r):
        """
        Creates listbox which displayed list with correctly guessed countries
        r: Window root
        """
        global current_guessed
        current_guessed = get_guessed()
        self.listbox = Listbox(r, width=35, height=50, font=('Georgia', 12))
        self.listbox.place(x=160, y=90)

        if len(current_guessed) == 1:
            self.listbox.insert(0, current_guessed[0])

        if len(current_guessed) >= 2:
            for item in current_guessed:
                print(item)
                self.listbox.insert(0, item)

    def win(self, top_root):
        """
        Add win label to current window
        top_root: Current window
        """
        self.win_message = Label(top_root, text='Congrats! You listed all of the countries', font='Arial')
        self.win_message.pack()

    def stop(self, r, g):
        """
        Gets countries not guessed and runs function to create label on current window
        r: Curren window
        g: Game mode
        """
        lst = get_remaining(g).keys()
        change_text(r, lst)

    def _north(self):
        global current_score, current_guessed
        current_guessed, current_score = reset_guessed_score()
        self.max_score = 23
        self.top = Toplevel()
        self.top.title('Countries of North America')
        self.top.geometry('600x600')
        self.top.configure(background='orange')

        self.make_top_window(self.top, 'North America')
        reset_cntrylst()

        self.score_count = Label(self.top, text=f'{current_score}/{self.max_score}', font='Arial')
        self.score_count.place(x=270, y=20)

        self.study_guide_button = Button(self.top, text='Study Capitals',
                                         command=lambda: self.make_studyguide('North America'))
        self.study_guide_button.place(x=465, y=565)

    def _south(self):
        global current_score, current_guessed
        current_guessed, current_score = reset_guessed_score()
        self.max_score = 12
        self.top = Toplevel()
        self.top.title('Countries of South America')
        self.top.geometry('600x600')
        self.top.configure(background='teal')

        self.make_top_window(self.top, 'South America')
        reset_cntrylst()

        score_count = Label(self.top, text=f'{current_score}/{self.max_score}', font='Arial')
        score_count.place(x=270, y=20)

        self.study_guide_button = Button(self.top, text='Study Capitals',
                                         command=lambda: self.make_studyguide('South America'))
        self.study_guide_button.place(x=465, y=565)

    def _europe(self):
        global current_score, current_guessed
        current_guessed, current_score = reset_guessed_score()
        self.max_score = 46
        self.top = Toplevel()
        self.top.title('Countries of Europe')
        self.top.geometry('600x600')
        self.top.configure(background='purple')

        self.make_top_window(self.top, 'Europe')
        reset_cntrylst()

        score_count = Label(self.top, text=f'{current_score}/{self.max_score}', font='Arial')
        score_count.place(x=270, y=20)

        self.study_guide_button = Button(self.top, text='Study Capitals',
                                         command=lambda: self.make_studyguide('Europe'))
        self.study_guide_button.place(x=465, y=565)

    def _asia(self):
        global current_score, current_guessed
        current_guessed, current_score = reset_guessed_score()
        self.max_score = 49
        self.top = Toplevel()
        self.top.title('Countries of Asia')
        self.top.geometry('600x600')
        self.top.configure(background='yellow')

        self.make_top_window(self.top, 'Asia')
        reset_cntrylst()

        score_count = Label(self.top, text=f'{current_score}/{self.max_score}', font='Arial')
        score_count.place(x=270, y=20)

        self.study_guide_button = Button(self.top, text='Study Capitals',
                                         command=lambda: self.make_studyguide('Asia'))
        self.study_guide_button.place(x=465, y=565)

    def _africa(self):
        global current_score, current_guessed
        current_guessed, current_score = reset_guessed_score()
        self.max_score = 54
        self.top = Toplevel()
        self.top.title('Countries of Africa')
        self.top.geometry('600x600')
        self.top.configure(background='aqua')

        self.make_top_window(self.top, 'Africa')
        reset_cntrylst()

        score_count = Label(self.top, text=f'{current_score}/{self.max_score}', font='Arial')
        score_count.place(x=270, y=20)

        self.study_guide_button = Button(self.top, text='Study Capitals',
                                         command=lambda: self.make_studyguide('Africa'))
        self.study_guide_button.place(x=465, y=565)

    def _australia(self):
        global current_score, current_guessed
        current_guessed, current_score = reset_guessed_score()
        self.max_score = 14
        self.top = Toplevel()
        self.top.title('Countries of Australia and Oceania')
        self.top.geometry('600x600')
        self.top.configure(background='forest green')

        self.make_top_window(self.top, 'Australia')
        reset_cntrylst()

        score_count = Label(self.top, text=f'{current_score}/{self.max_score}', font='Arial')
        score_count.place(x=270, y=20)

        self.study_guide_button = Button(self.top, text='Study Capitals',
                                         command=lambda: self.make_studyguide('Australia'))
        self.study_guide_button.place(x=465, y=565)

    def _all(self):
        global current_score, current_guessed
        current_guessed, current_score = reset_guessed_score()
        self.max_score = 196
        self.top = Toplevel()
        self.top.title('Countries of the World')
        self.top.geometry('600x600')
        self.top.configure(background='sky blue')

        self.make_top_window(self.top, 'All')
        reset_cntrylst()

        score_count = Label(self.top, text=f'{current_score}/{self.max_score}', font='Arial')
        score_count.place(x=270, y=20)

        self.study_guide_button = Button(self.top, text='Study Capitals',
                                         command=lambda: self.make_studyguide('All'))
        self.study_guide_button.place(x=465, y=565)
