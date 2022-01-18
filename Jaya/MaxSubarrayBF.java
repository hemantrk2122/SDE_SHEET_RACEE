/* *****************************************************************************
 *  Name:              Jaya Mukherjee
 *  Last modified:     JAN 17, 2022
 **************************************************************************** */

import java.util.Scanner;

public class MaxSubarrayBF {
    public static int maxSum(int[] arr) {
        int maxSubSum = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++) {
            int currentSum = 0;
            for (int j = i; j < arr.length; j++) {
                currentSum += arr[j];
                maxSubSum = Math.max(maxSubSum, currentSum);
            }
        }

        return maxSubSum;
    }

    public static int maxSumDP(int[] arr) {
        
    }

    public static void display(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scn.nextInt();
        }

        System.out.println(maxSumDP(a));

    }
}
