import React, { Suspense, useEffect, useRef, useState } from "react";
import { Canvas, useThree, useLoader, useFrame } from "@react-three/fiber";
import { VRButton, XR, Controllers, Hands, useXR, useController } from "@react-three/xr";
import { OrbitControls, PerspectiveCamera } from "@react-three/drei";
import * as THREE from "three";
import "./App.css";

// import Chat from "./pages/Chat";
import Hall from "./Hall";
import Avatar from "./Avatar";
// import Hall from "./Theatre";
import { SERVER } from "./infrastructure";
import { Box3 } from "three";
// import { logger } from "./common/logger";

const Theatre = ({ setPositions }: any) => {
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
    SERVER.receive((data) => {
      const jsonData = JSON.parse(data)
      if ( jsonData.type === "coordinates" ) {
        setPositions((prev: any) => {
          return [...jsonData.positions]
        })
      }
      setSeekTime(parseInt(data));
    });
  };

  useEffect(() => {
    SERVER.start();
    handleStream();
    const interval = setInterval(() => {
      // sending seektime from every client
      // but only the first clients seektime is synced with server
      SERVER.send({ seek: seekTime });
    }, 500);
    //
    return () => {
      clearInterval(interval)
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

const Avatars = ({ positions }: { positions: any}) => {
  const [avatars, setAvatars] = useState<any>()

  useEffect(() => {
    if (positions) {
      const temp = positions?.map((position: any, key: any) => {
        return <Avatar position={position} key={key} model={`/avatar/scene.gltf?randomId=${key}`} />;
      })
      setAvatars(temp)
    }
  }, [positions])
  
  return <>
    {avatars}
  </>
}

const Controls = () => {
  const { camera } = useThree();
  console.log({ position: camera.position })
  console.log(camera.position)

  // const handleKeyPress = (e: KeyboardEvent) => {
  //   switch (e.key) {
  //     case "w":
  //       camera.translateZ(-10);
  //       break;
  //     case "s":
  //       camera.translateZ(10);
  //       break;
  //     case "a":
  //       camera.translateX(10);
  //       break;
  //     case "d":
  //       camera.translateX(-10);
  //       break;
  //   }
  // };
  // useEffect(() => {
  //   document.addEventListener("keypress", handleKeyPress);

  //   return () => {
  //     document.removeEventListener("keypress", handleKeyPress);
  //   };
  // });

  return null;
};

const Controller = () => {
  const [paused, setPaused] = useState<boolean>(false);

  // console.log(c2.position)
  // console.log({ position: camera.position })
  // const [headset, setHeadset] = useState<any>({
  //   position: [0, 0, 0],
  //   quaternion: [0, 0, 0]
  // })
  // const headset = useController("none")
  // const rightController = useController("right")
  // const { controllers  } = useXR()
  // const { inputSource } = rightController



  useFrame(({ gl, camera }) => {
    if (gl.xr.getSession() !== null && !paused) {
      let vector = camera.position.clone()
      vector.applyMatrix4(camera.matrixWorld)
      // const vector3 = new THREE.Vector3();
      // const direction = camera.getWorldDirection(vector3)

      console.log("useFrame:", camera.position)
      // console.log({ position: camera.position })
      // console.log({ position: camera.position.toArray() })
      // console.log({ position: camera.position.y })
      setPaused(() => true)
    }
  });

  useEffect(() => {
    const interval = setInterval(() => {
      setPaused(() => false)
    }, 5000)

    return () => {
      clearInterval(interval)
    }
  }, [])
  
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

function Box(props: any) {
  const mesh = useRef() as any;
  useFrame(() => (mesh.current.rotation.x = mesh.current.rotation.y += 0.01));
  return (
     <mesh {...props} ref={mesh}>
        <boxGeometry args={[3, 3, 3]} />
        <meshStandardMaterial color={"orange"} />
     </mesh>
  );
}

function App() {
  const [avatarPositions, setAvatarPositions] = useState<any>([])

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
          // position: [0, 0, 0],
          manual: true
        }}
      >
        {/* <Avatar position={[0, 0, 0]} model={'/avatar/scene.gltf'} key={0} />
        <Avatar position={[0, 1, 0]} model={'/avatar/scene.gltf?randomId=5'} key={1} /> */}
        <XR>
          <PerspectiveCamera position={[0, 0, 0]} makeDefault manual />
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
          <Suspense fallback={<Theatre setPositions={setAvatarPositions} />}>
            <Avatars positions={avatarPositions} />
            {/* <Box position={[0, 0, 0]} />
            <Box position={[0, 5, 0]} />
            <Box position={[5, 0, 0]} /> */}

            {/* <Avatar position={[1, 0, 0]} key={2} /> */}
            <Theatre setPositions={setAvatarPositions} />
            <Controls />
            <Hall />
          </Suspense>
        </XR>
      </Canvas>
    </>
  );
}

export default App;
