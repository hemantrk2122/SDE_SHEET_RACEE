/* *****************************************************************************
 *  Name:              Jaya Mukherjee
 *  Last modified:     JAN 13, 2022
 **************************************************************************** */

import java.util.Scanner;

public class RotateMatrix {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[][] arr = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = scn.nextInt();
            }
        }
        int[][] matrix = Transpose(arr);
        int[][] matrix2 = Reverse(matrix);
        display(matrix2);

    }

    public static int[][] Reverse(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            int si = 0;
            int ei = matrix[i].length - 1;
            while (si < ei) {
                int temp = matrix[i][si];
                matrix[i][si] = matrix[i][ei];
                matrix[i][ei] = temp;

                si++;
                ei--;
            }
        }
        return matrix;
    }

    public static int[][] Transpose(int[][] matrix) {

        for (int i = 0; i < matrix.length; i++) {
            for (int j = i; j < matrix[0].length; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        return matrix;
    }

    public static void display(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {

                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

}
