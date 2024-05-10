using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;
namespace Pg347sum
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int variable = int.Parse(Interaction.InputBox("Enter a positive integer value", "Input Needed"));
            int num2 = 0;
            for (int lcv = 0; lcv <= variable; lcv++) {
                num2 += lcv;
            }
                MessageBox.Show(num2.ToString());
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
