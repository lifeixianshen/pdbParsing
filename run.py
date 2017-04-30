
from PyQt4 import QtCore, QtGui
from ui import Ui_Dialog
import string
import os, sys
class Apptt(QtGui.QMainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.loginGui()
	def loginGui(self):
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.Tbl_GPCR.setRowCount(100)
		self.ui.Tbl_GPCR.setItem(0, 0, QtGui.QTableWidgetItem(""));
		self.show()
		
	@QtCore.pyqtSlot(int)
	def browsefile(self):
		self.ui.Ln_Filename.setText(QtGui.QFileDialog.getOpenFileName(self, "open file", " ",  "PDB file(*.pdb);;Allfile(*.*)"  ))
		
		file = open(self.ui.Ln_Filename.text())
		title=""
		author=""
		num=0
		while True:
			line=file.readline()
			
			if not line:
				break
			
			if line.find("AUTHOR")!=-1:
				line=line.strip()
				print line
				author=author+line[10:]
				self.ui.Tbl_GPCR.setItem(0, 3, QtGui.QTableWidgetItem(line));
			
			if line.find("HEADER")!=-1:
				num=line.index("-")
				self.ui.Tbl_GPCR.setItem(0, 4, QtGui.QTableWidgetItem(line[num-2:num+7]));
				
			if line[0:5]=="TITLE":
				line=line.strip()
				title=title+line[10:]
				self.ui.Tbl_GPCR.setItem(0, 1, QtGui.QTableWidgetItem(title));
				

			
			if line[12:15]=="REF":
				line=line.strip()
				jounal=jounal+line[19:]
				self.ui.Tbl_GPCR.setItem(0, 2, QtGui.QTableWidgetItem(jounal));
				
			if line[0:6]=="EXPDTA":
				line=line.strip()
				method=method+line[10:]
				self.ui.Tbl_GPCR.setItem(0, 8, QtGui.QTableWidgetItem(method));
			
			if line[11:22]=="RESOLUTION.":
				line=line.strip()
				resolution=resolution+line[26:]
				self.ui.Tbl_GPCR.setItem(0, 9, QtGui.QTableWidgetItem(resolution));
			
			if line[13:47]=="R VALUE     (WORKING + TEST SET) :":
				line=line.strip()
				r_value=r_value+line[48:]
				self.ui.Tbl_GPCR.setItem(0, 10, QtGui.QTableWidgetItem(r_value));
			
			if line[13:26]=="PROTEIN ATOMS":
				line=line.strip()
				protein_num=protein_num+line[40:]
				self.ui.Tbl_GPCR.setItem(0, 1, QtGui.QTableWidgetItem(protein_num));
			
			
	@QtCore.pyqtSlot(int)
	def submitdata(self):
		self.ui.Ln_Filename.setText(QtGui.QFileDialog.getOpenFileName(self, "open file", " ",  "PDB file(*.pdb);;Allfile(*.*)"  ))	
		
app = QtGui.QApplication(sys.argv)
myqq = Apptt()
sys.exit(app.exec_())