import React, { useMemo } from "react";
import type { ServerResponse } from "../types";

type Props = {
  lastMessage?: ServerResponse;
};

export default function ArrayView({ lastMessage }: Props) {
  const { arr, highlight } = useMemo(() => {
    const arr = Array.isArray(lastMessage?.array) ? lastMessage!.array! : [];
    const cmd = lastMessage?.cmd;
    const i = typeof lastMessage?.i === "number" ? (lastMessage!.i as number) : -1;
    const j = typeof lastMessage?.j === "number" ? (lastMessage!.j as number) : -1;
    const kind = cmd === "compare" || cmd === "swap" ? cmd : null;
    return { arr, highlight: kind ? { kind, i, j } as const : null };
  }, [lastMessage]);

  const cls = (idx: number) => {
    if (!highlight) return "";
    const hit = idx === highlight.i || idx === highlight.j;
    if (!hit) return "";
    return highlight.kind === "compare" ? "bg-yellow-200 rounded px-1" : "bg-rose-200 rounded px-1";
  };

  return (
    <section>
      <p>
        {arr.length === 0
          ? "(empty)"
          : arr.map((n, idx) => (
              <React.Fragment key={idx}>
                <span className={cls(idx)}>{n}</span>
                {idx < arr.length - 1 && <span>, </span>}
              </React.Fragment>
            ))}
      </p>
    </section>
  );
}
