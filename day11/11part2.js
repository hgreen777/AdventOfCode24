// Day 11
// Part 2 : 238317474993392 

let cache = new Map();

function checkCache(stone, blinks) {
    const key = `${stone}:${blinks}`;
    if (cache.has(key)) {
        return cache.get(key);
    } else {
        const total = p2nextStone(stone, blinks);
        cache.set(key, total);
        return total;
    }
}

function p2nextStone(stone_num, blinks_left) {
    if (blinks_left > 0) {
        if (stone_num === 0) {
            return checkCache(1, blinks_left - 1);
        } else if (stone_num.toString().length % 2 === 0) { // Even
            let split = stone_num.toString().length / 2;
            return checkCache(parseInt(stone_num.toString().substring(0, split)), blinks_left - 1) +
                   checkCache(parseInt(stone_num.toString().substring(split)), blinks_left - 1);
        } else {
            return checkCache(stone_num * 2024, blinks_left - 1);
        }
    } else {
        return 1;
    }
}

function p2calculateTotalStone(array, blinks) {
    let total = 0;
    for (let stone of array) {
        total += checkCache(stone, blinks);
    }
    return total;
}

function part2_11() {
    try {
        const start = performance.now();
        console.log("Started processing part 2.");
        document.getElementById("11part2").innerHTML = `Part 2: ${p2calculateTotalStone(real_arr, 75)}`;
        console.log(cache);
        const end = performance.now();
        console.log(`Execution Time: ${(end - start) / 1000} seconds`);
    } catch (error) {
        document.getElementById("11part2").innerHTML = error;
    }
}
