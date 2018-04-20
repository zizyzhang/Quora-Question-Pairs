
let express = require('express');
let app = express();
app.all('*',function (req, res, next) {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild');
  res.header('Access-Control-Allow-Methods', 'PUT, POST, GET, DELETE, OPTIONS');

  if (req.method === 'OPTIONS') {
    res.send(200);
  }
  else {
    next();
  }
});
let pendingRes = null;

const file = 'model.py';

function startServer(){
	app.listen(3802,function(){
		console.log('ok')	
	});
	
}
startServer();

app.get('/',(req,res)=>{
	res.json({err:false})
})

app.get('/question/:id/:q1/:q2',async (req,res)=>{
	let id = unescape(req.params.id)
	let q1 = unescape(req.params.q1)
	let q2 = unescape(req.params.q2)

	pyshell.send(id+'||||'+q1+'||||'+q2);
	pyshell.send(id+'||||'+q1+'||||'+q2);
	
	if(pendingRes){
		pendingRes.json({err:true});
		pendingRes=null;
	}else{
		pendingRes=res;
	}
})


var PythonShell = require('python-shell');
var options = {
  pythonOptions: ['-i'],
};
var pyshell = new PythonShell(file);
 
// sends a message to the Python script via stdin
pyshell.send('hello');
 
pyshell.on('message', function (message) {
	console.log(message)
	if(message && message[0]==='$'){
		if(pendingRes){
			pendingRes.json({err:false,result:message.slice(1)});
			pendingRes=null;
		}
	}
});
 

process.on('uncaughtException', function (err) {
　　console.log('Caught exception: ' + err);
});