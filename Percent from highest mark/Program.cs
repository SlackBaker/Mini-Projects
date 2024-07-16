namespace MarkPercent
{
    class Program
    {
        string mark;
        int mark2;
        static int maxmark = 12; //12 because this is maximal mark in Ukraine.

        void CalculatePercent()
        {
            int calculate = this.mark2 * 100 / Program.maxmark;
            Console.WriteLine(calculate + "%");
        }

        
        static void Main(string[] args)
        {
            Program pr = new Program();
            Console.WriteLine("Write mark which you have got to convert it into the percents from highest mark");
            pr.mark = Console.ReadLine();
            pr.mark2 = Convert.ToInt32(pr.mark);
            pr.CalculatePercent();
        }
    }

}
