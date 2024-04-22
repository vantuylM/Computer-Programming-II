using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lang85cForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            num1 = num1 - 165;
            double num2 = (double)num1 / 100.0;
            double num3 = (double)Math.Round(num2, 2);
            label4.Text = num3.ToString();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
