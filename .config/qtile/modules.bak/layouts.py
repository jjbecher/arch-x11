from libqtile import layout
from .colors import current_theme

def init_layout_theme():
    return {
		"margin":8,
		"border_width":3,
		#"border_focus": "#5294e2", #"#acb9ca",
		"border_focus": current_theme[6], #"#5294e2", #"#acb9ca",
		"border_normal": current_theme[9] # "#4c566a"
		}

layout_theme = init_layout_theme()

# LAYOUTS
layouts = [
    layout.RatioTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Bsp(**layout_theme),   
    # layout.Max(**layout_theme),
    # layout.TreeTab(sections=['Tabs:'], panel_width=85, bg_color="#2F343F", fontsize=10, place_right=True),
    # layout.Floating(margin=3, border_width=1, border_focus="#fba922", border_normal="#fba922"),
    # layout.Stack(num_stacks=2)
]