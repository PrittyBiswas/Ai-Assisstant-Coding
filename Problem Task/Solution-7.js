// Problem 7: Find Even Numbers


function findEvenNumbers(arr) {
  let even = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) {
      even.push(arr[i]);
    }
  }

  return even;
}

console.log(findEvenNumbers([1, 2, 3, 4, 5, 6]));

// 2,4,6
