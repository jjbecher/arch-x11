import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Drag, Key, Screen, Group, Click, Rule, KeyChord, Match, DropDown, ScratchPad
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer

from modules.paths import home
from modules.keys import mod, mod1, mod2, keys
from modules.mouse import mouse
from modules.groups import groups
from modules.colors import current_theme #se movera a donde se necesite color
from modules.layouts import layouts
from modules.widgets import *  # baby jesus llora
from modules.screens import screens

# logfile: ~/.local/share/qtile

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)



# SCRATCHPADS
#groups.append(ScratchPad("0",[DropDown("notes", 'alacritty -o "window.opacity=1" -e "joplin"', x=0.05, y=0.02, width=0.9, height=0.95, on_focus_lost_hide=True)]))
#groups.append(ScratchPad("0",[DropDown("notes", 'xfce4-terminal -e "joplin"', x=0.05, y=0.02, width=0.9, height=0.95, on_focus_lost_hide=True)]))
#keys.append(Key([mod], 's', lazy.group['0'].dropdown_toggle('notes')))


dgroups_key_binder = None
dgroups_app_rules = []
main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for() or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"] # "rename"

floats_keep_above = True
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
# use xprop to get wm_class
floating_layout = layout.Floating(float_rules=[
	Match(wm_class = 'qalculate-gtk'),
    Match(wm_class = 'Galculator'),
    Match(wm_class = 'xfce4-terminal'),
    Match(wm_class = 'pavucontrol'),
    Match(wm_class = 'nitrogen'),
    Match(title = 'P-Dal Capture'),
    Match(title = 'Save Document?'), # Libre Office
    Match(title = 'Torrent Options'), # Transmission 
    Match(title = 'Question'), # Geany
    Match(title = 'Save As'), # Firefox
    ], border_focus = current_theme[6])

focus_on_window_activation = "smart" # focus or smart
wmname = "LG3D"
