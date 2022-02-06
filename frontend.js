//1.Intersection of unsorted arrays
function getIntersection(arr1, arr2) {
  setter = new Set(arr1);
  for (const n of arr2) {
    if (!setter.has(n)) {
      setter.delete(n);
    }
  }
  return [...setter];
}
console.log(
  getIntersection(
    [1, 100, 200, 8, 8, 8, 3, 6, 100, 10, 10],
    [8, 7, 7, 50, 50, 1, 1, 1, 1, 3, 3]
  )
);
