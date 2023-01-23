import React, { Suspense, useState } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, useGLTF } from "@react-three/drei";
import * as THREE from "three";
import "./App.css";

import Video from "./assets/video/dummy.mp4";
import Cinema from "./Cinema";
import Chat from "./pages/Chat";

const Theatre = () => {
  const { nodes, scene } = useGLTF("cinema.glb");

  const [video] = useState(() => {
    const _video = document.createElement("video");
    _video.src = Video;
    _video.crossOrigin = "Anonymous";
    _video.loop = true;
    _video.muted = true;
    _video.play();
    return _video;
  });

  console.log(nodes, scene);

  return (
    <>
      <group>
        {/* <Cinema /> */}
        {/* <mesh geometry={nodes.frame.geometry}>
        <meshStandardMaterial color="white" />
      </mesh> */}
        <mesh rotation={[0, 0, 0]} position={[0, 0, 2]}>
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

const Floor = () => {
  return (
    <mesh rotation={[-Math.PI / 2, 0, 0]} position={[-2, -2, 0]}>
      <planeBufferGeometry args={[100, 100]} />
      <meshStandardMaterial color="white" />
    </mesh>
  );
};

function App() {
  if (window.location.pathname === "/chat") return <Chat />;
  return (
    <Canvas>
      <fog attach="fog" args={["black", 1, 7]} />
      <OrbitControls maxPolarAngle={Math.PI / 2} minPolarAngle={0} />
      <directionalLight intensity={0.5} />
      <Suspense fallback={null}>
        <Theatre />
        {/* <Cinema /> */}
      </Suspense>

      <Floor />
    </Canvas>
  );
}

export default App;
