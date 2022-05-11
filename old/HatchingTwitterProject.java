import java.io.*;

public class HatchingTwitterProject
{
    final static String[] twitterASCIILogo = 
        {"                              /                    ((((((((((/  .(/,                              ",
        "                             ((((,               ((((((((((((((((. .(                             ",
        "                             /(((((((           ((((((((((((((((((/                               ",
        "                              ((((((((((((,     (((((((((((((((((                                 ",
        "                             .  (((((((((((((((((((((((((((((((((                                 ",
        "                             ,((((((((((((((((((((((((((((((((((*                                 ",
        "                               (((((((((((((((((((((((((((((((((                                  ",
        "                                 /(((((((((((((((((((((((((((((                                   ",
        "                                 (((((((((((((((((((((((((((((                                    ",
        "                                  ,((((((((((((((((((((((((/                                      ",
        "                                        ((((((((((((((((((                                        ",
        "                                   ,((((((((((((((((((/.                                          ",
        "                              //(((((((((((((((((((,                                              "};

    public static void main(String[] args)
    {
        printSplashScreen();
    }

    public static void printSplashScreen()
    {
        for (String s : twitterASCIILogo)
        {
            delay(100);
            System.out.println(s);
        }
    }

    public static void printMenu()
    {
        String[] options = {"1) Book Reflection", "2) Characters", "3) Timeline", "4) "};


    }

    // Common Functions
    public static void clearScreen()
    {

    }
    public static void delay(int milliseconds)
    {
        try
        {
            Thread.sleep(milliseconds);
        }
        catch (InterruptedException e)
        {
            System.err.println("Thread Sleep Error");
        }
        catch (IllegalArgumentException e)
        {
            System.err.println("Invalid delay time");
        }
    }
    public static String getInput()
    {
        return System.console().readLine();
    }
    public static String getInput(String msg)
    {
        System.out.print(msg + " ");
        String input = System.console().readLine();
        System.out.println();
        return input;
    }
}