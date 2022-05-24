public class Solution {
    public static void main(String args[]) {
        // Test cases
        System.out.println(Solution.solution(0));
        System.out.println(Solution.solution(10000));
        System.out.println(Solution.solution(-1));
        System.out.println(Solution.solution(10001));
    }
    
    public static String solution(int i) {
        // Configuration Parameters
        int SOLUTION_INDEX_RANGE_START = 0;
        int SOLUTION_INDEX_RANGE_END = 10000;
        int PRIME_NUMBER_SEQUENCE_LENGTH = 5;
        int PRIME_NUMBER_STRING_LENGTH = SOLUTION_INDEX_RANGE_END + PRIME_NUMBER_SEQUENCE_LENGTH;
        
        // Function Variables
        String PrimeNumberString = "";
        
        // Initialize the String
        int num = 1;
        boolean  is_prime = true;
        while (PrimeNumberString.length() < PRIME_NUMBER_STRING_LENGTH)
        {
          num += 1;
          is_prime = true;
          // Identify if num is a prime number and append to the list
          for (int j = 2; j < num; j++)
          {
              if ((num % j) == 0)
              {
                  is_prime = false;
                  break;
              }
          }
          if (is_prime == true)
          {
              PrimeNumberString = PrimeNumberString.concat(String.valueOf(num));
          }
        }
        
        // Check for input parameter errors
        if ((i < SOLUTION_INDEX_RANGE_START) || (i > SOLUTION_INDEX_RANGE_END))
        {
            return "";
        }
        
        // Return the selected number sequence
        return PrimeNumberString.substring(i, i + PRIME_NUMBER_SEQUENCE_LENGTH);
    }
}