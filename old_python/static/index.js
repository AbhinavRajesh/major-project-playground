var socket = io();
socket.on('connect', function () {
            socket.emit('my_event', {data: 'I\'m connected!'});
});
const videoElement = document.getElementsByClassName('input_video')[0];
const canvasElement = document.getElementsByClassName('output_canvas')[0];
const controlsElement =document.getElementsByClassName('control-panel')[0];
const canvasCtx = canvasElement.getContext('2d');
const finalCanvas = document.getElementById('final_canvas');
const finalCtx = finalCanvas.getContext('2d');
const video = videoElement
let canvas = document.getElementById('canvas');
context = canvas.getContext('2d');
let result = document.getElementById('result');
let context2 = result.getContext('2d');
const photo = document.getElementById('photo');
const photores = document.getElementById('phres');
const startbutton = document.getElementById('startbutton');
const fpsControl = new FPS();
var fpsval;
var mode = true;
var counter = 0;
var streaming = false;
var width = 320;
var height = 0; 
var ping_pong_times = [];
var start_time;
window.setInterval(function () {
    start_time = (new Date).getTime();
    socket.emit('my_ping');
}, 1000);

socket.on('my_pong', function () {
    var latency = (new Date).getTime() - start_time;
    ping_pong_times.push(latency);
    ping_pong_times = ping_pong_times.slice(-30); // keep last 30 samples
    var sum = 0;
    for (var i = 0; i < ping_pong_times.length; i++)
        sum += ping_pong_times[i];
    $('#ping-pong').text(Math.round(10 * sum / ping_pong_times.length) / 10);
});

socket.on('switch', function (data) {
  mode = true
  counter = 0
})

function startup() {
    
    navigator.mediaDevices.getUserMedia({video: true, audio: false})
    .then(function(stream) {
      video.srcObject = stream;
      video.play();
    })
    .catch(function(err) {
      console.log("An error occurred: " + err);
    });
    video.addEventListener('canplay', function(ev){
      if (!streaming) {
        height = video.videoHeight / (video.videoWidth/width);
        if (isNaN(height)) {
          height = width / (4/3);
        }
        video.setAttribute('width', width);
        video.setAttribute('height', height);
        canvas.setAttribute('width', width);
        canvas.setAttribute('height', height);
        streaming = true;
      }
    }, false);
    
   
  }

function onResults(results) {
    canvasCtx.save();
    fpsControl.tick();
    fpsval = fpsControl.a[9];
    counter = counter + 1
    if(fpsval < 18 && results.multiHandLandmarks && counter > 60){
        mode = false
    }
    canvasCtx.clearRect(0, 0, canvasElement.width, canvasElement.height);
    canvasCtx.drawImage(
        results.image, 0, 0, canvasElement.width, canvasElement.height);
    if (results.multiHandLandmarks) {
    socket.emit('send_hand_points',results.multiHandLandmarks)
    }
    canvasCtx.restore();
}

const hands = new Hands({locateFile: (file) => {
    return `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`;
}});
hands.setOptions({
    maxNumHands: 2,
    minDetectionConfidence: 0.5,
    minTrackingConfidence: 0.5
});
hands.onResults(onResults);



const camera = new Camera(videoElement, {
    onFrame: async () => {
    if(mode === true) {
        await hands.send({image: videoElement});
    }
    },
    width: 320,
    height: 240
});
camera.start();

new ControlPanel(controlsElement, {

  })
  .add([
    fpsControl,
  ])


    
    setInterval(function(){
        // if (!mode){
        takepicture();
        // }
    },66)
   
  
    function takepicture() {
      if (width && height) {
        canvas.width = width;
        canvas.height = height;
        context.drawImage(video, 0, 0, width, height);
        if(!mode){
          canvas.toBlob((data) => {
            socket.emit('image_recv',data)
        },'image/jpeg');
        }
      }
    }
  
    socket.on('imgbackend', function (data) {
        var urlCreator = window.URL || window.webkitURL;
        newdata = new Blob([data.data],{ type: "image/png" })
        var resurl = urlCreator.createObjectURL(newdata)
        var imgurl = canvas.toDataURL();
        
        mergeImages([
          {src: imgurl},
          {src: resurl}
        ])
        .then(b64 => photores.src = b64);
        // console.log(url)
        
        // if(!context2){
        //   result = document.getElementById('result');
        //   context2 = result.getContext('result');
        // }
        // console.log(result, context2)
        // var img = new Image;
        // img.onload = function(){
        //   context2.drawImage(img,0,0); // Or at whatever offset you like
        // };
        // img.src = resurl
        // // context2.drawImage(img, 0, 0, 320 , 240);
        // let imageData = context2.getImageData(0, 0, 320, 240);
        // let imageData1 = context.getImageData(0, 0, 320, 240);
        // let pixels = imageData.data;
        // let pixels1 = imageData1.data;
        // for (let i = 0; i < pixels.length; i += 4) {
        //     let r = pixels[i], g = pixels[i + 1], b = pixels[i + 2];
        //     // console.log()
        //     if (r === 0 && g === 0 && b === 0)
        //         pixels[i + 3] = 0
        //         pixels[i + 2] =  pixels1[i + 2]
        //         pixels[i + 1] =  pixels1[i + 2]
        //         pixels[i + 0] =  pixels1[i + 2]

        // }
        // var can2 = document.createElement('canvas');
      // set can2's width and height, get the context etc...
        // ctx2.putImageData(resultData, 0, 0);

        // context2.putImageData(imageData, 0, 0);
        // context.drawImage(result, 0, 0);

        // photo.src = resurl
        photores.onload = function() {
            // blend();
            urlCreator.revokeObjectURL(resurl);
        }
        
        
        
    })

    

    // Set up our event listener to run the startup process
    // once loading is complete.
    window.addEventListener('load', startup, false);
