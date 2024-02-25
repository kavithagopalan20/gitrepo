package arraylistconcept;
import java.util.*;
//import java.util.concurrent.CopyOnWriteArrayList;

public class ArrayListdemo {

	public static void main(String[] args) {

		ArrayList<Integer> al = new ArrayList<Integer>();
	
		al.add(10);
		al.add(90);
		al.add(23);
		Iterator<Integer> i= al.iterator();
		while(i.hasNext())
		{
			
			System.out.println("the element is "+i.next());
		}


    		
	}

}
