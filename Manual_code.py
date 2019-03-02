#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import io

import requests
from wx.core import wx


class CheckCodeInputDlg(wx.Dialog):
    def __init__(self, get_vcode_data_func, title,parent=None, size=(300, 100)):
        self.get_check_code_data_func = get_vcode_data_func

        wx.Dialog.__init__(self, parent, -1, title=title,
                           size=size, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.check_code_ctl = wx.StaticBitmap(self)
        self.check_code_ctl.Bind(wx.EVT_LEFT_DOWN, self.OnUpdateVCode)
        self.sizer.Add(self.check_code_ctl, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2)

        self.text = wx.TextCtrl(self, -1, "", style=wx.TE_PROCESS_ENTER)
        self.text.Bind(wx.EVT_TEXT_ENTER, self.OnEnterPress)
        self.sizer.Add(self.text, 0, wx.ALIGN_CENTRE|wx.ALL, 3)

        self.SetSizer(self.sizer)

        self.OnUpdateVCode(None)

    def OnUpdateVCode(self, event):
        im = self.get_check_code_data_func()
        stream = io.BytesIO(im)

        bmp = wx.Bitmap(wx.Image(stream))
        self.check_code_ctl.SetBitmap(bmp)
        self.Fit()

    def OnEnterPress(self, event):
        self.check_code = self.text.GetValue()
        if not self.check_code:
            return

        self.EndModal(wx.ID_OK)

    def get_check_code(self):
        return self.text.GetValue()

def input_vcode(get_vcode_data_func, parent=None, title="请输入验证码(点击图片切换)"):
    if not parent:
        app = wx.App(redirect=False)
    dlg = CheckCodeInputDlg(get_vcode_data_func,title ,parent)
    dlg.CenterOnScreen()
    val = dlg.ShowModal()
    dlg.Destroy()
    return dlg.get_check_code()

class Manual:
    def __init__(self, *args, **kwargs):
        self.parent = None

    def set_parent(self,parent):
        self.parent = parent

    def create(self, get_vcode_data_func, im_type=6113):
        vcode = input_vcode(get_vcode_data_func, self.parent)
        return {'Result': vcode, 'Id': 'manul'}

    def report_error(self, id):
        pass

def create_dama(*args, **kwargs):
    return Manual(*args, **kwargs)


if __name__ == '__main__':
    def get_vcode_data_func():
        url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&' + str(random.random())
        return requests.get(url).content

    dm = Manual()
    result = dm.create(get_vcode_data_func)
    print(result)


