// Day 4 -> Advent of Code 2024.

// Program [part one] Returns: 2424
// Program [part two] Returns: 1873

// in future if handling matrix like things use x,y > i,j
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::time::Instant;
const FILE: &str = r"E:\Programming\AdventOfCode24\day4\src\input.txt";

fn main() {
    let start = Instant::now();
    let mut matrix : Vec<Vec<char>> = Vec::with_capacity(140);

    // Handle Input
    eprintln!("{:?}",handle_input(FILE, &mut matrix));
    //println!("{:?}", matrix);

    // Calculate Total XMASes
    let total : u32 = compute_wordsearch(&matrix);

    println!("Part 1: {}", total);


    let total : u32 = part2_compute_wordsearch(&matrix);
    println!("Part 2: {}", total);

    eprintln!("{:.2?}", start.elapsed());
    println!("{}", "MAS".starts_with(""));
}

// 140 x 140 matrix
fn handle_input(file_location: &str, matrix : &mut Vec<Vec<char>>) -> io::Result<()> {

    let file: File = File::open(file_location)?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        match line {
            Ok(content) => {
                let mut row: [char; 140] = [' '; 140];
                for (i, c) in content.chars().enumerate() {
                    if i < 140 {
                        row[i] = c;
                    }
                }
                matrix.push(row.to_vec());
                
            },
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    Ok(())
}

fn compute_wordsearch(matrix : &Vec<Vec<char>>) -> u32 {
    let mut total : u32 = 0;
    let row_length : usize = matrix[0].len();
    let direction : Vec<(i8,i8)> = vec!(
        (0,1),  (1,1),  
        (1,0),  (1,-1), 
        (0,-1), (-1,-1),
        (-1,0), (-1,1)
    );

    // solve
    {

        for i in 0..matrix.len() {
            for j in 0..row_length {
                if matrix[i][j] == 'X' {
                    for k in 0..direction.len() {
                        check(&matrix, i,j,direction[k], &mut total);
                    }
                }
            }
        }
    };

    fn check(matrix : &Vec<Vec<char>>, i: usize, j:usize, direction: (i8, i8), total : &mut u32) {
        let n = matrix.len();
        let m = matrix[0].len();
        let mut dynamic_i = i;
        let mut dynamic_j = j;

        let mut substring = String::new();

        
        while (dynamic_i < n) && (dynamic_j < m) && ("XMAS".starts_with(&substring)) {
            substring.push(matrix[dynamic_i][dynamic_j]);
            
            if substring == "XMAS" {
                *total += 1
            }

            // will overflow if negative and that is bigger then n & m therefore no need for 0 check
            dynamic_i = (dynamic_i as i32 + direction.1 as i32) as usize; //y
            dynamic_j = (dynamic_j as i32 + direction.0 as i32) as usize;
        }
    }
    
    return total
}

// only finds diagonal, not Xs
// restrict to only check down, if a sam or mas is found vertically right down, skip 2 places and see if that is found in the opposite vertical
// could improve by limiting the amount of nesting and iterations for sam & mas
fn part2_compute_wordsearch(matrix : &Vec<Vec<char>>) -> u32 {
    let mut total : u32 = 0;
    let row_length : usize = matrix[0].len();
    let search_words: [&str;2] = ["SAM", "MAS"];
    //
    let direction : Vec<(i8,i8)> = vec!(
      //(y,x),
        (1,1),  
        (1,-1)
    );

    // solve
    {

        for i in 0..matrix.len() {
            for j in 0..row_length {
                if matrix[i][j] == 'M' || matrix[i][j] == 'S' {
                    for k in 0..search_words.len() {
                        if check(&matrix, i, j, direction[0], search_words[k]) {
                            // Check that work in 2 positions forward 
                            for a in 0..search_words.len() {
                                if check(&matrix, i, j + 2, direction[1], search_words[a]) {
                                    total += 1;

                                    /*
                                    // Printing The successful boxes.
                                    println!("i: {}, j: {}", i, j);
                                    for x in i..=(i + 2).min(matrix.len() - 1) {
                                        for y in j..=(j + 2).min(matrix[0].len() - 1) {
                                            print!("{}", matrix[x][y]);
                                        }
                                        println!();
                                    }
                                    */

                                }
                            }
                        }
                    }
                }
            }
        }
    };

    fn check(matrix : &Vec<Vec<char>>, i: usize, j:usize, direction: (i8, i8), search_word : &str) -> bool{
        let n = matrix.len();
        let m = matrix[0].len();
        let mut dynamic_i = i;
        let mut dynamic_j = j;

        let mut substring = String::new();
        
        while (dynamic_i < n) && (dynamic_j < m) && (search_word.starts_with(&substring)) {
            substring.push(matrix[dynamic_i][dynamic_j]);
            
            if substring == search_word {
                return true;
            }

            dynamic_i = (dynamic_i as i32 + direction.0 as i32) as usize; //y
            dynamic_j = (dynamic_j as i32 + direction.1 as i32) as usize;


        }
        return false;
    }
    
    return total
}