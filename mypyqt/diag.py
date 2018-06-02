#!/usr/bin/env python
import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)

lineEdit=QLineEdit()
go=QPushButton("&Go");
h1=QHBoxLayout()
h1.addWidget(lineEdit)
h1.addWidget(go)

ok=QPushButton("&OK")
cancel=QPushButton("&Cancel")
h2=QHBoxLayout()
h2.addStretch(1)
h2.addWidget(ok)
h2.addWidget(cancel)

layout=QVBoxLayout()
layout.addLayout(h1)
layout.addLayout(h2)

widget=QWidget()
widget.setLayout(layout)
widget.show()

app.exec_()



