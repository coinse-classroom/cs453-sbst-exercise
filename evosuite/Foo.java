import java.util.*;

public class Foo
{
	public void testMe(int x, int y, String z)
	{
		if(x == 42)
		{
			System.out.println("hey, it's 42!");
		}
		else
		{
				if(z.length() > 3 && z.startsWith("hello!"))
					System.out.println("z is longer than 3 characters.");
				else
					System.out.println("z is 3 characters or fewer.");
		}
	}
}