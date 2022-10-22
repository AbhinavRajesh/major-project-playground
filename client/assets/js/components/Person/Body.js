import * as THREE from "three";
import { BODY_HEIGHT, BODY_RAD, HEAD_RAD, SHIRT_COLOR } from "./constants.js";

function Body() {
  const bodyGeo = new THREE.CylinderGeometry(
    BODY_RAD - 1.5,
    BODY_RAD,
    BODY_HEIGHT,
    50
  );
  const bodyMat = new THREE.MeshLambertMaterial({ color: SHIRT_COLOR });
  const body = new THREE.Mesh(bodyGeo, bodyMat);
  body.position.y -= HEAD_RAD * 2;
  return body;
}
export default Body;
