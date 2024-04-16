namespace Prog88a
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.lblMax = new System.Windows.Forms.Label();
            this.lblAbs = new System.Windows.Forms.Label();
            this.lblAvg = new System.Windows.Forms.Label();
            this.lblProduct = new System.Windows.Forms.Label();
            this.lblDiff = new System.Windows.Forms.Label();
            this.lblSum = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.lblMin = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // textBox1
            // 
            this.textBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox1.Location = new System.Drawing.Point(12, 55);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(254, 40);
            this.textBox1.TabIndex = 0;
            // 
            // textBox2
            // 
            this.textBox2.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBox2.Location = new System.Drawing.Point(12, 103);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(254, 40);
            this.textBox2.TabIndex = 1;
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.Location = new System.Drawing.Point(273, 13);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(175, 39);
            this.button1.TabIndex = 2;
            this.button1.Text = "Calculate";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button2.Location = new System.Drawing.Point(272, 58);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(175, 39);
            this.button2.TabIndex = 3;
            this.button2.Text = "Clear";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button3.Location = new System.Drawing.Point(272, 103);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(175, 39);
            this.button3.TabIndex = 4;
            this.button3.Text = "Exit";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // label1
            // 
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(254, 39);
            this.label1.TabIndex = 5;
            this.label1.Text = "Enter 2 #s:";
            // 
            // label2
            // 
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(12, 146);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(222, 39);
            this.label2.TabIndex = 6;
            this.label2.Text = "Sum:";
            // 
            // label3
            // 
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(12, 185);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(222, 39);
            this.label3.TabIndex = 7;
            this.label3.Text = "Difference:";
            // 
            // label4
            // 
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(12, 224);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(222, 39);
            this.label4.TabIndex = 8;
            this.label4.Text = "Product:";
            // 
            // label5
            // 
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.Location = new System.Drawing.Point(12, 263);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(222, 39);
            this.label5.TabIndex = 9;
            this.label5.Text = "Avg:";
            // 
            // label6
            // 
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.Location = new System.Drawing.Point(12, 302);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(222, 39);
            this.label6.TabIndex = 10;
            this.label6.Text = "Abs. Distance:";
            // 
            // label7
            // 
            this.label7.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label7.Location = new System.Drawing.Point(12, 337);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(222, 39);
            this.label7.TabIndex = 11;
            this.label7.Text = "Max";
            // 
            // lblMax
            // 
            this.lblMax.BackColor = System.Drawing.Color.Maroon;
            this.lblMax.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblMax.Location = new System.Drawing.Point(266, 347);
            this.lblMax.Name = "lblMax";
            this.lblMax.Size = new System.Drawing.Size(226, 35);
            this.lblMax.TabIndex = 17;
            // 
            // lblAbs
            // 
            this.lblAbs.BackColor = System.Drawing.Color.Maroon;
            this.lblAbs.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblAbs.Location = new System.Drawing.Point(267, 308);
            this.lblAbs.Name = "lblAbs";
            this.lblAbs.Size = new System.Drawing.Size(226, 39);
            this.lblAbs.TabIndex = 16;
            // 
            // lblAvg
            // 
            this.lblAvg.BackColor = System.Drawing.Color.Maroon;
            this.lblAvg.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblAvg.Location = new System.Drawing.Point(266, 269);
            this.lblAvg.Name = "lblAvg";
            this.lblAvg.Size = new System.Drawing.Size(226, 39);
            this.lblAvg.TabIndex = 15;
            // 
            // lblProduct
            // 
            this.lblProduct.BackColor = System.Drawing.Color.Maroon;
            this.lblProduct.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblProduct.Location = new System.Drawing.Point(268, 230);
            this.lblProduct.Name = "lblProduct";
            this.lblProduct.Size = new System.Drawing.Size(222, 39);
            this.lblProduct.TabIndex = 14;
            // 
            // lblDiff
            // 
            this.lblDiff.BackColor = System.Drawing.Color.Maroon;
            this.lblDiff.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblDiff.Location = new System.Drawing.Point(268, 191);
            this.lblDiff.Name = "lblDiff";
            this.lblDiff.Size = new System.Drawing.Size(222, 39);
            this.lblDiff.TabIndex = 13;
            // 
            // lblSum
            // 
            this.lblSum.BackColor = System.Drawing.Color.Maroon;
            this.lblSum.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblSum.Location = new System.Drawing.Point(267, 151);
            this.lblSum.Name = "lblSum";
            this.lblSum.Size = new System.Drawing.Size(222, 40);
            this.lblSum.TabIndex = 12;
            // 
            // label14
            // 
            this.label14.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label14.Location = new System.Drawing.Point(12, 382);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(222, 39);
            this.label14.TabIndex = 18;
            this.label14.Text = "Min";
            // 
            // lblMin
            // 
            this.lblMin.BackColor = System.Drawing.Color.Maroon;
            this.lblMin.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblMin.Location = new System.Drawing.Point(266, 382);
            this.lblMin.Name = "lblMin";
            this.lblMin.Size = new System.Drawing.Size(222, 39);
            this.lblMin.TabIndex = 19;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(514, 430);
            this.Controls.Add(this.lblMin);
            this.Controls.Add(this.label14);
            this.Controls.Add(this.lblMax);
            this.Controls.Add(this.lblAbs);
            this.Controls.Add(this.lblAvg);
            this.Controls.Add(this.lblProduct);
            this.Controls.Add(this.lblDiff);
            this.Controls.Add(this.lblSum);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label lblMax;
        private System.Windows.Forms.Label lblAbs;
        private System.Windows.Forms.Label lblAvg;
        private System.Windows.Forms.Label lblProduct;
        private System.Windows.Forms.Label lblDiff;
        private System.Windows.Forms.Label lblSum;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label lblMin;
    }
}

