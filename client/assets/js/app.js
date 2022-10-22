import * as THREE from "three";
import { OrbitControls } from "https://threejs.org/examples/jsm/controls/OrbitControls.js";

const scene = new THREE.Scene();

// your code here

// LAST
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.render(scene, camera);
document.body.appendChild(renderer.domElement);
