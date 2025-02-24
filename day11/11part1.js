// Day 11
// Part 1 : 200446
// Analyse time constant then improve efficiency, make a readfrom file function
// O(8*2^25)

const test_arr = [125,17];

//814 1183689 0 1 766231 4091 93836 46
const real_arr = [814,1183689,0,1,766231,4091,93836,46];

function nextStone(stone_num, blinks_left, stone_counter, calculated_values) {
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

function calculateTotalStone(array, blinks) {
    let total = 0;

    calculated_values = new Array(blinks)
    for (stone of array) {
        total += nextStone(stone, blinks, 0,calculated_values);
        // Next stone change to calculating full stone should instead call a different function upon recursion and this call as well, this will check the cache for the given data first before ecalculating it again -> ensure numbers can b
    }
    //total += nextStone(0, blinks, 0,calculated_values); :663251546 ~110s
    

    return total;
}

function part1_11() {
try{
const start = performance.now();

document.getElementById("11part1").innerHTML = `Part 1: ${calculateTotalStone(real_arr,25)}`

const end = performance.now();
console.log(`Execution Time: ${(end - start) / 1000} seconds`);

} catch (error) {
    document.getElementById("11part1").innerHTML = error;
}
}