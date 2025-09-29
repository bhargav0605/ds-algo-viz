import { useCallback, useEffect, useRef, useState } from "react";
import type { ServerResponse } from "../types";

export function useWebSocket(initialUrl: string) {
  const [url, setUrl] = useState(initialUrl);
  const wsRef = useRef<WebSocket | null>(null);
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<ServerResponse[]>([]);
  const [error, setError] = useState<string | null>(null);

  const connect = useCallback(() => {
    const exist = wsRef.current;
    if (exist && (exist.readyState === WebSocket.OPEN || exist.readyState === WebSocket.CONNECTING)) {
      return;
    }
    try {
      const ws = new WebSocket(url);
      wsRef.current = ws;

      ws.onopen = () => {
        setIsOpen(true);
        setError(null);
      };

      ws.onmessage = async (evt) => {
        try {
          const raw = evt.data instanceof Blob ? await evt.data.text() : String(evt.data);
          const parsed = JSON.parse(raw) as ServerResponse;
          setMessages((prev) => [...prev, parsed]);
        } catch {
          // non-JSON payload; keep for debugging
          setMessages((prev) => [
            ...prev,
            { type: "text", cmd: "message", data: evt.data } as unknown as ServerResponse,
          ]);
        }
      };

      ws.onerror = () => setError("WebSocket error (check server URL/origin)");
      ws.onclose = () => setIsOpen(false);
    } catch (e: any) {
      setError(e?.message ?? String(e));
    }
  }, [url]);

  const disconnect = useCallback(() => {
    const ws = wsRef.current;
    if (!ws) return;
    try { ws.close(); } catch {}
    wsRef.current = null;
    setIsOpen(false);
  }, []);

  const sendJson = useCallback((payload: unknown) => {
    const ws = wsRef.current;
    if (!ws || ws.readyState !== WebSocket.OPEN) return false;
    ws.send(JSON.stringify(payload));
    return true;
  }, []);

  // cleanup on unmount
  useEffect(() => {
    return () => {
      if (wsRef.current) {
        try { wsRef.current.close(); } catch {}
        wsRef.current = null;
      }
    };
  }, []);

  const lastMessage = messages[messages.length - 1];

  return {
    // state
    url, setUrl,
    isOpen, error,
    messages, lastMessage,
    // actions
    connect, disconnect, sendJson,
  };
}
