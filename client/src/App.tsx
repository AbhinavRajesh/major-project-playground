import React, { Suspense, useEffect, useState } from "react";
import { Canvas, useThree, useLoader } from "@react-three/fiber";
import { VRButton, XR, Controllers, Hands } from "@react-three/xr";
import { OrbitControls } from "@react-three/drei";
import * as THREE from "three";
import "./App.css";

// import Chat from "./pages/Chat";
import Hall from "./Hall";
// import Hall from "./Theatre";
import { SERVER } from "./infrastructure";
// import { logger } from "./common/logger";

const Theatre = () => {
  const [frameUrl, setFrameUrl] = useState<string>(
    "https://st2.depositphotos.com/6797658/10299/v/950/depositphotos_102990436-stock-illustration-happy-pathers-day-love-dady.jpg"
  );
  const [seekTime, setSeekTime] = useState(0);
  const texture = useLoader(THREE.TextureLoader, frameUrl);
  texture.needsUpdate = true;
  const [imageElement] = useState(() => {
    const _image = document.createElement("img");
    _image.crossOrigin = "Anonymous";
    return _image;
  });

  const handleStream = () => {
    console.log("yee");
    SERVER.receive((data) => {
      setSeekTime(parseInt(data));
    });
  };

  useEffect(() => {
    SERVER.start();
    handleStream();
    setInterval(() => {
      // sending seektime from every client
      // but only the first clients seektime is synced with server
      SERVER.send({ seek: seekTime });
    }, 500);
    //
    return () => {
      // SERVER.close();
    };
  });

  return (
    <>
      <group position={[0, -11, 10]} scale={10}>
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

const Controller = () => {
  // const rightController= useController("right") as XRController
  // const { inputSource } = rightController

  // logger.send(JSON.stringify(inputSource))
  return null;

  // useFrame(() => {
  //   if (!rightController) return;
  //   const { grip: controller } = rightController;

  // })
  // const { camera } = useThree();

  // useEffect(() => {
  //   function handleControllerInput(event: any) {
  //     const gamepad = event.gamepad;
  //     const x = gamepad.axes[0];
  //     const y = gamepad.axes[1];
  //     camera.position.x = x;
  //     camera.position.y = y;
  //   }

  //   window.addEventListener("gamepadconnected", handleControllerInput);
  //   return () =>
  //     window.removeEventListener("gamepadconnected", handleControllerInput);
  // }, []);

  // return null;
};

function App() {
  // useEffect(() => {
  //   function handleControllerInput(event: any) {
  //     const gamepad = event.gamepad;
  //     const x = gamepad.axes[0];
  //     const y = gamepad.axes[1];
  //     SERVER.send(JSON.stringify({x, y}))
  //   }

  //   window.addEventListener("gamepadconnected", handleControllerInput);
  //   return () =>
  //     window.removeEventListener("gamepadconnected", handleControllerInput);
  // }, []);

  // if (window.location.pathname === "/chat") return <Chat />;

  return (
    <>
      <VRButton />
      <Canvas
        camera={{
          // near: 0.1,
          // far: 100,
          position: [0, 0, 0],
        }}
      >
        <XR>
          <Controllers />
          <Controller />
          <Hands />
          <OrbitControls
            maxPolarAngle={Math.PI / 2}
            minPolarAngle={0}
            minDistance={10}
            maxDistance={30}
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
