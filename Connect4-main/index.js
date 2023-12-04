const boardContainer = document.querySelector(".board-container");
createBoard(7, 6);
const createBoard = (width, height) => {
  for (let i = 0; i < width; i++) {
    let newcol = document.createElement("div");
    newcol.setAttribute("col", i);
    boardContainer.appendChild(newcol);
    for (let j = 0; j < height; j++) {
      let newrow = document.createElement("div");
      newrow.setAttribute("row", j);
      newcol.appendChild(newrow);
    }
  }
};
