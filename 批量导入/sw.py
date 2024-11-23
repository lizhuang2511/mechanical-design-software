# -*- coding: utf-8 -*-
import win32com.client as win32
import pythoncom
sw_app = win32.Dispatch("Sldworks.application") #引入sldworks接口
sw_app.Visible = True #是否可视化
arg_Nothing = win32.VARIANT(pythoncom.VT_DISPATCH, None) #转义VBA中不同变量nothing
Part=sw_app.OpenDoc(r'C:\Users\Administrator\Desktop\CDQMB25-50-M9BL-零件.SLDPRT',1)
swModel= sw_app.ActiveDoc
#visibility = sw_app.DocumentVisible(False, swDocPART)
#myDimension1 = Part.Parameter("D6@草图1@镀锌平板.Part")
#myDimension1.SystemValue = 0.4
#Set myModelView = Part.ActiveView
#myModelView.FrameState = swWindowState_e.swWindowMaximized
swSelMgr = swModel.SelectionManager
swFeat = swSelMgr.GetSelectedObject6(1, 0)
#swCustPropMgr = swFeat.CustomPropertyManager
print(swModel.GetPathName)
print(swModel.FileSummaryInfo)
d=swModel.FileSummaryInfo
Description = Part.GetCustomInfoValue("物料名称", "类型")