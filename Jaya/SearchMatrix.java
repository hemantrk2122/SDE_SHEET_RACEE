/* *****************************************************************************
 *  Name:              Jaya Mukherjee
 *  Last modified:     JAN 12, 2022
 **************************************************************************** */

import java.util.Scanner;

public class SearchMatrix {

    public static boolean search(int[][] matrix, int target) {
        int row = 0, col = matrix[0].length - 1;
        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] == target) {
                return true;
            }
            if (target > matrix[row][col]) {
                row++;
            } else {
                col--;
            }
        }
        return false;
    }

    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int m = scn.nextInt();
        int[][] arr = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = scn.nextInt();
            }
        }
        int target = scn.nextInt();
        System.out.println(search(arr, target));
    }
}
