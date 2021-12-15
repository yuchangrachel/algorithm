var student = {
  name: "David Rayy",
  sclass: "VI",
  rollno: 12,
};
//1.List propertie of object
const showStudent = function (obj) {
  const res = [];
  for (let k in obj) {
    res.push(k);
  }
  return res;
};
// console.log(showStudent(student));
//2,delete one property of object
const deleteStudent = function (obj) {
  delete obj.rollno;
  return obj;
};
// console.log(deleteStudent(student));
//3.get length of obj
const getLenStudent = function (obj) {
  //1WAY Use class Method:keys(obj)
  //return Object.keys(obj).length;
  //2WAY Use instance Method: hasOwnProperty(k)
  let count = 0;
  for (let k in obj) {
    if (obj.hasOwnProperty(k)) count++;
  }
  return count;
};
// console.log(getLenStudent(student));
///////////////////////////////
var library = [
  {
    author: "Bill Gates",
    title: "The Road Ahead",
    readingStatus: true,
    libraryID: 1254,
  },
  {
    author: "Steve Jobs",
    title: "Walter Isaacson",
    readingStatus: true,
    libraryID: 4264,
  },
  {
    author: "Suzanne Collins",
    title: "Mockingjay: The Final Book of The Hunger Games",
    readingStatus: false,
    libraryID: 3245,
  },
];
/*
4.Array has objects
display the reading status
Already read 'Bill Gates' by The Road Ahead.
Already read 'Steve Jobs' by Walter Isaacson.
You still need to read 'Mockingjay: The Final Book of The Hunger Games' by Suzanne Collins.
*/
const checkLibrary = function (arr) {
  const res = [];
  for (let obj of arr) {
    if (obj.readingStatus == true) {
      res.push("Already read " + obj.title + " by " + obj.author);
    } else {
      res.push("You still need to read " + obj.title + " by " + obj.author);
    }
  }
  return res;
};
//sort array of JS objects reversely
const sortLibrary = function (arr) {
  return arr.sort((a, b) => b.libraryID - a.libraryID);
};
// console.log(sortLibrary(library));
// console.log(checkLibrary(library));
//////////////////////////////////////
/*
5.Write class
Write a JavaScript program to get the volume of a Cylinder with four decimal places using object classes.
Volume of a cylinder : V = πr2h
where r is the radius and h is the height of the cylinder.
*/
class Cylinder {
  constructor(diameter = null, height = null) {
    this.diameter = diameter;
    this.height = height;
  }
  getVolumn() {
    let r = this.diameter / 2;
    return Math.PI * r * r * this.height;
  }
}
const cyl = new Cylinder(4, 7);
// console.log(cyl.getVolumn().toFixed(4));
//////////////////////////////////////////
/*
6.Subset
Time complexity: str.length!
dog => subset["d", "do", "dog", "o", "og", "g"] :T:3*2*1=3!
*/
const subset = function (str) {
  const res = [];
  for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; j < str.length + 1; j++) {
      res.push(str.slice(i, j));
    }
  }
  return res;
};
// console.log(subset("dog"));
///////////////////////////////////////////
/*
7.Clock
keep updating
*/
class Clock {
  static timer() {
    // 1WAY setInterval(() => console.log(new Date().toLocaleTimeString()), 1000);
    // 2WAY
    setInterval(() => {
      let date = new Date();
      console.log(
        date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds()
      );
    }, 1000);
  }
}
// Clock.timer();
////////////////////////////////////////////////
/*
8.parse an URL
https://dmitripavlutin.com/parse-url-javascript/
*/
const parseUrl = function (url) {
  //     //1WAY built-in method
  //   let parser = new URL(url);
  //   console.log({
  //     source: parser.href,
  //     protocol: parser.protocol,
  //     host: parser.host,
  //     port: parser.port,
  //     search: parser.search,
  //     params: parser.searchParams,
  //     hash: parser.hash,
  //     path: parser.pathname,
  //   });
  //2WAY
  console.log({
    source: url,
    protocol: url.split(":")[0],
  });
};
// parseUrl(
//   "https://www.facebook.com/groups/313956096482261/?hoisted_section_header_type=recently_seen&multi_permalinks=572175623993639"
// );
///////////////////////////////
/*
9. convert one object into a list of '[key, value]' pairs.
*/
const convertPair = function (obj) {
  //1WAY
  const res = [];
  for (let k in obj) {
    const pair = [k, obj[k]]; //here not use obj.k (since search obj property k, so need obj[k]); but if in array search inside, obj's property, obj.key
    res.push(pair);
  }
  return res;
};
// console.log(
//   convertPair({ red: "#FF0000", green: "#00FF00", white: "#FFFFFF" }) //output:[["red","#FF0000"],["green","#00FF00"],["white","#FFFFFF"]]
// );
//2WAY
// console.log(
//   Object.entries({ red: "#FF0000", green: "#00FF00", white: "#FFFFFF" })
// );

//10.get a copy of the object where the keys have become the values and the values become the keys.
const switchPair = function (obj) {
  let res = {};
  for (let k in obj) {
    res[obj[k]] = k;
  }
  return res;
};
// console.log(
//   switchPair({ red: "#FF0000", green: "#00FF00", white: "#FFFFFF" }) //output:{"#FF0000":"red","#00FF00":"green","#FFFFFF":"white"}
// );

//11.check whether an object contains given property.
const checkProperty = function (obj, prop) {
  return obj != null && obj.hasOwnProperty(prop) ? true : false;
};
console.log(
  checkProperty({ red: "#FF0000", green: "#00FF00", white: "#FFFFFF" }, "red")
);
