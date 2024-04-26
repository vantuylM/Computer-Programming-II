﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273MassAndWeight
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
            double newtons = (double) num1 * 9.8;
            if (newtons > 1000)
                label2.Text = "It is too heavy";
            else if (newtons < 10)
                label2.Text = "It is too light";
            else
                label2.Text = (newtons.ToString());
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = "";
            textBox1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
