/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
Command: npx gltfjsx@6.1.3 simple_theater_2.glb
*/

import { useGLTF } from "@react-three/drei";

export default function Model(props: any) {
  const { nodes, materials } = useGLTF("simple_theater_2.glb") as any;
  return (
    <group {...props} dispose={null}>
      <mesh
        geometry={nodes.Wall.geometry}
        material={materials.Wall}
        position={[0, 2.63, 0]}
        scale={[79.16, 59.37, 79.16]}
      >
        <mesh
          geometry={nodes.Chair_1001.geometry}
          material={materials.Wardrobe}
          position={[0.53, -0.83, 0.22]}
          rotation={[0, -0.03, 0]}
          scale={[0.25, 0.33, 0.25]}
        />
        <mesh
          geometry={nodes.Chair_1002.geometry}
          material={materials.Wardrobe}
          position={[0.2, -0.83, 0.22]}
          rotation={[0, -0.03, 0]}
          scale={[0.25, 0.33, 0.25]}
        />
        <mesh
          geometry={nodes.Chair_1003.geometry}
          material={materials.Wardrobe}
          position={[-0.22, -0.83, 0.22]}
          rotation={[0, -0.03, 0]}
          scale={[0.25, 0.33, 0.25]}
        />
        <mesh
          geometry={nodes.Chair_1004.geometry}
          material={materials.Wardrobe}
          position={[-0.63, -0.83, 0.22]}
          rotation={[0, -0.03, 0]}
          scale={[0.25, 0.33, 0.25]}
        />
        <mesh
          geometry={nodes.Chair_1005.geometry}
          material={materials.Wardrobe}
          position={[0.53, -0.83, -0.35]}
          rotation={[0, -0.03, 0]}
          scale={[0.25, 0.33, 0.25]}
        />
        <mesh
          geometry={nodes.Chair_1006.geometry}
          material={materials.Wardrobe}
          position={[0.2, -0.83, -0.35]}
          rotation={[0, -0.03, 0]}
          scale={[0.25, 0.33, 0.25]}
        />
        <mesh
          geometry={nodes.Chair_1007.geometry}
          material={materials.Wardrobe}
          position={[-0.22, -0.83, -0.35]}
          rotation={[0, -0.03, 0]}
          scale={[0.25, 0.33, 0.25]}
        />
        <mesh
          geometry={nodes.Chair_1008.geometry}
          material={materials.Wardrobe}
          position={[-0.63, -0.83, -0.35]}
          rotation={[0, -0.03, 0]}
          scale={[0.25, 0.33, 0.25]}
        />
        <mesh
          geometry={nodes.Floor.geometry}
          material={materials.Wall}
          position={[0, -0.88, 0]}
          scale={[1, 1.33, 1]}
        />
        <group position={[-0.07, -0.73, 1]} scale={[1.09, 1.46, 1.09]}>
          <mesh geometry={nodes.Cube021.geometry} material={materials.Black} />
          <mesh
            geometry={nodes.Cube021_1.geometry}
            material={materials.Screen}
          />
        </group>
        <mesh
          geometry={nodes.Wood_floor_1.geometry}
          material={materials.Floor}
          position={[0, -0.88, 0]}
          scale={[0.13, 1.33, 0.94]}
        />
      </mesh>
      <mesh geometry={nodes.Seat.geometry} material={materials.Blanket} />
      <mesh geometry={nodes.Carpet.geometry} material={materials.White} />
      <mesh geometry={nodes.Chair.geometry} material={materials.Wardrobe} />
      <group scale={[0.42, 0.04, 0.5]}>
        <mesh geometry={nodes.Cube029.geometry} material={materials.White} />
        <mesh
          geometry={nodes.Cube029_1.geometry}
          material={materials["Paint red"]}
        />
      </group>
      <mesh
        geometry={nodes.Wall_shelf.geometry}
        material={materials.Wardrobe}
      />
      <mesh
        geometry={nodes.Wall_bookshelf.geometry}
        material={materials.Wardrobe}
      />
      <mesh geometry={nodes.Wood_floor.geometry} material={materials.Floor} />
      <mesh geometry={nodes.Cube001.geometry} material={materials.Wardrobe} />
      <mesh geometry={nodes.Cube001_1.geometry} material={materials.White} />
      <mesh geometry={nodes.Cube001_2.geometry} material={materials.Blanket} />
      <mesh geometry={nodes.Cube032.geometry} material={materials.Wardrobe} />
      <mesh geometry={nodes.Cube032_1.geometry} material={materials.Handle} />
      <mesh geometry={nodes.Cube034.geometry} material={materials.Handle} />
      <mesh geometry={nodes.Cube034_1.geometry} material={materials.Wardrobe} />
      <mesh geometry={nodes.Cube034_2.geometry} material={materials.White} />
      <mesh geometry={nodes.Cube035.geometry} material={materials.Black} />
      <mesh geometry={nodes.Cube035_1.geometry} material={materials.Screen} />
      <mesh geometry={nodes.Cube036.geometry} material={materials.Black} />
      <mesh geometry={nodes.Cube036_1.geometry} material={materials.Screen} />
      <mesh geometry={nodes.Cube037.geometry} material={materials.White} />
      <mesh geometry={nodes.Cube037_1.geometry} material={materials.Wardrobe} />
      <mesh geometry={nodes.Cube037_2.geometry} material={materials.Handle} />
      <mesh geometry={nodes.Cube038.geometry} material={materials.Blanket} />
      <mesh geometry={nodes.Cube038_1.geometry} material={materials.Wardrobe} />
      <mesh geometry={nodes.Cube028.geometry} material={materials.White} />
      <mesh
        geometry={nodes.Cube028_1.geometry}
        material={materials["Paint green"]}
      />
      <mesh geometry={nodes.Cube030.geometry} material={materials.White} />
      <mesh
        geometry={nodes.Cube030_1.geometry}
        material={materials["Paint yellow"]}
      />
      <mesh geometry={nodes.Cube009.geometry} material={materials.White} />
      <mesh
        geometry={nodes.Cube009_1.geometry}
        material={materials["Book red"]}
      />
      <mesh
        geometry={nodes.Cube009_2.geometry}
        material={materials["Book yellow"]}
      />
      <mesh
        geometry={nodes.Cube009_3.geometry}
        material={materials["Book blue"]}
      />
      <mesh geometry={nodes.Cube004.geometry} material={materials.White} />
      <mesh
        geometry={nodes.Cube004_1.geometry}
        material={materials["Book red"]}
      />
      <mesh
        geometry={nodes.Cube004_2.geometry}
        material={materials["Book blue"]}
      />
      <mesh
        geometry={nodes.Cube004_3.geometry}
        material={materials["Book yellow"]}
      />
    </group>
  );
}

useGLTF.preload("simple_theater_2.glb");