import qtlib
QT_LIB = qtlib.QT_LIB
if QT_LIB == 'PyQt4':
    from PyQt4.QtDesigner import *
elif QT_LIB == 'PyQt5':
    from PyQt5.QtDesigner import *