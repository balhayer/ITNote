# Tmux
## Installation

- apt-get install tmux
- Configuration file: ~/.tmux.conf
- set-option -g mouse on: enable mouse support
- set-option -g history-limit 3000: set history limit
- After making change: source-file ~/.tmux.conf

Commands

- Windows and Pane: Command ctrl_b, then:
    - c: create window
    - , (comma): rename window
    - p|n|<number of window>: previous|next window
    - w: list windows
    - %: split windows
    - ” (double quote) | :split-windows: split horizontally
    - ?: help
    - <> (left, right arrow): change between panels
    - Ctrl_<> to resize panel
    - <space>: change panel layout
    - { }: move panel around
    - [: copy mode
        - Move up/down, then Ctrl_<space> to start highlight, then move cursor
        - <Enter> or Alt_w (Esc_w on Mac) to copy text to tmux clipboard
        - Ctrl_b, ] to paste
        - q to quit
    - t: show time panel, q for quit
    - q: to show number of panel, <number> to jump to that panel
    - :join-pane -s <windows>.<pane>
    - z: zoom/unzoom a pane
    - x|&: force kill all unresponsive process in a pane|window
    - L (lower case L): switch to last used windows
- Alt_. (dot): cycle through last word of previous commands
- Session
    - tmux new -s <name>: Create new session
    - Ctrl_b, d: detach session
    - tmux ls | list-sessions: list tmux sessions
    - tmux attach [-t <session name>]: re-attach session
    - <prefix> (|): previous | next session
- Tmux list-keys = Ctrl_b,? : see all hot keys
- Note:
    - Paste in vi editor: hold shift and right mouse click
- Capture pane content to file:
    - Ctrl_b, :
    - Capture-pane -b <buffername> -S -: -S – Start of history
    - Save-buff -b <buffername> <file>
    - https://blog.sleeplessbeastie.eu/2019/10/28/how-to-store-the-contents-of-tmux-pane/
    - https://ricochen.wordpress.com/2011/04/07/capture-tmux-output-the-much-less-painful-way/

## Reference
- https://www.linode.com/docs/networking/ssh/persistent-terminal-sessions-with-tmux/
- https://gist.github.com/russelldb/06873e0ad4f5ba1c4eec1b673ff4d4cd