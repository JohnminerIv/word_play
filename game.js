var c = document.getElementById("game");
var ctx = c.getContext("2d");
var ball;
var bx = 300;
var by = 300;
var y1 = 300;
var y2 = 300;
var speed = 50;
var bspdy = Math.floor((Math.random() * 8) - 4);
var bspdx = Math.floor((Math.random() * 8) - 4);
var win = false;
var lose = false;
var pause = false;

function setup(){
    ball = new Ball();
    puck1 = new Puck(0,"a","z",2);
    puck2 = new Puck(580,"p","l",1);
    nn = new neuraln();
    document.addEventListener('keydown',function(event){
        if(event.keyCode == 32 && pause == true){
            win = false;
            lose = false;
            pause = false;
            bx = 300;
            by = 300;
            y1 = 300;
            y2 = 300;
            speed = 50;
            bspdy = Math.floor((Math.random() * 4) + 1);
            bspdx = Math.floor((Math.random() * 4) + 3);
            ball = new Ball();
            puck1 = new Puck(0,"a","z",2);
            puck2 = new Puck(580,"p","l",1);

        }
        else if (event.keyCode == 81){
            if (y2-50 >= 0){
                y2= y2 - 50;
            }



        }
        else if (event.keyCode == 65){
            if (y2+50 <= 500){
                y2= y2 + 50;
            }


        }
        else{

        }
    });
}
function sigmoid(t) {
    return 1/(1+Math.pow(Math.E, -t));
}

class Puck{
    constructor(x,key1,key2,num){
        this.x = x;
        this.key1 = key1;
        this.key2 = key2;
        this.width = 20;
        this.height = 100;
        this.num = num;
}


    draw(){
        if (this.num==1){
            ctx.fillStyle = "#FF0000";
            ctx.fillRect(this.x,y1,this.width,this.height);}
else {
    ctx.fillStyle = "#FF0000";
    ctx.fillRect(this.x,y2,this.width,this.height);
}

    }
}

class Ball{
    constructor(){
        this.x = 50;
        this.y = 50;
        this.size = 50;

    }
    updatexpos(){
        if (pause == true){
            bx = 300;
            by = 300;
        }
        if (by > y1-50 && by < y1+50){
            if (bx + bspdx > 555){
                bspdx = -bspdx*1.25;
            }
        }
        if (by > y2-50 && by < y2+50){
            if (bx + bspdx < 20){

                bspdx = -bspdx*1.25;
            }
        }
        if (bx + bspdx > 0 && bx + bspdx < 575){
                bx = bx + bspdx;
        }
        else{
            if(bx + bspdx <= 0){
                pause = true;
                lose = true;

            }
            else if(bx + bspdx >= 575){
                pause = true;
                win = true;

            }
        }
        if (by + bspdy > 0 && by + bspdy < 560){
                by = by + bspdy;
        }
        else{
            bspdy = -bspdy;
        }

    }
    draw(){
        ctx.fillStyle = "#FF0000";
        ctx.fillRect(bx, by, this.size, this.size);
    }
}
class neuraln {
    constructor(){

        this.w1 = Math.random()*2 - 1;
        this.w2 = Math.random()*2 - 1;
        this.w3 = Math.random()*2 - 1;
        this.w4 = Math.random()*2 - 1;
        this.w5 = Math.random()*2 - 1;
        this.w6 = Math.random()*2 - 1;
        this.w7 = Math.random()*2 - 1;
        this.w8 = Math.random()*2 - 1;
        this.w9 = Math.random()*2 - 1;
        this.w0 = Math.random()*2 - 1;
        this.b1 = Math.random()*2 - 1;
        this.b2 = Math.random()*2 - 1;
        this.b3 = Math.random()*2 - 1;
        this.b4 = Math.random()*2 - 1;
        this.b5 = Math.random()*2 - 1;
        this.b6 = Math.random()*2 - 1;
        this.b7 = Math.random()*2 - 1;
        this.b8 = Math.random()*2 - 1;
        this.b9 = Math.random()*2 - 1;
        this.b0 = Math.random()*2 - 1;
        this.b11 = Math.random()*2 - 1;
        this.b12 = Math.random()*2 - 1;
        this.b13 = Math.random()*2 - 1;
        this.b14 = Math.random()*2 - 1;
        this.b15 = Math.random()*2 - 1;
        this.c1 = Math.random()*2 - 1;
        this.c2 = Math.random()*2 - 1;
        this.c3 = Math.random()*2 - 1;
        this.c4 = Math.random()*2 - 1;
        this.c5 = Math.random()*2 - 1;
        this.c6 = Math.random()*2 - 1;


    }
    updinputs(bx, by, bspdx, bspdy, y2){
        this.bx = bx-300;
        this.by = by-300;
        this.bspdx = bspdx;
        this.bspdy = bspdy;
        this.y2 = y2-300;


    }
    network(){
    this.node1 = sigmoid(this.bx)*this.w1;
    this.node2 = sigmoid(this.by)*this.w2;
    this.node3 = sigmoid(this.bspdx)*this.w3;
    this.node4 = sigmoid(this.bspdy)*this.w4;
    this.node5 = sigmoid(this.y2)*this.w5;
    this.node6 = sigmoid(this.node1 * this.b1 + this.node2 + this.b2 + this.node3 * this.b3 + this.node4 * this.b4 + this.node5 * this.b5);
    this.node7 = sigmoid(this.node1 * this.b6 + this.node2 + this.b7 + this.node3 * this.b8 + this.node4 * this.b9 + this.node5 * this.b0);
    this.node8 = sigmoid(this.node1 * this.b11 + this.node2 + this.b12 + this.node3 * this.b13 + this.node4 * this.b14 + this.node5 * this.b15);
    this.node9 = sigmoid(this.node6 * this.c1 + this.node7 + this.c2 + this.node8 * this.c3);
    this.node10 = sigmoid(this.node6 * this.c4 + this.node7 + this.c5 + this.node8 * this.c6);
    }
    move(){

            if(this.node9 > 0.90){
                if(y1-50 >= 0){
                    y1= y1 - 50;
                }

            }
            else if (this.node10 > 0.90) {
                if (y1+50 <= 500){
                    y1= y1 + 50;
                }


            }


    }


}

function draw(){
    if(pause == false){
         ctx.clearRect(0, 0, 600, 600);
        ctx.fillStyle = "#000000";
        ctx.fillRect(0, 0, 600, 600);
             ball.updatexpos();
             nn.updinputs(bx,by,bspdx,bspdy,y1);
             nn.network();
            nn.move();

        ball.draw();
        puck1.draw();
        puck2.draw();}
    else if (pause == true && win == true){
        ctx.clearRect(0, 0, 600, 600);
       ctx.fillStyle = "#000000";
       ctx.fillRect(0, 0, 600, 600);
       ball.updatexpos();

    }
    else{
        ctx.clearRect(0, 0, 600, 600);
       ctx.fillStyle = "#FF0000";
       ctx.fillRect(0, 0, 600, 600);
       ball.updatexpos();

    }



}
setup();
var intervalID = window.setInterval(draw, 50);
