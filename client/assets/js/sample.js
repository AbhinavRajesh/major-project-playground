import * as THREE from "three";
import { OrbitControls } from "https://threejs.org/examples/jsm/controls/OrbitControls.js";


let camera;
//let controls;

let scene = new THREE.Scene();
camera = new THREE.PerspectiveCamera(54, window.innerWidth / window.innerHeight, 0.1, 1000);

renderer = new THREE.WebGLRenderer({
    antialias: true,
    canvas: document.getElementById("viewport")
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(new THREE.Color(0xfefefe));
// document.body.appendChild(renderer.domElement);

camera.position.x = 1.5;
camera.position.y = 5;
camera.position.z = -1.5 + window.scrollY / 250.0;
camera.lookAt(0, 0, -1.5);

//controls = new THREE.OrbitControls(camera);

// white spotlight shining from the side, casting a shadow
let spotLight = new THREE.SpotLight(0xffffff, 2.5, 25, Math.PI / 6);
spotLight.position.set(9, 10, 1);
scene.add(spotLight);

let gridHelper = new THREE.GridHelper(4, 4);
scene.add(gridHelper);

// example code
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial({
    color: 0xff0000
});
const topBox = new THREE.Mesh(geometry, material);
scene.add(topBox);

///// end of example

let animate = function() {
    requestAnimationFrame(animate);

    //controls.update();
    renderer.render(scene, camera);
};

animate();

function updateCamera(ev) {
    let div1 = document.getElementById("div1");
	camera.position.z = -1.5 + window.scrollY / 250.0;
}

window.addEventListener("scroll", updateCamera);