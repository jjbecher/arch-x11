from libqtile.config import Group, Key
from libqtile.lazy import lazy

from .keys import keys, mod

# GROUPS
groups = []
group_names = ["1", "2", "3", "4", "5", "6",]
group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ",]
group_layouts = ["ratiotile", "ratiotile", "ratiotile", "ratiotile", "ratiotile", "ratiotile",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))


for i in groups:
    keys.extend([

# CHANGE GROUPS
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        #Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

# MOVE WINDOW TO SELECTED WORKSPACE AND FOLLOW MOVED WINDOW TO WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])
