import * as THREE from "three";
import Body from "./Body.js";
import Hands from "./Hands.js";
import Head from "./Head.js";
import Legs from "./Legs.js";

function Person(BASE_X = 0, BASE_Y = 0, BASE_Z = 0) {
  const person = new THREE.Group();

  const { left_leg, right_leg } = Legs();
  const { left_hand, right_hand } = Hands();
  person.add(Head());
  person.add(Body());
  person.add(left_hand);
  person.add(right_hand);
  person.add(left_leg);
  person.add(right_leg);

  person.position.x = BASE_X;
  person.position.y = BASE_Y;
  person.position.z = BASE_Z;
  person.rotation.y = 0.277 * Math.PI;
  // person.rotation.z = 0.277 * Math.PI;
  // person.rotation.x = 0.277 * Math.PI;

  return person;
}

// function Person(BASE_X = 0, BASE_Y = 0, BASE_Z = 0) {
//   const person = new THREE.Group();
//   const HEAD_RAD = 3,
//     BODY_RAD = 3,
//     BODY_HEIGHT = 15,
//     LEG_LEN = 15,
//     HAND_LEN = 10,
//     COLOR = 0xa1665e;

//   const headGeo = new THREE.SphereGeometry(HEAD_RAD);
//   const headMat = new THREE.MeshLambertMaterial({ color: COLOR });
//   const head = new THREE.Mesh(headGeo, headMat);
//   person.add(head);

//   const bodyGeo = new THREE.CylinderGeometry(
//     BODY_RAD,
//     BODY_RAD + 1,
//     BODY_HEIGHT,
//     20
//   );
//   const bodyMat = new THREE.MeshLambertMaterial({ color: COLOR });
//   const body = new THREE.Mesh(bodyGeo, bodyMat);
//   body.position.y -= HEAD_RAD * 3;
//   person.add(body);

//   const legGeo = new THREE.CylinderGeometry(1.5, 1, LEG_LEN, 20);
//   const legMat = new THREE.MeshLambertMaterial({ color: COLOR });
//   const left_leg = new THREE.Mesh(legGeo, legMat);
//   const right_leg = new THREE.Mesh(legGeo, legMat);
//   left_leg.position.x += BODY_RAD - 1.5;
//   left_leg.position.y -= HEAD_RAD * 2 + BODY_HEIGHT;
//   right_leg.position.x -= BODY_RAD - 1.5;
//   right_leg.position.y -= HEAD_RAD * 2 + BODY_HEIGHT;
//   person.add(left_leg);
//   person.add(right_leg);

//   const handGeo = new THREE.CylinderGeometry(1, 1.5, HAND_LEN, 20);
//   const handMat = new THREE.MeshLambertMaterial({ color: COLOR });
//   const left_hand = new THREE.Mesh(handGeo, handMat);
//   const right_hand = new THREE.Mesh(handGeo, handMat);
//   left_hand.position.x += BODY_RAD;
//   left_hand.position.y -= HEAD_RAD * 2;
//   left_hand.position.z += HAND_LEN / 2;
//   right_hand.position.x -= BODY_RAD;
//   right_hand.position.y -= HEAD_RAD * 2;
//   right_hand.position.z += HAND_LEN / 2;
//   right_hand.rotation.x = 0.6 * Math.PI;
//   left_hand.rotation.x = 0.6 * Math.PI;
//   person.add(left_hand);
//   person.add(right_hand);

//   person.position.x = BASE_X;
//   person.position.y = BASE_Y;
//   person.position.z = BASE_Z;

//   return person;
// }

export { Person };
