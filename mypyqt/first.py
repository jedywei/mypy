#!/usr/bin/env python
import sys
from PyQt4.QtGui import *
app = QApplication(sys.argv)
#widget = QWidget()
#widget.resize(200,200)
#widget.move(10,10)
#widget.setWindowTitle("jedy's first PyQt application")
#widget.show()
#button=QPushButton("H&ello!")
#button.resize(200,75)
#button.move(500,400)
#button.setWindowTitle("Hello World")
#button.clicked.connect(button.close)
#button.show()

ok=QPushButton("&OK")
cancel=QPushButton("&Cancel")

layout=QHBoxLayout()
layout.addWidget(ok)
layout.addWidget(cancel)

widget=QWidget()
widget.setLayout(layout)
widget.show()

app.exec_()


