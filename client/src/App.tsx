import React, { Suspense, useEffect, useState } from "react";
import { Canvas, useThree, useLoader } from "@react-three/fiber";
import { VRButton, XR, Controllers, Hands } from "@react-three/xr";
import { OrbitControls } from "@react-three/drei";
import * as THREE from "three";
import "./App.css";

import Chat from "./pages/Chat";
import Hall from "./Hall";
import { SERVER } from "./infrastructure";

const Theatre = () => {
  const [frameUrl, setFrameUrl] = useState<string>(
    "https://st2.depositphotos.com/6797658/10299/v/950/depositphotos_102990436-stock-illustration-happy-pathers-day-love-dady.jpg"
  );
  const texture = useLoader(THREE.TextureLoader, frameUrl);
  texture.needsUpdate = true;
  const [imageElement] = useState(() => {
    const _image = document.createElement("img");
    _image.crossOrigin = "Anonymous";
    return _image;
  });

  const handleStream = () => {
    SERVER.receive((data) => {
      let newFile = data;
      let base64 = "";
      let reader = new FileReader();
      reader.readAsDataURL(newFile);
      reader.onloadend = function () {
        base64 = reader.result as string;
        setFrameUrl(() => {
          return base64;
        });
        imageElement.src = base64;
        texture.needsUpdate = true;
      };
    });
  };

  useEffect(() => {
    SERVER.start();
    handleStream();
    //
    return () => {
      // SERVER.close();
    };
  });

  return (
    <>
      <group position={[0, -260, -280]} scale={150}>
        <mesh rotation={[0, Math.PI, 0]} position={[0, 2, 3]}>
          <planeGeometry args={[3.2, 1.9]} />
          <meshBasicMaterial attach="material" map={texture} />
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
  if (window.location.pathname === "/chat") return <Chat />;
  return (
    <>
      <VRButton />
      <Canvas
        camera={{
          // near: 0.1,
          // far: 100,
          position: [2, 6, 7],
        }}
      >
        <XR>
          <Controllers />
          <Hands />
          <OrbitControls
            maxPolarAngle={Math.PI / 2}
            minPolarAngle={0}
            minDistance={100}
            maxDistance={300}
          />
          <ambientLight intensity={0.1} color="#b9d5ff" />
          <directionalLight
            intensity={1.2}
            color="#b9d5ff"
            position={[-4, 5, 2]}
          />
          <Suspense fallback={<Theatre />}>
            <Theatre />
            <Controls />
            <Hall />
          </Suspense>
        </XR>
      </Canvas>
    </>
  );
}

export default App;
