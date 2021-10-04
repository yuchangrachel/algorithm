//when collision, positive going to right, negative going to left
var asteroidCollision = function (asteroids) {
  if (asteroids == null || asteroids.length == 0) return [];

  //create stack, if positive store into stack, when see negative, check top of stack
  const stack = [];
  for (let i = 0; i < asteroids.length; i++) {
    let char = asteroids[i];
    if (char > 0) stack.push(char);
    //store all positive
    else {
      while (
        stack.length > 0 &&
        stack[stack.length - 1] > 0 &&
        Math.abs(char) > stack[stack.length - 1]
      ) {
        //while loop handle stack eg.-2,-3,1,2
        stack.pop();
      }
      if (!stack.length || stack[stack.length - 1] < 0) {
        //2,2,-5 OR -2,-3,1,2
        stack.push(char);
      } else if (Math.abs(char) == stack[stack.length - 1]) {
        //collide both
        stack.pop();
      }
    }
  }
  return stack;
};
console.log(asteroidCollision([10, 2, -5]));
