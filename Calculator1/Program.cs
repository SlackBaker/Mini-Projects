using System;
using System.Security.Cryptography.X509Certificates;

namespace calculator
{
    class Program
    {
        
        static void Main(String[] args) 
        {
            int Plus(int x, int y)
            {
                return x + y;
            }

            double Minus(double x, double y)
            {
                return x - y;
            }

            int Substract(int x, int y)
            {
                return x * y;
            }

            double Division(int x, int y)
            {
                return x / y;
            }
            Console.WriteLine("Choose +,-,*, or :");
            string text = Console.ReadLine();
            Console.WriteLine("Write first number:");
            int x1 = int.Parse(Console.ReadLine());
            Console.WriteLine("Write second number:");
            int y1 = int.Parse(Console.ReadLine());
            double counter = 0;
            if (text == "+")
            {
                counter = Plus(x1, y1);
                Console.WriteLine($"Your result: {counter}");

            }
            if (text == "-")
            {
                counter = Minus(x1, y1);
                Console.WriteLine($"Your result: {counter}");
            }
            if (text == "*")
            {
                counter = Substract(x1, y1);
                Console.WriteLine($"Your result: {counter}");
            }
            if(text == ":")
            {
                counter = Division(x1, y1);
                Console.WriteLine($"Your result: {counter}");
            }
            else
            {
                Console.WriteLine("Wrong");
            }
            Console.WriteLine("v. 1.0.0.");

            Console.WriteLine("Task 2");

            /*int[] Summ(int value, int[] num1)
            {
                for(int i =0; i < num1.Length; i++)
                {
                    num1[i] += value;
                }
                return num1;
            }*/
            int[] input(int[] massive)
            {
                Console.WriteLine("Enter massive size: ");
                int massiveSize = int.Parse(Console.ReadLine());
                massive = new int[massiveSize];
                for (int i = 0; i < massiveSize; i++)
                {
                    Console.WriteLine($"Enter {i} element: ");
                    int element = int.Parse(Console.ReadLine());
                    massive[i] = element;
                }
                return massive;
            }
            int[] mas = new int[] {};
            int[] massive = new int[] { };
            input(mas);
            input(massive);
            void method(int[] s)
            {
                foreach (var m in s)
                {
                    Console.WriteLine($"{m}");
                }
            }
            method(mas);
            method(massive);
        }
    }
}