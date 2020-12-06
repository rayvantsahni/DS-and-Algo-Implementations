public class Main
{
    static int n;

    public static void getMazePaths(int[][] maze, int[][] solutionMaze, int x, int y) {
        if ((x == n - 1) && (y == n - 1)) {
            solutionMaze[x][y] = 1;
            displayPath(solutionMaze);
            return;
        }

        if (!furtherStepPossible(maze, solutionMaze, x, y))
            return;

        solutionMaze[x][y] = 1;
        getMazePaths(maze, solutionMaze, x - 1, y);
        getMazePaths(maze, solutionMaze, x + 1, y);
        getMazePaths(maze, solutionMaze, x, y - 1);
        getMazePaths(maze, solutionMaze, x, y + 1);
        solutionMaze[x][y] = 0;

    }


    private static boolean furtherStepPossible(int[][] maze, int[][] solutionMaze, int x, int y) {
        return !((x < 0) || (y < 0) || (x >= n) || (y >= n) || (maze[x][y] == 0) || (solutionMaze[x][y] == 1));
    }


    private static void displayPath(int[][] solutionMaze) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (solutionMaze[i][j] == 1)
                    System.out.print("x ");
                else {
                    System.out.print("- ");
                }
            }
            System.out.println();
        }
        System.out.println();
    }


    public static void main(String[] args) {

        int[][] maze = {{1,0,0},
                        {1,1,0},
                        {1,1,1}};
        n = maze.length;

        int[][] solutionMaze = new int[n][n];

        getMazePaths(maze, solutionMaze, 0, 0);
    }
}
