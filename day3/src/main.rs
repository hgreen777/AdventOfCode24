// Day 3 -> Advent of Code 2024.

// Program [part one] Returns: 181345830
// Program [part two] Return: 98729041

use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::time::Instant;
use regex::Regex;
const FILE: &str = r"E:\Programming\AdventOfCode24\day3\src\input.txt";

fn main() {
    let start = Instant::now();
    println!("Hello, world!");
    let mut total_p1 : u32 = 0;

    eprintln!("{:?}",load_data(FILE, &mut total_p1));
    println!("{}",total_p1);
    eprintln!("{:.2?}", start.elapsed());
}

fn load_data(file_location: &str, total : &mut u32) -> io::Result<()> {

    let file: File = File::open(file_location)?;
    let reader = BufReader::new(file);
    let mull_pattern: Regex = Regex::new(r"mul\([0-9]{1,3},[0-9]{1,3}\)").unwrap();
    let num_pattern: Regex = Regex::new(r"([0-9]{1,3})").unwrap();
    let do_pattern: Regex = Regex::new(r"do\(\)").unwrap();
    let dont_pattern: Regex =  Regex::new(r"don't\(\)").unwrap();

    let mut collecting : bool = true;

    for line in reader.lines() {
        match line {
            Ok(content) => {

                for (i, char) in content.chars().enumerate() {
                    if char == 'd' {
                        let substring : &str;
                        if i+7 < content.len() {
                            substring = &content[i..i+7];
                        } else {
                            substring = &content[i..content.len()];
                        }
                        
                        println!("{:?}",substring);
                        if do_pattern.is_match(substring) {
                            collecting = true;
                        } else if dont_pattern.is_match(substring) {
                            collecting = false;
                        }
                        continue;
                    }

                    if collecting && char == 'm' {
                        
                        // abstract the next x characters
                        let substring : &str;
                        if i+ 12 < content.len() {
                            substring = &content[i..i+12];
                        } else {
                            substring = &content[i..content.len()];
                        }

                        // compare with pattern
                        if mull_pattern.is_match(&substring) {
                            let nums: Vec<u32> = num_pattern.captures_iter(&substring)
                                .filter_map(|cap| cap[0].parse::<u32>().ok())
                                .collect();

                            calculate_mul(nums[0], nums[1], total);
                        }


                    }
                }
                
                
                
            },
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    Ok(())
}

fn calculate_mul(x : u32, y : u32, total : &mut u32) {
    *total += x * y;
}