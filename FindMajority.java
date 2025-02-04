import java.util.HashMap;
import java.util.Map;


public class FindMajority{
    public static void main(String[] args) {


        int a[] = {10, 10, 10, 10, 2, 3, 4};

        // initialize the object
        // FindMajority obj = new FindMajority();

        // call the solve method
        // int ans = obj.solve(a);

        // System.out.println(ans);



        int ans = solve(a);
        System.out.println("The majority element is "+ans);
        
    }

    public static int solve(int a[]){
        Map<Integer, Integer> map = new HashMap<>();

        for(int ele: a){
            map.put(ele, map.getOrDefault(ele, 0)   +  1);
        }

        for(Map.Entry<Integer,Integer> e: map.entrySet()){
            if(e.getValue() > a.length/2){
                return e.getKey();
            }
        }
        return -1;
    }
}


