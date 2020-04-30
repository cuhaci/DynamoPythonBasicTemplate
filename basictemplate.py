import clr
clr.AddRreference('ProtoGeomotry')
from Autodesk.DesignScript.Geometry import *

#Import Revit Nodes
clr.AddRreference("RevitNodes")
import Revit

#Import Revit elements
from Revit.Elements import *

#Import Document Manager
clr.AddRreference("RevitServices")
import RevitServices
from RevitServices.Persistaence import DocumentManager

Import System

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

#Assign your output to the OUT variable
OUT=[doc,uiapp,app]

