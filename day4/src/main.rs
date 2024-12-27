// Day 4 -> Advent of Code 2024.

// Program [part one] Returns:
// Program [part two] Returns: 

use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::time::Instant;
use regex::Regex;
const FILE: &str = r"E:\Programming\AdventOfCode24\day4\src\input.txt";

fn main() {
    println!("Hello, world!");
    let mut matrix : Vec<Vec<char>> = Vec::with_capacity(140);

    // Handle Input

    // Calculate Total XMASes

}

// 140 x 140 matrix
fn handle_input(file_location: &str, mut matrix : Vec<Vec<char>>) -> io::Result<()> {
    let mut row : Vec<char> = Vec::with_capacity(140);

    let file: File = File::open(file_location)?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        match line {
            Ok(content) => {
                let mut row : Vec<char> = Vec::with_capacity(140);
                for (i, char) in content.chars().enumerate() {
                    
                }
                
                
                
            },
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    Ok(())
}

fn compute_wordsearch() -> u32 {
    return 0
}