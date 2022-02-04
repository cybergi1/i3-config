from i3ipc import Event , Connection

i3 = Connection()
def on_window_focus(i3, e):
    focused_window = e.container
    fullscreen=bool(focused_window.fullscreen_mode)
    if(not fullscreen):
        if(focused_window.rect.width>focused_window.rect.height):
            i3.command('split horizontal')
        else: 
            i3.command('split vertical')

i3.on(Event.WINDOW_FOCUS, on_window_focus)
i3.main()
