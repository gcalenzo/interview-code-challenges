public class CodeChallenge{

    public static void main(String []args){
    
	int[] arr = {10, 15, 3, 7}; 
        
	if (function(arr, 22)) {
            System.out.println("True - The value can be obtained as a combination of two numbers of the array");
        } else {
            System.out.println("False - The value cannot be obtained as a combination of two numbers of the array");
        }
     }
     
    private static boolean function(int [] arr, int k) {
        for (int x : arr) {
            if ( arr.indexOf(k - x) > -1) {
                return true;
            }
        }
        return false;
    }
}
