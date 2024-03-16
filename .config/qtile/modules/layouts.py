import re # for regex expressions on float_rules?

from libqtile.config import Match
from libqtile import layout
from .colors import current_theme

def init_layout_theme():
    return {
		"margin":9,
		"border_width":4,
		"border_focus": current_theme[3], # Unico uso
		"border_normal": current_theme[9]
		}

layout_theme = init_layout_theme()

# LAYOUTS
layouts = [
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    #layout.MonadWide(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Bsp(**layout_theme),   
    #layout.Max(**layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.Zoomy(),
    #layout.TreeTab(sections=['Tabs:'], panel_width=85, bg_color="#2F343F", fontsize=10, place_right=True),
    #layout.Floating(margin=3, border_width=1, border_focus="#fba922", border_normal="#fba922"),
]

# floating windows rules
# run the utility of `xprop` to see the wm class and name of an X client.
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
    ], border_focus = current_theme[3])