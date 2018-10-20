static void Main(string[] args)
        static void Main(string[] args) {
            string line = "4d12";
            int index = line.IndexOf("d");
            Random randomizer = new Random();
            int total = 0;
            string answer = "";

            string dice = Substring(line, 0, index);
            string sides = Substring(line, index + 1, line.Length);
            
            for (int i = 0; i < Int32.Parse(dice); i++) {
                int temp = randomizer.Next(0, Int32.Parse(sides));
                total += (  temp);
                answer += " " + temp;
            }
            answer = total + ":" + answer;
            Console.WriteLine(answer);
            Console.Read();
        }

        static string Substring(string word, int start, int end) {

            string subWord = "";
            for (int i = start; i < end; i++) {
                subWord += word[i];
            }

            return subWord;
        }
		
Answer

{
    Random rnd = new Random();
    Console.Title = "Create a Dice Roller";
    bool exit = false;
    while (!exit)
    {
        Console.Clear();
        Console.CursorVisible = true;
        Console.Write("Enter your input (COUNTdFACES ex: 5d6): ");
        string input = Console.ReadLine().ToLower();
        Console.CursorVisible = false;
        int count = int.Parse(input.Split('d')[0]);
        int faces = int.Parse(input.Split('d')[1]);

        int result = 0;
        string[] results = new string[count];
        int line = Console.CursorTop;
        for (int i = 0; i < count; i++)
        {
            Console.Write($"Rolling die {i + 1}/{count}");
            int curr = rnd.Next(faces) + 1;
            result += curr;
            results[i] = curr.ToString();
            Console.SetCursorPosition(0, line);
        }
        ClearCurrentConsoleLineFromCurrentPos();
        Console.WriteLine($"{result}: {string.Join(" ", results)}");
        Console.Write("Do you want to roll again? (Y/N)");
        ConsoleKeyInfo key = Console.ReadKey(true);
        if (key.KeyChar == 'N' || key.KeyChar == 'n')
            exit = true;
    }
}

public static void ClearCurrentConsoleLineFromCurrentPos()
{
    int currentLineCursor = Console.CursorTop;
    int currentCharCursor = Console.CursorLeft;
    Console.Write(new string(' ', Console.WindowWidth-currentCharCursor));
    Console.SetCursorPosition(currentCharCursor, currentLineCursor);
}

