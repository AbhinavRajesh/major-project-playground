import React, { Suspense, useEffect, useState } from "react";
import { Canvas, useThree } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import * as THREE from "three";
import "./App.css";

import Video from "./assets/video/dummy.mp4";

import Hall from "./Hall";

const Theatre = () => {
  const [video] = useState(() => {
    const _video = document.createElement("video");
    _video.src = Video;
    _video.crossOrigin = "Anonymous";
    _video.loop = true;
    _video.muted = true;
    _video.play();
    return _video;
  });

  return (
    <>
      <group position={[0, -260, -280]} scale={150}>
        <mesh rotation={[0, 0, 0]} position={[0, 2, 3]}>
          <planeGeometry args={[3.2, 1.9]} />
          <meshStandardMaterial emissive="white" side={THREE.DoubleSide}>
            <videoTexture attach="map" args={[video]} />
            <videoTexture attach="emissiveMap" args={[video]} />
          </meshStandardMaterial>
        </mesh>
      </group>
    </>
  );
};

const Controls = () => {
  const { camera } = useThree();

  const handleKeyPress = (e: KeyboardEvent) => {
    switch (e.key) {
      case "w":
        camera.translateZ(-10);
        break;
      case "s":
        camera.translateZ(10);
        break;
      case "a":
        camera.translateX(10);
        break;
      case "d":
        camera.translateX(-10);
        break;
    }
    console.log(camera);
  };
  useEffect(() => {
    document.addEventListener("keypress", handleKeyPress);

    return () => {
      document.removeEventListener("keypress", handleKeyPress);
    };
  });

  return null;
};

function App() {
  return (
    <Canvas
      camera={{
        near: 0.1,
        far: 100,
        position: [2, 6, 7],
      }}
    >
      <OrbitControls
        maxPolarAngle={Math.PI / 2}
        minPolarAngle={0}
        minDistance={100}
        maxDistance={300}
      />
      <ambientLight intensity={0.1} color="#b9d5ff" />
      <directionalLight intensity={1.2} color="#b9d5ff" position={[-4, 5, 2]} />
      <Suspense fallback={<Theatre />}>
        <Theatre />
        <Controls />
        <Hall />
      </Suspense>
    </Canvas>
  );
}

export default App;
