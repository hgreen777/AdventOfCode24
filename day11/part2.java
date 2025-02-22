//package AdventOfCode24.day11;


public class part2 {
    
    int[] real_arr = new int[]{814,1183689,0,1,766231,4091,93836,46};

    public static int nextStone(int stone_num, int blinks_left, int stone_counter) {
        if (blinks_left > 0) {
            if (stone_num == 0) {
                stone_counter = nextStone(1,blinks_left - 1, stone_counter);
                
            } else if (stone_num > 0 && String.valueOf(stone_num).length() % 2 == 0) {
                int split = String.valueOf(stone_num).length() / 2;
                stone_counter = nextStone(Integer.parseInt(String.valueOf(stone_num).substring(0,split)),blinks_left - 1, stone_counter);
                stone_counter = nextStone(Integer.parseInt(String.valueOf(stone_num).substring(split)),blinks_left - 1, stone_counter);
            } else {
                stone_counter = nextStone(stone_num * 2024, 
                blinks_left -1, stone_counter);
            }
        } else {
            return stone_counter + 1;
        }
        return stone_counter;
    }

    public static void main(String[] args) {
        int total = 0;
        int[] array = {814, 1183689, 0, 1, 766231, 4091, 93836, 46};
        for (int stone : array) {
            total += nextStone(stone, 25, 0);
        }  System.out.println(total);
    }
}