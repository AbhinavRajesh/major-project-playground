import * as THREE from "three";
import { OrbitControls } from "https://threejs.org/examples/jsm/controls/OrbitControls.js";

const scene = new THREE.Scene();


// your code here
const camera = new THREE.PerspectiveCamera( 1000, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.PlaneGeometry( 1, 1 );
const material = new THREE.MeshBasicMaterial( {color: 0xffff00, side: THREE.DoubleSide} );


const plane = new THREE.Mesh( geometry, material );
scene.add( plane );



camera.position.z = 5;

function animate() {
	requestAnimationFrame( animate );
  if (THREE.MOUSE)
  {plane.rotation.x += 0.01;
  }
  else if(THREE.MOUSE.ROTATE)
  {

  plane.rotation.y += 0.01;
  }
	renderer.render( scene, camera );
}
animate();




