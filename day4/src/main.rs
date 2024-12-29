// Day 4 -> Advent of Code 2024.

// Program [part one] Returns:
// Program [part two] Returns: 

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
    let total : u32 = compute_wordsearch(matrix);

    println!("Part 1: {}", total);

    eprintln!("{:.2?}", start.elapsed());
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

fn compute_wordsearch(matrix : Vec<Vec<char>>) -> u32 {
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
        substring.push(matrix[i][j]);
        dynamic_i = (dynamic_i as i32 + direction.1 as i32) as usize; //y
        dynamic_j = (dynamic_j as i32 + direction.0 as i32) as usize;
        
        while (0 <= dynamic_i && dynamic_i < n) && (0 <= dynamic_j && dynamic_j < m) && ("XMAS".starts_with(&substring)) {
            substring.push(matrix[dynamic_i][dynamic_j]);
            
            if substring == "XMAS" {
                *total += 1
            }

            dynamic_i = (dynamic_i as i32 + direction.1 as i32) as usize; //y
            dynamic_j = (dynamic_j as i32 + direction.0 as i32) as usize;
        }
    }
    
    return total
}

// compute same looking for mas with restict direction domain