public class Foo{

	private int x = 0;
	
	public Foo(int x){
		this.x = x;
	}

	public int testMe(int a, int b) throws Exception
	{
		if (a > 0){
			if(a - b < 50){
				throw new Exception("Hey!");
			}
		}
		return a + b;
	}
}