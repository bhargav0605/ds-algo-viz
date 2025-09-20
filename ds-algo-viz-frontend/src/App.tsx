// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css';
import React from 'react';
import { Stage, Layer, Rect, Circle, Text } from 'react-konva';

function App() {
  const socket = new WebSocket("ws://localhost:8080")
  // const [count, setCount] = useState(0)

  return (
    <Stage width={window.innerWidth} height={window.innerHeight}>
      <Layer>
        <Text text="Try to drag shapes" fontSize={15} />
        <Rect
          x={20}
          y={50}
          width={100}
          height={100}
          fill="red"
          shadowBlur={10}
          // draggable
        />
        <Circle
          x={200}
          y={100}
          radius={50}
          fill="green"
          draggable
        />
      </Layer>
    </Stage>
  );
};

export default App
