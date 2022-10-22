import * as THREE from "three";
import { BODY_COLOR, BODY_RAD, HAND_LEN, HEAD_RAD } from "./constants.js";

function Hands() {
  const handGeo = new THREE.CylinderGeometry(1, 1.5, HAND_LEN, 20);
  const handMat = new THREE.MeshLambertMaterial({ color: BODY_COLOR });
  const left_hand = new THREE.Mesh(handGeo, handMat);
  const right_hand = new THREE.Mesh(handGeo, handMat);
  left_hand.position.x += BODY_RAD / 1.2;
  left_hand.position.y -= HEAD_RAD * 2;
  left_hand.position.z += HAND_LEN / 2;
  right_hand.position.x -= BODY_RAD / 1.2;
  right_hand.position.y -= HEAD_RAD * 2;
  right_hand.position.z += HAND_LEN / 2;
  right_hand.rotation.x = 0.6 * Math.PI;
  left_hand.rotation.x = 0.6 * Math.PI;
  return { left_hand, right_hand };
}

export default Hands;
