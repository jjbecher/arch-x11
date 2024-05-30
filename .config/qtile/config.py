import os
import subprocess

# qtile imports
from libqtile import qtile
from libqtile.lazy import lazy
from libqtile import hook
#from libqtile.config import Key, Screen, Group, Click, Rule, KeyChord, Match

# qtile/modules imports
from modules.paths import home
from modules.keys import mod, mod1, mod2, keys
from modules.mouse import mouse
from modules.groups import groups
from modules.colors import current_theme
from modules.layouts import layouts, floating_layout
from modules.screens import screens

# TaskList looses color and theme if not present
from modules.widgets import widget_defaults

# default config: https://docs.qtile.org/en/latest/manual/config/default.html
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

main = None
dgroups_key_binder = None
dgroups_app_rules = []
floating_types = ["notification", "toolbar", "splash", "dialog"] # "rename"
floats_keep_above = True
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

focus_on_window_activation = "smart" # focus or smart
wmname = "LG3D"
