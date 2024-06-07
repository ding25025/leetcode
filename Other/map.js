//Design a data structure such that it can achieve O(1) on the following operations: 
//insert a key, fetch a key, delete a key and fetch a random key.

class RandomizedSet {
    constructor() {
        this.map = new Map();
        this.array = [];
    }

    // Inserts a value into the set. Returns true if the set did not already contain the specified element.
    insert(val) {
        if (this.map.has(val)) return false;
        this.map.set(val, this.array.length);
        this.array.push(val);
        return true;
    }

    // Removes a value from the set. Returns true if the set contained the specified element.
    delete(val) {
        if (!this.map.has(val)) return false;

        // Get the index of the element to delete
        const index = this.map.get(val);

        // Swap the element with the last element
        const lastElement = this.array[this.array.length - 1];
        this.array[index] = lastElement;
        this.map.set(lastElement, index);

        // Remove the last element
        this.array.pop();
        this.map.delete(val);

        return true;
    }

    // Returns true if the set contains the specified element.
    fetch(val) {
        return this.map.has(val);
    }

    // Get a random element from the set.
    getRandom() {
        const randomIndex = Math.floor(Math.random() * this.array.length);
        return this.array[randomIndex];
    }
}

// Usage example:
const randomSet = new RandomizedSet();
console.log(randomSet.insert(1));  // true
console.log(randomSet.insert(2));  // true
console.log(randomSet.insert(3));  // true
console.log(randomSet.fetch(1));   // true
console.log(randomSet.fetch(4));   // false
console.log(randomSet.delete(2));  // true
console.log(randomSet.getRandom()); // 1 or 3 (random)
console.log(randomSet.getRandom()); // 1 or 3 (random)
