import * as THREE from "three";
import { OrbitControls } from "https://threejs.org/examples/jsm/controls/OrbitControls.js";
import { Person } from "./components/person.js";

const scene = new THREE.Scene();
const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
directionalLight.position.set(200, 500, 300);
scene.add(directionalLight);

const aspectRatio = window.innerWidth / window.innerHeight;
const cameraWidth = 150;
const cameraHeight = cameraWidth / aspectRatio;

const camera = new THREE.OrthographicCamera(
  cameraWidth / -2, // left
  cameraWidth / 2, // right
  cameraHeight / 2, // top
  cameraHeight / -2, // bottom
  0, // near plane
  1000 // far plane
);
camera.position.set(200, 200, 200);

const geometry = new THREE.PlaneGeometry(100, 100);
const material = new THREE.MeshBasicMaterial({
  color: 0x333333,
  side: THREE.DoubleSide,
});
const plane = new THREE.Mesh(geometry, material);
plane.rotation.x += 1;
plane.rotation.y += 0.5;
plane.rotation.z += 0;
// scene.add(plane);

const client1 = Person(30, 30, -30);
scene.add(client1);
const client2 = Person(-20, 20, 30);
scene.add(client2);
const client3 = Person(0, 0, 10);
scene.add(client3);

// LAST
const renderer = new THREE.WebGLRenderer({ antialias: true });
const controls = new OrbitControls(camera, renderer.domElement);
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.render(scene, camera);
document.body.appendChild(renderer.domElement);
