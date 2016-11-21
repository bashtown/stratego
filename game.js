var map = [
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,'X','X',0,0,'X','X',0,0],
			[0,0,'X','X',0,0,'X','X',0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0]
		]






function printMap(m){
	for (i=0; i < m.length; i++){
		line = ''
		for (y=0; y < m[i].length; y++){
			if(typeof(m[i][y]) === 'object'){
				line += m[i][y].num
			}else{
				line += m[i][y]
			}
		}
		console.log(line)
	}
}

function Piece(n){
	this.num = n
	this.x 
	this.y
	this.move = function(dir, dist=1){
		console.log("Move " + dir + ' ' + dist)
	}
	
	this.place = function(xPos, yPos){
		this.x = xPos
		this.y = yPos
	}
}

function placePiece(m, p, x, y){ //Y coordinates increase in downward direction.
	p.place(x, y);
	m[y][x] = p
}
