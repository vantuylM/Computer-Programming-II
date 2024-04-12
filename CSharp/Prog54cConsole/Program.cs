using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prog54cConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Radius: ");
            double radius = double.Parse(Console.ReadLine());
            double area = 3.141 * (radius * radius);
            double circum = 2 * radius * 3.141;
            Console.WriteLine("Area" + area);
            Console.WriteLine("Circumference" + circum);
            Console.ReadKey();

        }
    }
}
