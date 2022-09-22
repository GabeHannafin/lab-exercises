let canvas;
let context;

let request;

let fpsInterval = 1000 / 60;
let now;
let then = Date.now();

let sheep = {
    x : 800,
    y : 700,
    xChange: 0,
    yChange: 0,
    xFrame: 0, 
    yFrame: 0, 
    size : 128
};

let scissors = {
    x : 0,
    y : 0,
    xChange : 15,
    yChange : 10,
    width : 75,
    height: 60,
    xFrame: 0,
    yFrame: 0
};

let IMAGES = { sheep : "ram_walk.png", scissors: "scissors.png" };
let moveLeft = false;
let moveRight = false;
let moveUp = false;
let moveDown = false;

document.addEventListener("DOMContentLoaded", init, false)

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    window.addEventListener("keydown", activate, false)
    window.addEventListener("keyup", deactivate, false)

    load_images(draw);
}

function draw() {
    request = window.requestAnimationFrame(draw);
    
    // Throttling
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval);

    if (player_collides(scissors)) {
        stop();
    }

    if (sheep.x <= 0) {
        xChange = 0;
    }
    
    // Clear the canvas
    context.clearRect(0, 0, canvas.width, canvas.height)

    // Background colour
    context.fillStyle = "green";
    context.fillRect(0,0,canvas.width,canvas.height);

    // Draw sheep
    context.drawImage(IMAGES.sheep,
        sheep.xFrame * sheep.size, sheep.yFrame * sheep.size, sheep.size, sheep.size,
        sheep.x, sheep.y, sheep.size*2, sheep.size*2);

    // Cycle through the sprites
    if (moveLeft || moveRight || moveUp || moveDown) {
        sheep.xFrame = (sheep.xFrame +1) %4;
    }

    // Move sheep
    if (moveLeft) {
        sheep.xChange = -8
        // added acceleration
        sheep.xChange = sheep.xChange - 0.1
        sheep.yFrame = 1
    }
    if (moveRight) {
        sheep.xChange = 8
        // added acceleration
        sheep.xChange = sheep.xChange + 0.1
        sheep.yFrame = 3
    }
    if (moveUp) {
        sheep.yChange = -8
        // added acceleration
        sheep.yChange = sheep.yChange - 0.1
        sheep.yFrame = 0
    }
    if (moveDown) {
        sheep.yChange = 8
        // added acceleration
        sheep.yChange = sheep.yChange + 0.1
        sheep.yFrame = 2
    }

    // Update position only if not moving diagonal
    if ((moveUp || moveDown) && (moveLeft || moveRight)) {
        sheep.x = sheep.x
        sheep.y = sheep.y + sheep.yChange
    } else {
        sheep.y = sheep.y + sheep.yChange
        sheep.x = sheep.x + sheep.xChange
    }

    // Wall Colision
    if ((sheep.x + sheep.size) > canvas.width) {
        sheep.x = canvas.width - (sheep.size);
    } else if (sheep.x + sheep.size< 0) {
        sheep.x = 0;
    } else if (sheep.y < 0) {
        sheep.y = 0;
    } else if ((sheep.y + sheep.size) > canvas.height) {
        sheep.y = canvas.height - sheep.size;
    }


    // Friction
    sheep.xChange = sheep.xChange * 0.5
    sheep.yChange = sheep.yChange * 0.5

    // Scissors
    
    // Draw scissors
    context.drawImage(IMAGES.scissors,
        scissors.xFrame * scissors.width, scissors.yFrame * scissors.height, scissors.width, scissors.height,
        scissors.x, scissors.y, scissors.width *2, scissors.height*2);

    // Cycle animations
    scissors.xFrame = (scissors.xFrame +1) %6;

    // Constantly move
    scissors.x = scissors.x + scissors.xChange;
    scissors.y = scissors.y + scissors.yChange;

    // collision
    if (scissors.x < 0 || scissors.x > canvas.width) {
        scissors.xChange = -scissors.xChange;

    } else if (scissors.y < 0 || (scissors.y +scissors.height) > canvas.height || scissors.x < 0){
        scissors.yChange = -scissors.yChange;
    }
}

function player_collides(a) {
    if (sheep.x + sheep.size < a.x || a.x + a.width < sheep.x || sheep.y > a.y || a.y > sheep.y + sheep.size) {
        return false;
    } else {
        return true;
    }
}
       

function activate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = true;
    }
    if (key === "ArrowRight") {
        moveRight = true;
    }
    if (key === "ArrowUp") {
        moveUp = true;
    }
    if (key === "ArrowDown") {
        moveDown = true;
    }
}

function deactivate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = false;
    }
    if (key === "ArrowRight") {
        moveRight = false;
    }
    if (key === "ArrowUp") {
        moveUp = false;
    }
    if (key === "ArrowDown") {
        moveDown = false;
    }
}

function load_images(callback) {
    let num_images = Object.keys(IMAGES).length;
    let loaded = function() {
        num_images = num_images -1;
        if (num_images === 0) {
            callback();
        }
    };
    for (let name of Object.keys(IMAGES)) {
        let img = new Image();
        img.addEventListener("load", loaded, false);
        img.src = IMAGES[name];
        IMAGES[name] = img;
    }
}

function stop() {
    let outcome = document.querySelector("h1");
    outcome.innerHTML = "LOSERRRRR";
    window.cancelAnimationFrame(request);
}

function random(min, max) {
    return Math.round(Math.random() * (max -min)) + min;
}
