#!/usr/bin/env python3


import wx
import wx.adv


from wxmpd import mpc


TRAY_TOOLTIP = 'WXMPD'
TRAY_ICON = '/usr/share/icons/Adwaita/scalable/emblems/emblem-music-symbolic.svg'


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):

    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, '\uf025 WXMPD', None)
        menu.AppendSeparator()
        create_menu_item(menu, '\uf04a Prevoius', self.on_mpc_prev)
        create_menu_item(menu, '\uf04b Play', self.on_mpc_play)
        create_menu_item(menu, '\uf04c Pause', self.on_mpc_pause)
        create_menu_item(menu, '\uf04d Stop', self.on_mpc_stop)
        create_menu_item(menu, '\uf04e Next', self.on_mpc_next)
        menu.AppendSeparator()
        create_menu_item(menu, '\uf08b Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        print('Tray icon was left-clicked')

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()

    # MPC actions

    def on_mpc_play(self, event):
        mpc.mpc_action('play')

    def on_mpc_pause(self, event):
        mpc.mpc_action('pause')

    def on_mpc_prev(self, event):
        mpc.mpc_action('prev')

    def on_mpc_stop(self, event):
        mpc.mpc_action('stop')

    def on_mpc_next(self, event):
        mpc.mpc_action('next')


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True


def main():
    # Start application
    app = App(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
