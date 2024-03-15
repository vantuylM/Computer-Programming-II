
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class StudentForm1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self.SuspendLayout()
		# 
		# StudentForm1
		# 
		self.ClientSize = System.Drawing.Size(454, 330)
		self.Name = "StudentForm1"
		self.Text = "StudentForm1"
		self.ResumeLayout(False)

