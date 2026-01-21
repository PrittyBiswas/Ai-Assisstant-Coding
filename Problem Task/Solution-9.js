
// Problem 9: Factorial


function factorial(num) {
  let answer = 1;

  for (let i = 1; i <= num; i++) {
    answer = answer * i;
  }

  return answer;
}

console.log(factorial(5));
