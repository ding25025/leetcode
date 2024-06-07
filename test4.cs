
class Program
{
    static void Main(string[] args)
    {
        var t = new Test1();
    }

}

public class TestBase
{
    public TestBase()
    {
        Console.Write("1");
    }
    public TestBase(string text)
    {
        Console.Write("2");
        Console.Write(text);
    }
}
public class Test1
{
    public Test1() : this("3")
    {
        Console.Write("4");
    }
    public Test1(string text) : base(text + "5")
    {
        Console.Write("6");
        Console.Write(text);
    }
}