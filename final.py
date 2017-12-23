import urwid
import os
import time 

os.system("figlet Shenzhen")
time.sleep(1)

def menu_button(caption, callback):
    button = urwid.Button(caption)
    urwid.connect_signal(button, 'click', callback)
    return urwid.AttrMap(button, None, focus_map='reversed')

def sub_menu(caption, choices):
    contents = menu(caption, choices)
    def open_menu(button):
        return top.open_box(contents)
    return menu_button([caption, u'...'], open_menu)

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    body.extend(choices)
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen1(button):
    response = os.system("cmus")
  
def item_chosen2(button):
    response = os.system("ranger")

def item_chosen3(button):
    response = os.system("htop") 

def item_chosen4(button):
    response = os.system("sl")

def item_chosen5(button):
    response = os.system("wal")

def item_chosen6(button):
    response = os.system("mkdir dicks")

def exit_program(button):
    raise urwid.ExitMainLoop()

menu_top = menu(u'Shenzhen', [
    sub_menu(u'Hacking Tools', [
        sub_menu(u'', [
            menu_button(u'cmus', item_chosen1),
            menu_button(u'ranger', item_chosen2),
        ]),
    sub_menu(u'Dicks Out', [
        menu_button(u'wal', item_chosen5)
    ])
    ]),
    sub_menu(u'System', [
        sub_menu(u'Preferences', [
            menu_button(u'htop', item_chosen3),
        ]),
        menu_button(u'sl', item_chosen4),
    ]),
])

class CascadingBoxes(urwid.WidgetPlaceholder):
    max_box_levels = 4

    def __init__(self, box):
        super(CascadingBoxes, self).__init__(urwid.SolidFill(u'/'))
        self.box_level = 0
        self.open_box(box)

    def open_box(self, box):
        self.original_widget = urwid.Overlay(urwid.LineBox(box),
            self.original_widget,
            align='center', width=('relative', 80),
            valign='middle', height=('relative', 80),
            min_width=24, min_height=8,
            left=self.box_level * 3,
            right=(self.max_box_levels - self.box_level - 1) * 3,
            top=self.box_level * 2,
            bottom=(self.max_box_levels - self.box_level - 1) * 2)
        self.box_level += 1

    def keypress(self, size, key):
        if key == 'esc' and self.box_level > 1:
            self.original_widget = self.original_widget[0]
            self.box_level -= 1
        else:
            return super(CascadingBoxes, self).keypress(size, key)

top = CascadingBoxes(menu_top)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
