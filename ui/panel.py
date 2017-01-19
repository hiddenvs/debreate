# -*- coding: utf-8 -*-

## \package ui.panel

# MIT licensing
# See: docs/LICENSE.txt


import wx

from dbr.styles import PANEL_BORDER


## A wx.Panel with a border
#  
#  This is to work around differences in wx 3.0 with older versions
class BorderedPanel(wx.Panel):
    def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):
        wx.Panel.__init__(self, parent, ID, pos, size, style|PANEL_BORDER, name)


## A wx.ScrolledWindow that sets scrollbars by default
class ScrolledPanel(wx.ScrolledWindow):
    def __init__(self, parent, win_id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                style=wx.HSCROLL|wx.VSCROLL, name=u'scrolledPanel'):
        wx.ScrolledWindow.__init__(self, parent, win_id, pos, size, style, name)
        
        self.SetScrollbars(0, 20, 0, 0)