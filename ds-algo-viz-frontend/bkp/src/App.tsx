// src/App.tsx
import React, { useRef, useState, type JSX } from "react";
import { Stage, Layer, Rect, Text, Group } from "react-konva";
import Konva from "konva";

type Box = {
  id: number;
  value: number;
};

const BOX_SIZE = 70;
const GAP = 20;
const STAGE_PADDING = 40; // extra vertical/horizontal padding

export default function App(): JSX.Element {
  const initialValues = [5, 2, 8, 1, 7, 3];
  const [boxes, setBoxes] = useState<Box[]>(
    initialValues.map((v, i) => ({ id: i, value: v }))
  );

  // references to group nodes so we can set x/y directly during animation
  const groupRefs = useRef<(Konva.Group | null)[]>([]);
  const [isAnimating, setIsAnimating] = useState(false);

  // stage size responsive-ish: you can replace with window.innerWidth/Height if you want full page
  const STAGE_WIDTH = Math.max(600, boxes.length * (BOX_SIZE + GAP) + STAGE_PADDING * 2);
  const STAGE_HEIGHT = 300;

  // compute slot x positions centered
  const totalWidth = boxes.length * BOX_SIZE + (boxes.length - 1) * GAP;
  const startX = (STAGE_WIDTH - totalWidth) / 2;
  const startY = (STAGE_HEIGHT - BOX_SIZE) / 2;

  // utility to animate along a half-circle arc from start->end
  const animateAlongHalfCircle = (
    node: Konva.Group,
    fromX: number,
    toX: number,
    baseY: number,
    arcHeight: number,
    durationSec: number
  ) => {
    return new Promise<void>((resolve) => {
      const start = performance.now();
      const durationMs = durationSec * 1000;
      let rafId = 0;

      const step = (now: number) => {
        const elapsed = now - start;
        let t = Math.min(1, elapsed / durationMs); // 0..1
        // linear x
        const x = fromX + (toX - fromX) * t;
        // half circle using sine: y lifts up then comes down
        const y = baseY - Math.sin(Math.PI * t) * arcHeight;

        node.x(x);
        node.y(y);

        if (t < 1) {
          rafId = requestAnimationFrame(step);
        } else {
          // ensure final position
          node.x(toX);
          node.y(baseY);
          cancelAnimationFrame(rafId);
          resolve();
        }
      };

      rafId = requestAnimationFrame(step);
    });
  };

  // swap function that animates two groups along symmetric arcs
  const swapWithHalfCircle = async (i: number, j: number) => {
    if (isAnimating || i === j) return;
    setIsAnimating(true);

    // slot positions
    const slotAX = startX + i * (BOX_SIZE + GAP);
    const slotBX = startX + j * (BOX_SIZE + GAP);
    const slotY = startY;

    const nodeA = groupRefs.current[boxes[i].id];
    const nodeB = groupRefs.current[boxes[j].id];

    if (!nodeA || !nodeB) {
      // fallback: immediate swap in state
      setBoxes((prev) => {
        const next = [...prev];
        const tmp = next[i].value;
        next[i].value = next[j].value;
        next[j].value = tmp;
        return next;
      });
      setIsAnimating(false);
      return;
    }

    // arc height based on distance (so longer swaps have higher arc)
    const horizontalDistance = Math.abs(slotBX - slotAX);
    const arcHeight = Math.max(30, horizontalDistance / 2); // tweak as you like
    const duration = 0.6; // seconds

    // start both animations simultaneously; nodeA goes to slotBX, nodeB goes to slotAX
    await Promise.all([
      animateAlongHalfCircle(nodeA, slotAX, slotBX, slotY, arcHeight, duration),
      animateAlongHalfCircle(nodeB, slotBX, slotAX, slotY, arcHeight, duration),
    ]);

    // after animation finishes: swap values in state
    setBoxes((prev) => {
      const next = [...prev];
      const tmp = next[i].value;
      next[i].value = next[j].value;
      next[j].value = tmp;
      return next;
    });

    // reset groups to their slot positions (important so future animations start from correct place)
    nodeA.x(slotAX);
    nodeA.y(slotY);
    nodeB.x(slotBX);
    nodeB.y(slotY);

    setIsAnimating(false);
  };

  const swapRandom = () => {
    if (isAnimating) return;
    const n = boxes.length;
    let i = Math.floor(Math.random() * n);
    let j = Math.floor(Math.random() * n);
    while (j === i) j = Math.floor(Math.random() * n);
    swapWithHalfCircle(i, j);
  };

  const swapFirstTwo = () => swapWithHalfCircle(0, 1);

  return (
    <div style={{ textAlign: "center", padding: 12 }}>
      <h2>Konva — Swap along half-circle arc</h2>

      <div style={{ marginBottom: 12 }}>
        <button onClick={swapRandom} disabled={isAnimating} style={{ marginRight: 8 }}>
          Swap random
        </button>
        <button onClick={swapFirstTwo} disabled={isAnimating}>
          Swap first two
        </button>
        {isAnimating && <span style={{ marginLeft: 12 }}>Animating...</span>}
      </div>

      <Stage width={STAGE_WIDTH} height={STAGE_HEIGHT}>
        <Layer>
          {boxes.map((box, i) => {
            const slotX = startX + i * (BOX_SIZE + GAP);
            const slotY = startY;
            return (
              <Group
                key={box.id}
                x={slotX}
                y={slotY}
                ref={(el) => { groupRefs.current[box.id] = el as Konva.Group | null; }}
              >
                <Rect width={BOX_SIZE} height={BOX_SIZE} cornerRadius={8} shadowBlur={5} fill="skyblue" />
                <Text
                  x={BOX_SIZE / 2 - 8}
                  y={BOX_SIZE / 2 - 12}
                  text={String(box.value)}
                  fontSize={20}
                  fontStyle="bold"
                  fill="black"
                />
              </Group>
            );
          })}
        </Layer>
      </Stage>

      <div style={{ marginTop: 14 }}>
        <strong>Current array:</strong> {JSON.stringify(boxes.map((b) => b.value))}
      </div>
    </div>
  );
}
