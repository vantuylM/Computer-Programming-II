import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Red
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 396)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(181, 157)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(255, 396)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(181, 157)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(485, 396)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(181, 157)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(183, 50)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter A Three Digit Number:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(202, 19)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(333, 40)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(202, 82)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(333, 40)
		self._textBox2.TabIndex = 6
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 72)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(183, 50)
		self._label2.TabIndex = 5
		self._label2.Text = "Enter A Three Digit Number:"
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(202, 145)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(333, 40)
		self._textBox3.TabIndex = 8
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(13, 135)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(183, 50)
		self._label3.TabIndex = 7
		self._label3.Text = "Enter A Three Digit Number:"
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(202, 205)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(333, 40)
		self._textBox4.TabIndex = 10
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(13, 195)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(183, 50)
		self._label4.TabIndex = 9
		self._label4.Text = "Enter A Three Digit Number:"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(13, 274)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(67, 31)
		self._label5.TabIndex = 11
		self._label5.Text = "Sum:"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 335)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(106, 32)
		self._label6.TabIndex = 12
		self._label6.Text = "Average:"
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(104, 274)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(562, 31)
		self._label7.TabIndex = 13
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(119, 335)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(547, 31)
		self._label8.TabIndex = 14
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.OrangeRed
		self.ClientSize = System.Drawing.Size(678, 565)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Sum = int(self._textBox1.Text) + int(self._textBox2.Text) + int(self._textBox3.Text) + int(self._textBox4.Text)
		Average = Sum / 4
		self._label7.Text = str(Sum)
		self._label8.Text = str(Average)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()