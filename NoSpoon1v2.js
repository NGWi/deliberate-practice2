// A straightforward way to solve this in O(n) where n is the number of nodes.

let width, height;
width = parseInt(readline());
height = parseInt(readline());

// An array to hold the coordinates string for each node that exists,
// to be built up as we go along, and printed out at the end:
// Example members: "0 0 1 0 0 1", "1 0 -1 -1 -1 -1"
let bigArray = [];
let key = 0;

// All existing nodes' main indices + coordinates, grouped by their row;
// easy peasy (i.e. O(1)) to find the next node to the right.
// Example members: [0=0 0, 1=1 0], [2=0 1]
let rowsArray = [];
for (let i = 0; i < height; i++) {
  rowsArray.push([]);
}

// All existing nodes' main indices + coordinates, grouped by their column;
// easy peasy (i.e. O(1)) to find the next node below.
// Example members: [0=0 0, 2=0 1], [1=1 0]
let columnsArray = [];
for (let i = 0; i < width; i++) {
  columnsArray.push([]);
}

// Go through all the nodes the first time:
for (let i = 0; i < height; i++) {
  let line = readline();
  let y = i;
  let x = 0;
  for (let char of line) {
    if (char === "0") {
      let coordinates = `${x} ${y} `;
      bigArray.push(coordinates);
      rowsArray[y].push(`${key}=${coordinates}`);
      columnsArray[x].push(`${key}=${coordinates}`);
      key++;
    }
    x++;
  }
}

//  Go through the rows_array to add all the nodes to the right of each node (or -1 -1)
for (let row of rowsArray) {
  let length = row.length;
  for (let i = 0; i < length; i++) {
    let nodeIndex = parseInt(row[i].split("=")[0]);
    if (i < length - 1) {
      let nextNode = row[i + 1];
      let nextCoord = nextNode.split("=")[1];
      bigArray[nodeIndex] += nextCoord;
    } else {
      bigArray[nodeIndex] += "-1 -1 ";
    }
  }
}

// Go through the columns_array for the nodes below each node.
for (let column of columnsArray) {
  let length = column.length;
  for (let i = 0; i < length; i++) {
    let nodeIndex = parseInt(column[i].split("=")[0]);
    if (i < length - 1) {
      let nextNode = column[i + 1];
      let nextCoord = nextNode.split("=")[1];
      bigArray[nodeIndex] += nextCoord;
    } else {
      bigArray[nodeIndex] += "-1 -1";
    }
  }
}
// Go through the big_array in order of its main indices and print each node's coordinate set one at a time:
for (let coord of bigArray) {
  console.log(coord);
}
