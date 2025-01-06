// Day 5 -> Advent of Code 2024.

// Program [part one] Returns: 
// Program [part two] Returns: 

use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::time::Instant;

const FILE: &str = r"E:\Programming\AdventOfCode24\day5\src\input.txt";

fn main() {
    let start = Instant::now();
    let mut rules : Vec<(u16,u16)> = Vec::new();
    let mut page_orders : Vec<Vec<u16>> = Vec::with_capacity(300);
    let mut correct_order_indexes : Vec<u16> = Vec::new();
    let mut total_p1 : u32 = 0;

    // Handle Input
    eprintln!("{:?}",handle_input(FILE, &mut rules, &mut page_orders));
    //println!("{:?}", matrix);

    // Calculate Total XMASes
    find_correct_page_orders(&mut rules, &mut page_orders, &mut Vec<u16>);
    println!("{:?}", correct_order_indexes)

    let total_p1 : u32 = calculate_p1_total(
        page_orders : &mut Vec<Vec<u16>>, 
        correct_order_indexes : &mut Vec<u16>
    );

    println!("Part 1: {}", total_p1);

    /*
    let total : u32 = part2_compute_wordsearch(&matrix);
    println!("Part 2: {}", total);
    */

    eprintln!("{:.2?}", start.elapsed());
}

fn handle_input(
    file_location: &str, r
    rules : &mut Vec<(u16,u16)>, 
    page_orders : &mut Vec<Vec<u16>>) -> io::Result<()>  {
    
    let file: File = File::open(file_location)?;
    let reader = BufReader::new(file);

    let mut is_section_one : bool = ture;

    for (i, line) in reader.lines().enumerate() {
        match line {
            Ok(content) => {

                if is_section_one {
                    if line == "" {
                        is_section_one = false
                        continue;
                    }

                    continue;
                }


                let mut page_row : Vec<u16> = Vec::new();
                // handle row as whole and read into vec and produce arr of nums 

                page_orders.push(page_row);
                
            },
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    Ok(())
    
    }

fn find_correct_page_orders(
    rules : &mut Vec<(u16,u16)>, 
    page_orders : &mut Vec<Vec<u16>>, 
    correct_order_indexes : &mut Vec<u16>) {

        // Sort rules by first one

        // for each page order:
            // for each page:
                // search for all rules 

                // for each rule, check if the second page exists before the current number (stop at the number as after is fine)
                    // if it does, stop processing, its wrong
                    // if it isn't add the current page_order index to correct_order_index


}

fn calculate_p1_total(
    page_orders : &mut Vec<Vec<u16>>, 
    correct_order_indexes : &mut Vec<u16>) -> u32 {
        // for each correct order index
            // find the page_orders (direct access)
            // find middle value
            // add to total
    }