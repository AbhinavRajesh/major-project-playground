import * as THREE from "three";
import { BODY_COLOR, HEAD_RAD } from "./constants.js";

function Head() {
  const headGeo = new THREE.SphereGeometry(HEAD_RAD);
  const headMat = new THREE.MeshLambertMaterial({ color: BODY_COLOR });
  const head = new THREE.Mesh(headGeo, headMat);
  return head;
}
export default Head;
