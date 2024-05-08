using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSalesCS
{
    public partial class GeneralForm : Form{
        private Form myParent;
    
        public GeneralForm(Form myParent){
            this.myParent = myParent;
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();

        }

        private void GeneralForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        
        }

        // TODO: copy into student form
        decimal decTaxRate = 0.06m; // sales tax
        private decimal CalcTax(decimal cost){
            // returns the sales tax on ticket sales
            return cost * decTaxRate;
        }
    }
}
