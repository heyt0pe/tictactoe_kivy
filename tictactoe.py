from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import random, threading, copy

Builder.load_file('tictactoe.kv')

gameBoard = [
             ['00', '01', '02'],
             ['10', '11', '12'],
             ['20', '21', '22'],
            ]

playedd = -1
coords = []
notWon = True
canPlay = True
tp = ''
op = ''
mgr = ''

class Block(Label):
    def on_touch_down(self, touch):
        global notWon
        if canPlay:
            if notWon:
                if self.collide_point(*touch.pos):
                    global playedd
                    if self.text != '':
                        pass
                    else:
                        playedd += 1
                        if playedd % 2 == 0 or playedd == 0:
                            self.text = 'O'
                        elif playedd % 2 != 0:
                            self.text = 'X'
                        global tp, op, gg
                        if mgr.current == 'twoplayers':
                            tp.play()
                        elif mgr.current == 'oneplayer':
                            op.play()


class Home(Screen):
    pass

class TwoPlayers(Screen):
    def __init__(self, **kwargs):
        super(TwoPlayers, self).__init__(**kwargs)
        global tp
        tp = self

    def clear(self, *args):
        for i in range(1, 10, 1):
            name = 'cell' + str(i)
            a = self.ids[name]
            a.text = ''
            a.color = 1, 1, 1, 1
        get = self.ids['player_text']
        get.text = ''
        global playedd, notWon, gameBoard
        playedd = -1
        notWon = True
        gameBoard = [
                     ['00', '01', '02'],
                     ['10', '11', '12'],
                     ['20', '21', '22'],
                    ]

    def play(self, *args):
        cell1 = self.ids['cell1']
        text1 = cell1.text.capitalize()
        if text1 == 'X':
            cell1.color = 1, 0, 0, 1
            cell1.text = text1
        elif text1 == 'O':
            cell1.color = 0, 1, 0, 1
            cell1.text = text1
        elif text1 == '1':
            pass
        else:
            cell1.text = ''

        cell2 = self.ids['cell2']
        text2 = cell2.text.capitalize()
        if text2 == 'X':
            cell2.color = 1, 0, 0, 1
            cell2.text = text2
        elif text2 == 'O':
            cell2.color = 0, 1, 0, 1
            cell2.text = text2
        elif text2 == '2':
            pass
        else:
            cell2.text = ''

        cell3 = self.ids['cell3']
        text3 = cell3.text.capitalize()
        if text3 == 'X':
            cell3.color = 1, 0, 0, 1
            cell3.text = text3
        elif text3 == 'O':
            cell3.color = 0, 1, 0, 1
            cell3.text = text3
        elif text3 == '3':
            pass
        else:
            cell3.text = ''

        cell4 = self.ids['cell4']
        text4 = cell4.text.capitalize()
        if text4 == 'X':
            cell4.color = 1, 0, 0, 1
            cell4.text = text4
        elif text4 == 'O':
            cell4.color = 0, 1, 0, 1
            cell4.text = text4
        elif text4 == '4':
            pass
        else:
            cell4.text = ''

        cell5 = self.ids['cell5']
        text5 = cell5.text.capitalize()
        if text5 == 'X':
            cell5.color = 1, 0, 0, 1
            cell5.text = text5
        elif text5 == 'O':
            cell5.color = 0, 1, 0, 1
            cell5.text = text5
        elif text5 == '5':
            pass
        else:
            cell5.text = ''

        cell6 = self.ids['cell6']
        text6 = cell6.text.capitalize()
        if text6 == 'X':
            cell6.color = 1, 0, 0, 1
            cell6.text = text6
        elif text6 == 'O':
            cell6.color = 0, 1, 0, 1
            cell6.text = text6
        elif text6 == '6':
            pass
        else:
            cell6.text = ''

        cell7 = self.ids['cell7']
        text7 = cell7.text.capitalize()
        if text7 == 'X':
            cell7.color = 1, 0, 0, 1
            cell7.text = text7
        elif text7 == 'O':
            cell7.color = 0, 1, 0, 1
            cell7.text = text7
        elif text7 == '7':
            pass
        else:
            cell7.text = ''

        cell8 = self.ids['cell8']
        text8 = cell8.text.capitalize()
        if text8 == 'X':
            cell8.color = 1, 0, 0, 1
            cell8.text = text8
        elif text8 == 'O':
            cell8.color = 0, 1, 0, 1
            cell8.text = text8
        elif text8 == '8':
            pass
        else:
            cell8.text = ''

        cell9 = self.ids['cell9']
        text9 = cell9.text.capitalize()
        if text9 == 'X':
            cell9.color = 1, 0, 0, 1
            cell9.text = text9
        elif text9 == 'O':
            cell9.color = 0, 1, 0, 1
            cell9.text = text9
        elif text9 == '9':
            pass
        else:
            cell9.text = ''

        getter3 = self.ids['player_text']
        global notWon

        if text1 == text2 and text2 == text3 and text1 != '':
            getter3.text = text1 + ' Wins'
            notWon = False

        elif text4 == text5 and text5  == text6 and text6 != '':
            getter3.text = text4 + ' Wins'
            notWon = False

        elif text7 == text8 and text8 == text9 and text9 != '':
            getter3.text = text7 + ' Wins'
            notWon = False

        elif text1 == text4 and text4 == text7 and text7 != '':
            getter3.text = text1 + ' Wins'
            notWon = False

        elif text2 == text5 and text5 == text8 and text8 != '':
            getter3.text = text2 + ' Wins'
            notWon = False

        elif text3 == text6 and text6 == text9 and text9 != '':
            getter3.text = text3 + ' Wins'
            notWon = False

        elif text1 == text5 and text5 == text9 and text1 != '':
            getter3.text = text1 + ' Wins'
            notWon = False

        elif text3 == text5 and text5 == text7 and text7 != '':
            getter3.text = text3 + ' Wins'
            notWon = False

        global gameBoard
        for i in range(1, 10, 1):
            name = 'cell' + str(i)
            a = self.ids[name]
            if a.text == 'X' or a.text == 'O':
                if i == 1:
                    gameBoard[0][0] = a.text
                elif i == 2:
                    gameBoard[0][1] = a.text
                elif i == 3:
                    gameBoard[0][2] = a.text
                elif i == 4:
                    gameBoard[1][0] = a.text
                elif i == 5:
                    gameBoard[1][1] = a.text
                elif i == 6:
                    gameBoard[1][2] = a.text
                elif i == 7:
                    gameBoard[2][0] = a.text
                elif i == 8:
                    gameBoard[2][1] = a.text
                elif i == 9:
                    gameBoard[2][2] = a.text

        for i in gameBoard:
            print(i)
        print()

class OnePlayer(Screen):
    n = 0
    base = 0
    no = 0

    def __init__(self, **kwargs):
        super(OnePlayer, self).__init__(**kwargs)
        global op
        op = self

    def clear(self, *args):
        for i in range(1, 10, 1):
            name = 'cell' + str(i)
            a = self.ids[name]
            a.text = ''
            a.color = 1, 1, 1, 1
        get = self.ids['player_text']
        get.text = ''
        global playedd, notWon, gameBoard
        playedd = -1
        notWon = True
        gameBoard = [
                     ['00', '01', '02'],
                     ['10', '11', '12'],
                     ['20', '21', '22'],
                    ]

    def play(self, *args):
        cell1 = self.ids['cell1']
        text1 = cell1.text.capitalize()
        if text1 == 'X':
            cell1.color = 1, 0, 0, 1
            cell1.text = text1
        elif text1 == 'O':
            cell1.color = 0, 1, 0, 1
            cell1.text = text1
        elif text1 == '1':
            pass
        else:
            cell1.text = ''

        cell2 = self.ids['cell2']
        text2 = cell2.text.capitalize()
        if text2 == 'X':
            cell2.color = 1, 0, 0, 1
            cell2.text = text2
        elif text2 == 'O':
            cell2.color = 0, 1, 0, 1
            cell2.text = text2
        elif text2 == '2':
            pass
        else:
            cell2.text = ''

        cell3 = self.ids['cell3']
        text3 = cell3.text.capitalize()
        if text3 == 'X':
            cell3.color = 1, 0, 0, 1
            cell3.text = text3
        elif text3 == 'O':
            cell3.color = 0, 1, 0, 1
            cell3.text = text3
        elif text3 == '3':
            pass
        else:
            cell3.text = ''

        cell4 = self.ids['cell4']
        text4 = cell4.text.capitalize()
        if text4 == 'X':
            cell4.color = 1, 0, 0, 1
            cell4.text = text4
        elif text4 == 'O':
            cell4.color = 0, 1, 0, 1
            cell4.text = text4
        elif text4 == '4':
            pass
        else:
            cell4.text = ''

        cell5 = self.ids['cell5']
        text5 = cell5.text.capitalize()
        if text5 == 'X':
            cell5.color = 1, 0, 0, 1
            cell5.text = text5
        elif text5 == 'O':
            cell5.color = 0, 1, 0, 1
            cell5.text = text5
        elif text5 == '5':
            pass
        else:
            cell5.text = ''

        cell6 = self.ids['cell6']
        text6 = cell6.text.capitalize()
        if text6 == 'X':
            cell6.color = 1, 0, 0, 1
            cell6.text = text6
        elif text6 == 'O':
            cell6.color = 0, 1, 0, 1
            cell6.text = text6
        elif text6 == '6':
            pass
        else:
            cell6.text = ''

        cell7 = self.ids['cell7']
        text7 = cell7.text.capitalize()
        if text7 == 'X':
            cell7.color = 1, 0, 0, 1
            cell7.text = text7
        elif text7 == 'O':
            cell7.color = 0, 1, 0, 1
            cell7.text = text7
        elif text7 == '7':
            pass
        else:
            cell7.text = ''

        cell8 = self.ids['cell8']
        text8 = cell8.text.capitalize()
        if text8 == 'X':
            cell8.color = 1, 0, 0, 1
            cell8.text = text8
        elif text8 == 'O':
            cell8.color = 0, 1, 0, 1
            cell8.text = text8
        elif text8 == '8':
            pass
        else:
            cell8.text = ''

        cell9 = self.ids['cell9']
        text9 = cell9.text.capitalize()
        if text9 == 'X':
            cell9.color = 1, 0, 0, 1
            cell9.text = text9
        elif text9 == 'O':
            cell9.color = 0, 1, 0, 1
            cell9.text = text9
        elif text9 == '9':
            pass
        else:
            cell9.text = ''

        getter3 = self.ids['player_text']
        global notWon

        if text1 == text2 and text2 == text3 and text1 != '':
            getter3.text = text1 + ' Wins'
            notWon = False

        elif text4 == text5 and text5  == text6 and text6 != '':
            getter3.text = text4 + ' Wins'
            notWon = False

        elif text7 == text8 and text8 == text9 and text9 != '':
            getter3.text = text7 + ' Wins'
            notWon = False

        elif text1 == text4 and text4 == text7 and text7 != '':
            getter3.text = text1 + ' Wins'
            notWon = False

        elif text2 == text5 and text5 == text8 and text8 != '':
            getter3.text = text2 + ' Wins'
            notWon = False

        elif text3 == text6 and text6 == text9 and text9 != '':
            getter3.text = text3 + ' Wins'
            notWon = False

        elif text1 == text5 and text5 == text9 and text1 != '':
            getter3.text = text1 + ' Wins'
            notWon = False

        elif text3 == text5 and text5 == text7 and text7 != '':
            getter3.text = text3 + ' Wins'
            notWon = False

        tie = 0

        for i in range(1, 10, 1):
            name = 'cell' + str(i)
            a = self.ids[name]
            if a.text == 'X' or a.text == 'O':
                tie += 1
            else:
                pass
        if tie >= 9:
            j = self.ids['player_text']
            j.text = 'Tie'

        global gameBoard
        for i in range(1, 10, 1):
            name = 'cell' + str(i)
            a = self.ids[name]
            if a.text == 'X' or a.text == 'O':
                if i == 1:
                    gameBoard[0][0] = a.text
                elif i == 2:
                    gameBoard[0][1] = a.text
                elif i == 3:
                    gameBoard[0][2] = a.text
                elif i == 4:
                    gameBoard[1][0] = a.text
                elif i == 5:
                    gameBoard[1][1] = a.text
                elif i == 6:
                    gameBoard[1][2] = a.text
                elif i == 7:
                    gameBoard[2][0] = a.text
                elif i == 8:
                    gameBoard[2][1] = a.text
                elif i == 9:
                    gameBoard[2][2] = a.text

        for i in gameBoard:
            print(i)
        print()

        global playedd
        st = self.getResult(gameBoard)
        if playedd % 2 == 0:
            if notWon:
                if st % 2 == 0:
                    pass
                else:
                    global canPlay
                    canPlay = False
                    self.prog()
                    threading.Thread(target = self.compGet(gameBoard)).start()

    def getResult(self, gB):
        no = 0
        for a in gB:
            for _ in a:
                if _ == 'X' or _ == 'O':
                    no += 1
                else:
                    pass
        if no >= 9:
            win = 2
        elif gB[0][0] == gB[0][1] == gB[0][2]:
            win = 3
        elif gB[1][0] == gB[1][1] == gB[1][2]:
            win = 3
        elif gB[2][0] == gB[2][1] == gB[2][2]:
            win = 3
        elif gB[0][0] == gB[1][1] == gB[2][2]:
            win = 3
        elif gB[2][0] == gB[1][1] == gB[0][2]:
            win = 3
        elif gB[0][0] == gB[1][0] == gB[2][0]:
            win = 3
        elif gB[0][1] == gB[1][1] == gB[2][1]:
            win = 3
        elif gB[0][2] == gB[1][2] == gB[2][2]:
            win = 3
        else:
            win = 1
        return win

    def compGet(self, gB, *args):
        free = []
        global coords
        coords = []
        neulist = []
        winlist = []
        for i in gB:
            for _ in i:
                if _ == 'X' or _ == 'O':
                    pass
                else:
                    free.append(_)
        for i in free:
            new = copy.deepcopy(gB)
            f = int(i[0])
            s = int(i[1])
            new[f][s] = 'X'
            stat = self.getResult(new)
            if stat == 3: #win
                coords = f, s
                break
            elif stat == 2: #tie

                coords = f, s
                break
            elif stat == 1: #neutral
                newcopy = copy.deepcopy(new)
                newfree = []
                for newi in newcopy:
                    for new_ in newi:
                        if new_ == 'X' or _ == 'O':
                            pass
                        else:
                            newfree.append(_)
                for newi in free:
                    newnew = copy.deepcopy(newcopy)
                    f = int(newi[0])
                    s = int(newi[1])
                    newnew[f][s] = 'O'
                    newstat = self.getResult(newnew)
                    if newstat == 3: #win
                        coords = f, s
                        winlist.append(coords)
                    elif stat == 2: #tie

                        coords = f, s
                        break
                    elif stat == 1: #neutral
                        coords = f, s
                        neulist.append(coords)
                try:
                    winlist.sort()
                    coords = winlist[0]
                except:
                    neulist.sort()
                    coords = neulist[0]

    def prog(self, *args):
        Clock.schedule_interval(self.update, 1/3)

    def update(self, *args):
        e = self.ids['player_text']
        self.n += 0.333
        if self.n >= 1:
            Clock.unschedule(self.update)
            e.text = ''
            self.n = 0
            global coords, canPlay, gameBoard, playedd
            playedd += 1
            if coords[0] == 0 and coords[1] == 0:
                a = self.ids['cell1']
                a.text = 'X'
            elif coords[0] == 0 and coords[1] == 1:
                a = self.ids['cell2']
                a.text = 'X'
            elif coords[0] == 0 and coords[1] == 2:
                a = self.ids['cell3']
                a.text = 'X'
            elif coords[0] == 1 and coords[1] == 0:
                a = self.ids['cell4']
                a.text = 'X'
            elif coords[0] == 1 and coords[1] == 1:
                a = self.ids['cell5']
                a.text = 'X'
            elif coords[0] == 1 and coords[1] == 2:
                a = self.ids['cell6']
                a.text = 'X'
            elif coords[0] == 2 and coords[1] == 0:
                a = self.ids['cell7']
                a.text = 'X'
            elif coords[0] == 2 and coords[1] == 1:
                a = self.ids['cell8']
                a.text = 'X'
            elif coords[0] == 2 and coords[1] == 2:
                a = self.ids['cell9']
                a.text = 'X'
            else:
                pass
            canPlay = True
            self.play()

        else:
            if self.no >= 3:
                self.base = -1
            if self.no == 0:
                self.base = 1
            self.no += self.base
            e.text = 'Thinking{}'.format('.'*self.no)

class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)
        global mgr
        mgr = self

class Main(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    Main().run()
