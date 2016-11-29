# -*- coding: utf-8 -*-

## \package dbr.progress

# MIT licensing
# See: docs/LICENSE.txt


import wx

from dbr.language import GT


## A progress dialog that is compatible between wx versions
class ProgressDialog(wx.ProgressDialog):
    def __init__(self, parent, title=GT(u'Progress'), message=wx.EmptyString, maximum=100,
            style=wx.PD_APP_MODAL|wx.PD_AUTO_HIDE):
        wx.ProgressDialog.__init__(self, title, message, maximum, parent, style)
        
        self.active = None
        
        if wx.MAJOR_VERSION < 3 and self.GetWindowStyle() & wx.PD_CAN_ABORT:
            wx.EVT_CLOSE(self, self.OnAbort)
            for C in self.GetChildren():
                if isinstance(C, wx.Button) and C.GetId() == wx.ID_CANCEL:
                    C.Bind(wx.EVT_BUTTON, self.OnAbort)
    
    
    ## TODO: Doxygen
    def Destroy(self, *args, **kwargs):
        if wx.MAJOR_VERSION < 3:
            self.EndModal(0)
        
        return wx.ProgressDialog.Destroy(self, *args, **kwargs)
    
    
    ## TODO: Doxygen
    def GetGauge(self):
        for C in self.GetChildren():
            if isinstance(C, wx.Gauge):
                return C
    
    
    ## TODO: Doxygen
    def GetRange(self, *args, **kwargs):
        if wx.MAJOR_VERSION < 3:
            return self.GetGauge().GetRange()
        
        return wx.ProgressDialog.GetRange(self, *args, **kwargs)
    
    
    ## TODO: Doxgen
    def GetValue(self, *args, **kwargs):
        if wx.MAJOR_VERSION < 3:
            return self.GetGauge().GetValue()
        
        return wx.ProgressDialog.GetValue(self, *args, **kwargs)
    
    
    ## TODO: Doxygen
    def OnAbort(self, event=None):
        self.active = False
        
        if event:
            event.Skip()
    
    
    ## TODO: Doxygen
    def SetMessage(self, message):
        for C in self.GetChildren():
            if isinstance(C, wx.StaticText):
                return C.SetLabel(message)
        
        return False
    
    
    ## TODO: Doxygen
    def SetRange(self, *args, **kwargs):
        if wx.MAJOR_VERSION < 3:
            return self.GetGauge().SetRange(*args, **kwargs)
        
        return wx.ProgressDialog.SetRange(self, *args, **kwargs)
    
    
    ## TODO: Doxygen
    def ShowModal(self, *args, **kwargs):
        if wx.MAJOR_VERSION < 3:
            self.active = True
        
        return wx.ProgressDialog.ShowModal(self, *args, **kwargs)
    
    
    ## Override WasCancelled method for compatibility wx older wx versions
    def WasCancelled(self, *args, **kwargs):
        if wx.MAJOR_VERSION < 3:
            if self.active == None:
                return False
            
            return not self.active
        
        return wx.ProgressDialog.WasCancelled(self, *args, **kwargs)