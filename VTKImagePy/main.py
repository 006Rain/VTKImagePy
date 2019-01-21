import sys
sys.path.append( './Filters' )

from PyQt5.QtWidgets import QApplication
from Widgets.MainWindow import MainWindow
import GlobalDef as gldef

if __name__ == '__main__':
	app = QApplication( sys.argv )
	
	#init global define
	gldef.InitGlobalDef()

	#create Qt MainWindow
	mainWin = MainWindow()
	mainWin.show()
	
	sys.exit( app.exec_() )