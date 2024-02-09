import System.Drawing
import System.Windows.Forms
# import Form1
# form1 = Form1.Form1()
# from Form1 import Form1

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Brown
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(60, 48)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(577, 469)
		self._button1.TabIndex = 0
		self._button1.Text = "Shows New Form"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(686, 564)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MultiForms"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Hello, World!")
		form1.Show()
		self.Hide()
		
		#from secondForm import *
		#form2 = secondForm()
		#form2.Show