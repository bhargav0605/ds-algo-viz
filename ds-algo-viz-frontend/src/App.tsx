import { useMemo } from "react";
import { useWebSocket } from "./ws/useWebSocket";
import type { RandomRequest } from "./types";
import Controls from "./components/Controls";
import ArrayView from "./components/ArrayView";
import Messages from "./components/Messages";

export default function App() {
  const {
    url, setUrl,
    isOpen, error,
    messages, lastMessage,
    connect, disconnect, sendJson,
  } = useWebSocket("ws://localhost:8765/");

  // Your exact payload
  const randomPayload: RandomRequest = useMemo(() => ({
    type: "random",
    cmd: "generate",
    minSize: 1,
    maxSize: 5,
    minRange: 5,
    maxRange: 500,
    sorting: "bs",
  }), []);

  const onRandom = () => {
    sendJson(randomPayload);
  };

  return (
    <div className="min-h-screen bg-gray-50 text-gray-900 p-6">
      <div className="max-w-4xl mx-auto space-y-6">
        <header className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-3">
          <div>
            <h1 className="text-2xl font-bold">React ↔ WebSocket Client</h1>
            <p className="text-sm text-gray-600">
              Send <code>random</code> request and render the latest array; highlight compares/swaps; keep raw messages.
            </p>
          </div>
          <div className="flex items-center gap-2">
            <span className={`inline-flex items-center rounded-full px-3 py-1 text-sm font-medium ${isOpen ? "bg-green-100 text-green-700" : "bg-red-100 text-red-700"}`}>
              {isOpen ? "Connected" : "Disconnected"}
            </span>
          </div>
        </header>

        <Controls
          url={url}
          setUrl={setUrl}
          isOpen={isOpen}
          connect={connect}
          disconnect={disconnect}
          onRandom={onRandom}
          randomPayloadPreview={JSON.stringify(randomPayload)}
          error={error}
        />

        {/* Latest array (with commas) and highlighting of i/j on compare/swap */}
        <ArrayView lastMessage={lastMessage} />

        {/* Debug list of all server frames */}
        <Messages messages={messages} />

        <footer className="text-xs text-gray-500">
          Tip: Use <code>wss://</code> when your app is served over HTTPS.
        </footer>
      </div>
    </div>
  );
}
