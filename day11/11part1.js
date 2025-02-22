// Day 11
// Part 1 : 200446
// Analyse time constant then improve efficiency, make a readfrom file function
// O(8*2^25)

const test_arr = [125,17];

//814 1183689 0 1 766231 4091 93836 46
const real_arr = [814,1183689,0,1,766231,4091,93836,46];

// O(25*n^2 * 6) -> O(25*8^2)
function nextStone(stone_num, blinks_left, stone_counter, calculated_values) {
    // O(6) -> O(1)
    // How to make more efficient, maybe cache for some results
    if (blinks_left > 0) {
        if (stone_num == 0) {
            stone_counter = nextStone(1,blinks_left - 1, stone_counter)
        } else if (stone_num.toString().length % 2 == 0) { // Even
            let split = stone_num.toString().length / 2
            stone_counter = nextStone(parseInt(stone_num.toString().substring(0,split)),blinks_left - 1, stone_counter)
            stone_counter = nextStone(parseInt(stone_num.toString().substring(split)),blinks_left - 1, stone_counter)
        } else {
            stone_counter = nextStone(stone_num * 2024, blinks_left -1, stone_counter)
        }

    } else {
        return stone_counter + 1;
    }
    return stone_counter;
}

function new_nextStone(stone_num, blinks_left, stone_counter, calculated_values = {}) {
    let key = `${stone_num},${blinks_left}`;
    if (key in calculated_values) {
        return stone_counter + calculated_values[key]; // Use cached value
    }

    if (blinks_left > 0) {
        if (stone_num === 0) {
            stone_counter = new_nextStone(1, blinks_left - 1, stone_counter, calculated_values);
        } else if (stone_num.toString().length % 2 === 0) { // Even length
            let numStr = stone_num.toString();
            let split = numStr.length / 2;
            let leftPart = parseInt(numStr.substring(0, split));
            let rightPart = parseInt(numStr.substring(split));
            
            stone_counter = new_nextStone(leftPart, blinks_left - 1, stone_counter, calculated_values);
            stone_counter = new_nextStone(rightPart, blinks_left - 1, stone_counter, calculated_values);
        } else {
            stone_counter = new_nextStone(stone_num * 2024, blinks_left - 1, stone_counter, calculated_values);
        }
    } else {
        calculated_values[key] = 1; // Cache base case result
        return stone_counter + 1;
    }

    calculated_values[key] = stone_counter - (calculated_values[key] || 0); // Store result
    return stone_counter;
}

function calculateTotalStone(array, blinks) {
    let total = 0;

    calculated_values = new Array(blinks)
    for (stone of array) {
        total += nextStone(stone, blinks, 0,calculated_values);
    }
    //total += nextStone(0, blinks, 0,calculated_values); :663251546 ~110s
    

    return total;
}

function part1() {
try{
const start = performance.now();

document.getElementById("part1").innerHTML = `Part 1: ${calculateTotalStone(real_arr,25)}`

const end = performance.now();
console.log(`Execution Time: ${(end - start) / 1000} seconds`);

} catch (error) {
    document.getElementById("part1").innerHTML = error;
}
}

function part2() {
try{
const start = performance.now();
console.log("Started processing part 2.")
document.getElementById("part2").innerHTML = `Part 2: ${calculateTotalStone(real_arr,50)}`

const end = performance.now();
console.log(`Execution Time: ${(end - start) / 1000} seconds`);

} catch (error) {
    document.getElementById("part2").innerHTML = error;
}
}