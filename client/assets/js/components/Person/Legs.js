import * as THREE from "three";
import {
  BODY_COLOR,
  BODY_HEIGHT,
  BODY_RAD,
  HEAD_RAD,
  LEG_LEN,
} from "./constants.js";

function Legs() {
  const legGeo = new THREE.CylinderGeometry(1.5, 1, LEG_LEN, 20);
  const legMat = new THREE.MeshLambertMaterial({ color: BODY_COLOR });
  const left_leg = new THREE.Mesh(legGeo, legMat);
  const right_leg = new THREE.Mesh(legGeo, legMat);
  left_leg.position.x += BODY_RAD - 1.5;
  left_leg.position.y -= HEAD_RAD + BODY_HEIGHT;
  right_leg.position.x -= BODY_RAD - 1.5;
  right_leg.position.y -= HEAD_RAD + BODY_HEIGHT;
  return { left_leg, right_leg };
}

export default Legs;
