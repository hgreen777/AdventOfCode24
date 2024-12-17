// Day 2 -> Advent of Code 2024.

// Program [part one] Returns: 356

use std::fs::File;
use std::io::{self, BufRead, BufReader};

const FILE: &str = r"E:\Programming\AdventOfCode24\day2\src\input.txt";

fn main() {

    let mut total : u32 = 0;
    println!("{:?}",load_data(FILE,&mut total));
    println!("{}",total);
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
                if is_safe(&mut arr) {
                    *total_safe += 1;
                }
                
            },
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    Ok(())
}

fn is_safe(arr : &mut Vec<u32>) -> bool {
    // Need to ensure it stays decreasing or increasing 
    let mut is_increasing:bool = false;
    for i in 0..arr.len() - 1 {
        let diff:i16 = arr[i] as i16 - arr[i+1] as i16;
        if i == 0 {
            if diff < 0 {
                is_increasing = false;
            } else {
                is_increasing = true;
            }
        }

        //print!("{},",diff);
        if diff < 0 {
            if diff < -3 || is_increasing {
                return false; 
            }

        } else {
            if diff > 3 || diff < 1 || !is_increasing{
                return false;
            }
        }
    }
    return true;
}
