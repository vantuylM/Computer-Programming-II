import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(13, 13)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Daytime"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(12, 43)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(12, 73)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Off-peak"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(263, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(536, 40)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(104, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(153, 39)
		self._label1.TabIndex = 4
		self._label1.Text = "Enter amount of time in minutes:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Green
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 130)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(245, 136)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Green
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(282, 130)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(245, 136)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Green
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(554, 130)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(245, 136)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(263, 59)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(530, 68)
		self._label2.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Green
		self.ClientSize = System.Drawing.Size(805, 272)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "pg272LongDistance"
		self.ResumeLayout(False)
		self.PerformLayout()

#A long-distance provider charges the following rates for telephone calls:
#Rate Category Rate per Minute
#Daytime (6:00 a.m. through 5:59 P.M.) $0.07
#Evening (6:00 p.m. through 11:59 P.M.) $0.12
#Off-Peak (12:00 a.m. through 5:59 A.M.) $0.05
#Create an application that allows the user to select a rate category (from a set of
#radio buttons) and enter the number of minutes of the call, then displays the
#charges. Include a Clear button that clears the input and calculated values, and an
#Exit button that closes the window. Error checking: the minutes input by the user
#must be numeric, and it must be greater than zero.
#Use the following test data to determine if the application is calculating properly:
#Rate Category and Minutes Charge
#Daytime, 20 minutes $ 1.40
#Evening, 20 minutes $ 2.40
#Off-peak, 20 minutes $ 1.00

	def Button1Click(self, sender, e):
		Time = int(self._textBox1.Text)
		if self._radioButton1.Checked:
			rate = 0.07
		if self._radioButton2.Checked:
			rate = 0.12
		if self._radioButton3.Checked:
			rate = 0.05
		charge = rate * Time
		self._label2.Text = str(charge)
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()