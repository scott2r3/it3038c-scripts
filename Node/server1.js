const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');
const numCPU = os.cpus().length
const totalMem = os.totalmem();
const freemem = os.freemem();
var freemem1 = (freemem/1000000).toFixed(2);
var totalmem1 = (totalMem/1000000).toFixed(2);
var ut = os.uptime();
var ut_minutes = ut/60;
var ut_hours = ut_minutes/60;
var ut_days = ut_days/24;
ut1 = Math.floor(ut);
ut_minutes = Math.floor(ut_minutes);
ut_hours = Math.floor(ut_hours);
ut_days = Math.floor(ut_days);
ut = ut%60;
ut_minutes = ut_minutes%60;
ut_hours = ut_hours%60;
ut_days = ut_days%24;

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${ut_days} Days ${ut_hours} Hours ${ut_minutes} Minutes ${ut} Seconds</p>
        <p>Total Memory: ${totalmem1} MB</p>
        <p>Free Memory: ${freemem1} MB</p>
        <p>Number of CPUs: ${numCPU} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");