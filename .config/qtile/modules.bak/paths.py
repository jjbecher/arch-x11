import os


# PATHS
home = os.path.expanduser('~')
myTerm = "alacritty"
rofi_file_find = 'rofi  -show find -modi find:~/.config/rofi/scripts/file-finder -width 1600'
rofi_power_menu = 'rofi  -show menu \
-modi "menu:~/.config/rofi/scripts/power-menu --choices=reboot/shutdown/logout/suspend --no-symbols" \
-config "~/.config/rofi/themes/Pmenu.rasi" \
-font "JetBrains NF 14" \
-theme-str "window {width: 12em;}"'
notes_app = '~/Applications/Joplin-2.7.13.AppImage' #problemas con cambio de version appimg 
kill_pid = f'dex {home}/.local/share/applications/ropy-kill.desktop'