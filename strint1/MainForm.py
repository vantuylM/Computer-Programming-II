import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(75, 62)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 34)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter text:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(206, 62)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(220, 31)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(75, 122)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(125, 34)
		self._label2.TabIndex = 2
		self._label2.Text = "Duplicates:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Chartreuse
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(206, 122)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(220, 34)
		self._label3.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SeaGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 440)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(169, 108)
		self._button1.TabIndex = 4
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SeaGreen
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(242, 440)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(169, 108)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SeaGreen
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(500, 440)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(169, 108)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SpringGreen
		self.ClientSize = System.Drawing.Size(681, 560)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "strint1"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		mystr = self._textBox1.Text.lower()
		for lcv in range(len(mystr)):
			for lcv2 in range(lcv+1, len(mystr)):
				letter1 = mystr[lcv]
				letter2 = mystr[lcv2]
				if letter1 == letter2:
					self._label3.Text += letter2 + " "

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()