// Day 2 -> Advent of Code 2024.

// Program [part one] Returns: 356
// Program [part two] Return: 413

use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::time::Instant;

const FILE: &str = r"E:\Programming\AdventOfCode24\day2\src\input.txt";

fn main() {
    let start = Instant::now();
    let mut total : u32 = 0;
    println!("{:?}",load_data(FILE,&mut total));
    println!("{}",total);
    eprintln!("{:.2?}", start.elapsed());
}

fn load_data(file_location: &str, total_safe : &mut u32) -> io::Result<()> {

    let file = File::open(file_location)?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        match line {
            Ok(content) => {
                let mut num: String = String::new();
                let mut arr : Vec<u32> = Vec::new();

                for char in content.chars() {
                    if char == ' ' {
                        // Add num to array
                        arr.push(num.parse::<u32>().unwrap_or(0));
                        num.clear();
                    } else {
                        num = num.to_string() + &char.to_string();
                    }
                    //println!("{}",num)
                }
                arr.push(num.parse::<u32>().unwrap_or(0));
                //println!("{:?}",arr);
                // Compute if safe 
                if arr.len() <= 4 {
                    println!("{:?}", arr);
                }
                if is_safe(&arr) {
                    *total_safe += 1;
                }
                
            },
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    Ok(())
}

fn is_safe(arr: &[u32]) -> bool {
    let mut is_increasing: bool = arr[1] as i16 - arr[0] as i16 > 0;
    let mut ignore_index : i16 = -1;
    let mut i : usize = 0;
    let mut safe : bool;
    let mut diff : i32;

    while i < arr.len() - 1 {
        if ignore_index != -1 {
            if i == ignore_index as usize {
                i += 1;
                continue;
            }
        }

        if is_increasing {
            diff = arr[i + 1] as i32 - arr[i] as i32;
            
        } else {
            diff = arr[i] as i32 - arr[i + 1] as i32;
        }
        safe = 1 <= diff && diff <= 3;

        if !safe {
            if ignore_index != -1 {
                return false
            } else {
                ignore_index = i as i16;

                if i == 0 {
                    is_increasing = arr[2] as i16 - arr[1] as i16 > 0;
                } 
                i = 0;

                continue;
            }

        }

        i += 1
    }

    return true;
}

