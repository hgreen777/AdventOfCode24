// Day 1 -> Advent of Code 2024.

// Program [part one] Returns: 1320851
// 7000 operations (2(1000log1000) + 1000) -> O(2(nlogn) + n)
// Heap Sort then linear traverse.

// Program [part two] Returns: 26859182
// 2(nlog2(n)) -> 20000 operations for given input
// 2 linear traversals with binary search for each iteration.

use std::fs::File;
use std::io::{self, BufRead, BufReader};

const FILE: &str = r"E:\Programming\AdventOfCode24\day1\src\input.txt";
const ARR_ELEMENTS : usize = 1000;


fn main() {
    fn partOne() {
        let mut total : u32 = 0;
        let mut arr1: [u32; ARR_ELEMENTS] = [0; ARR_ELEMENTS];
        let mut arr2: [u32; ARR_ELEMENTS] = [0; ARR_ELEMENTS];

        // Read Data from file
        if let Err(e) = loadData(FILE, &mut arr1, &mut arr2) {
            eprintln!("Error loading data: {}", e);
        }

        // Sort the data
        heapSort(&mut arr1);
        heapSort(&mut arr2);
        //println!("{:?}",arr2);

        // Compute the difference
        for i in 0..ARR_ELEMENTS {
            computeDifference(&mut total,&mut arr1[i],&mut arr2[i]);
        }

        println!("{}", total);
    }

    fn partTwo() {
        let mut arr1: [u32; ARR_ELEMENTS] = [0; ARR_ELEMENTS];
        let mut arr2: [u32; ARR_ELEMENTS] = [0; ARR_ELEMENTS];
        loadData(FILE, &mut arr1, &mut arr2);
        heapSort(&mut arr2);

        // Generate unique 
        let mut unique: Vec<[u32; 2]> = Vec::new();

        for i in 0..ARR_ELEMENTS {
            if binarySearch(&mut unique, arr2[i]) == -1 {
                // add to unique
                unique.push([arr2[i], 1]);
            } else {
                // Add 1 to the count in unique
                for entry in unique.iter_mut() {
                    if entry[0] == arr2[i] {
                        entry[1] += 1;
                        break;
                    }
                }
            }
        }

        //println!("{:?}",unique);
        //println!("{}",unique.len());

        // Traverse array 1 adding each similarity score to the total
        let mut total = 0;

        for i in 0..ARR_ELEMENTS {
            let result = binarySearch(&mut unique, arr1[i]);
            if result != -1 {
                let result = result as usize;
                total += unique[result][0] * unique[result][1];
            }
        }

        println!("{}",total);
    }

    partTwo()
}



fn loadData(fileLocation: &str, 
            arr1 : &mut [u32; ARR_ELEMENTS], 
            arr2 : &mut [u32; ARR_ELEMENTS]) -> io::Result<()> {

    let file = File::open(fileLocation)?;
    let reader = BufReader::new(file);

    for (i, line) in reader.lines().enumerate() {
        match line {
            Ok(content) => {
                if i < ARR_ELEMENTS {
                    // get first 5 characters from content and convert to u32
                    arr1[i] = content[0..5].trim().parse::<u32>().unwrap_or(0);
                    arr2[i] = content[8..13].trim().parse::<u32>().unwrap_or(0);
                }
            },
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }
    Ok(())
}

fn heapSort(arr : &mut [u32; ARR_ELEMENTS]) {
    let n = arr.len();

    for i in (0..n / 2).rev() {
        heapify(arr, n, i);
    }

    for i in (0..n).rev() {
        arr.swap(0, i);
        heapify(arr, i, 0);
    }

    fn heapify(arr : &mut [u32; ARR_ELEMENTS], n : usize, i : usize) {
        let mut max = i;

        let left = 2 * i + 1;
        let right = 2 * i + 2;

        if left < n && arr[max] < arr[left] {
            max = left;
        }

        if right < n && arr[max] < arr[right] {
            max = right;
        }

        if max != i {
            arr.swap(i, max);
            heapify(arr, n, max);
        }
    }
}

fn computeDifference(total : &mut u32, 
    num1 : &u32, 
    num2 : &u32) {
    
    let diff : i32 = (*num1 as i32) - (*num2 as i32);

    if diff < 0 {
        *total += ((diff * -1) as u32);
    } else {
        *total += (diff as u32);
    }

}

fn binarySearch(arr : &mut Vec<[u32; 2]>, x : u32) -> i16{
    if arr.is_empty() {
        println!("Array Empty.");
        return -1;
    }

    let mut lower: isize = 0;
    let mut upper: isize = (arr.len() - 1) as isize;

    while lower <= upper {
        let mid = (lower + upper) / 2;
        if arr[mid as usize][0] == x {
            return mid as i16;
        } else if arr[mid as usize][0] > x {
            upper = mid - 1;
        } else {
            lower = mid + 1;
        }
    }
    return -1;
}


