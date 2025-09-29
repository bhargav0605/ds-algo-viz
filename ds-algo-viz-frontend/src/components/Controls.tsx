import React from "react";

type Props = {
  url: string;
  setUrl: (v: string) => void;
  isOpen: boolean;
  connect: () => void;
  disconnect: () => void;
  onRandom: () => void;
  randomPayloadPreview: string;
  error?: string | null;
};

export default function Controls({
  url, setUrl, isOpen, connect, disconnect, onRandom, randomPayloadPreview, error,
}: Props) {
  return (
    <>
      <section className="bg-white rounded-2xl shadow-sm p-4 grid gap-3">
        <label className="text-sm font-medium" htmlFor="wsurl">WebSocket URL</label>
        <div className="flex gap-2">
          <input
            id="wsurl"
            className="flex-1 rounded-xl border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="ws://localhost:8080/ws"
          />
          {!isOpen ? (
            <button onClick={connect} className="rounded-xl px-4 py-2 bg-blue-600 text-white hover:bg-blue-700">
              Connect
            </button>
          ) : (
            <button onClick={disconnect} className="rounded-xl px-4 py-2 bg-gray-700 text-white hover:bg-gray-800">
              Disconnect
            </button>
          )}
        </div>
        {error && <p className="text-sm text-red-600">{error}</p>}
      </section>

      <section className="bg-white rounded-2xl shadow-sm p-4">
        <h2 className="text-lg font-semibold mb-3">Actions</h2>
        <div className="flex gap-2">
          <button
            onClick={onRandom}
            disabled={!isOpen}
            className={`rounded-xl px-4 py-2 ${isOpen ? "bg-emerald-600 hover:bg-emerald-700" : "bg-emerald-300"} text-white`}
          >
            Random
          </button>
          <button disabled title="Coming soon" className="rounded-xl px-4 py-2 bg-gray-300 text-gray-700">
            Define (coming soon)
          </button>
        </div>
        <p className="text-xs text-gray-500 mt-2">Sending payload: <code>{randomPayloadPreview}</code></p>
      </section>
    </>
  );
}
