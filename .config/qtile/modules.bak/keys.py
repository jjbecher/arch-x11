from libqtile.config import Key
from libqtile.command import lazy
from libqtile import layout

from .paths import *

mod = "mod4" #  mod4 or mod = super key
mod1 = "alt"
mod2 = "control"

# KEYBINDINGS
keys = [
	# SUPER + KEYS
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "w", lazy.window.toggle_floating()),
    Key([mod], "e", lazy.spawn(rofi_file_find)), 
    Key([mod], "r", lazy.layout.flip()), # flip layout for monadrall/monadwide
    Key([mod], "a", lazy.spawn(myTerm + ' -e ranger')), 
    Key([mod], "s", lazy.spawn()),
    Key([mod], "d", lazy.spawn('rofi -show drun -font "JetBrains NF 14" -theme-str "window {width: 28em;}"')),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
	Key([mod], "z", lazy.spawn()),
	Key([mod], "x", lazy.spawn(kill_pid)), 
	Key([mod], "period", lazy.next_screen()), 
    Key([mod], "space", lazy.next_screen()),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(myTerm)),
	Key([mod], "Tab", lazy.next_layout()),
    # SUPER + KEYPAD
    Key([mod], "KP_Insert", lazy.restart()), # KP 0
    Key([mod], "KP_Subtract", lazy.spawn(rofi_power_menu)), # KP -
    Key([mod], "KP_Add", lazy.spawn('pavucontrol')), # KP +
	# SUPER + SHIFT + KEYS
    Key([mod, "shift"], "q", lazy.spawn('qalculate-gtk')),
    Key([mod, "shift"], "w", lazy.spawn('geany')),
    Key([mod, "shift"], "e", lazy.spawn('vscodium')),
    Key([mod, "shift"], "a", lazy.spawn('firefox')),
    Key([mod, "shift"], "s", lazy.spawn('./.local/bin/internet-search')), # No es un rofi modi es un script que usa rofi
    Key([mod, "shift"], "d", lazy.spawn('chromium -no-default-browser-check')),
	Key([mod, "shift"], "z", lazy.spawn(myTerm)),	
    Key([mod, "shift"], "x", lazy.spawn(myTerm)),
    Key([mod, "shift"], "c", lazy.spawn(myTerm)), 
    Key([mod, "shift"], "Return", lazy.spawn('Thunar')),
	# SUPER + CTRL KEYS
    #Key([mod, "control"], "s", lazy.spawn('libreoffice')),
    #Key([mod, "shift"], "x", lazy.shutdown()),
	# CONTROL KEYS
	#Key([mod], "z", lazy.next_screen()),
	# CONTROL + ALT KEYS
	Key(["mod1"], "Tab", lazy.spawn("rofi -show window")),
    #Key(["mod1", "control"], "Next", lazy.spawn('conky-rotate -n')), #
    #Key(["mod1", "control"], "Prior", lazy.spawn('conky-rotate -p')), #
    #Key(["mod1", "control"], "c", lazy.spawn('catfish')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    #Key(["mod1", "control"], "w", lazy.spawn('')),
	# ALT + Fx KEYS
    #Key(["mod1"], "F2", lazy.spawn('gmrun')),
    #Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),
	# CONTROL + SHIFT KEYS
    #Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),
    Key([], "Print", lazy.spawn('xfce4-screenshooter')),
	# MULTIMEDIA KEYS
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
	#Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
	#Key([], "XF86AudioNext", lazy.spawn("mpc next")),
	#Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
	#Key([], "XF86AudioStop", lazy.spawn("mpc stop")),
	# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
	# RESIZE UP, DOWN, LEFT, RIGHT
	# Commented lazy.layouts generate errors on qtiles logfile
    Key([mod, "control"], "l",
        #lazy.layout.grow_right(),
        lazy.layout.grow(),
        #lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        #lazy.layout.grow_right(),
        lazy.layout.grow(),
        #lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        #lazy.layout.grow_left(),
        lazy.layout.shrink(),
        #lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        #lazy.layout.grow_left(),
        lazy.layout.shrink(),
        #lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        #lazy.layout.grow_up(),
        lazy.layout.grow(),
        #lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        #lazy.layout.grow_up(),
        lazy.layout.grow(),
        #lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        #lazy.layout.grow_down(),
        lazy.layout.shrink(),
        #lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        #lazy.layout.grow_down(),
        lazy.layout.shrink(),
        #lazy.layout.increase_nmaster(),
        ),
	# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
	# FUNCTION KEYS
    Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),
	# FLIP LAYOUT FOR BSP
	#Key([mod, "mod1"], "k", lazy.layout.flip_up()),
	#Key([mod, "mod1"], "j", lazy.layout.flip_down()),
	#Key([mod, "mod1"], "l", lazy.layout.flip_right()),
	#Key([mod, "mod1"], "h", lazy.layout.flip_left()),
	# MOVE WINDOWS UP OR DOWN BSP LAYOUT
	#Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
	#Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
	#Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
	#Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ]