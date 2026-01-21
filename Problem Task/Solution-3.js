// Problem 3: Palindrome Check


function isPalindrome(str) {
  let reverse = "";

  for (let i = str.length - 1; i >= 0; i--) {
    reverse = reverse + str[i];
  }

  if (str === reverse) {
    return true;
  } else {
    return false;
  }
}

console.log(isPalindrome("madam"));
console.log(isPalindrome("hello"));
