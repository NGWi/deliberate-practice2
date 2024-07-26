const readline = require("readline");

let width, height;
let bigArray = [];
let rowsArray = [];
let columnsArray = [];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  if (!width) {
    width = parseInt(line);
  } else if (!height) {
    height = parseInt(line);
    for (let i = 0; i < height; i++) {
      rowsArray.push([]);
    }
    for (let i = 0; i < width; i++) {
      columnsArray.push([]);
    }
  } else {
    let y = rowsArray.length - height;
    let x = 0;
    for (let char of line) {
      if (char === "0") {
        let coordinates = `${x} ${y} `;
        bigArray.push(coordinates);
        rowsArray[y].push(`${bigArray.length - 1}=${coordinates}`);
        columnsArray[x].push(`${bigArray.length - 1}=${coordinates}`);
      }
      x++;
    }
    height--;
    if (height === 0) {
      rl.close();
      processNodes();
    }
  }
});

function processNodes() {
  for (let row of rowsArray) {
    for (let i = 0; i < row.length; i++) {
      let nodeIndex = parseInt(row[i].split("=")[0]);
      if (i < row.length - 1) {
        let nextNode = row[i + 1];
        let nextCoord = nextNode.split("=")[1];
        bigArray[nodeIndex] += nextCoord;
      } else {
        bigArray[nodeIndex] += "-1 -1 ";
      }
    }
  }

  for (let column of columnsArray) {
    for (let i = 0; i < column.length; i++) {
      let nodeIndex = parseInt(column[i].split("=")[0]);
      if (i < column.length - 1) {
        let nextNode = column[i + 1];
        let nextCoord = nextNode.split("=")[1];
        bigArray[nodeIndex] += nextCoord;
      } else {
        bigArray[nodeIndex] += "-1 -1";
      }
    }
  }

  for (let coord of bigArray) {
    console.log(coord);
  }
}
