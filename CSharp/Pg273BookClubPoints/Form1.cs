using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = (textBox1.Text);
            if (num1 == 0)
                num1 = 0;
            if (num1 == 1)
                num1 = 5;
            if (num1 == 2)
                num1 = 15;
            if (num1 == 3)
                num1 = 30;
            if (int num1 >= 4)
                num1 = 60;
            label3.Text = num1.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label3.Text = "";
            textBox1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
