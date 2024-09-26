using System;

class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            

            Random random = new Random();

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Let's play a game...");
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("You have to guess a number from 1 to 10");

            int randomNumber = random.Next(1, 11);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("Enter your guess: ");
            int output = Convert.ToInt32(Console.ReadLine());

            if (output == randomNumber)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"Yes, the number is {randomNumber}");
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine($"No, the number is {randomNumber}");
            }


            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Do you want to play again? (yes/no)");
            string playAgain = Console.ReadLine().ToLower();

            Console.ResetColor();

            if (playAgain != "yes")
            {
                break;
            }
            if (playAgain == "yes")
            {
                Console.Clear();
            }
        }
    }
}