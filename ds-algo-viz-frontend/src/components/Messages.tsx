import type { ServerResponse } from "../types";

type Props = {
  messages: ServerResponse[];
};

export default function Messages({ messages }: Props) {
  return (
    <section className="bg-white rounded-2xl shadow-sm p-4">
      <h2 className="text-lg font-semibold mb-3">Server Messages</h2>
      <div className="grid gap-3 max-h-[50vh] overflow-auto pr-1">
        {messages.length === 0 && (
          <p className="text-sm text-gray-500">(No messages yet)</p>
        )}
        {messages.map((m, idx) => (
          <div key={idx} className="rounded-xl border border-gray-200 p-3 bg-gray-50">
            <div className="text-xs text-gray-500 mb-1">#{idx + 1}</div>
            <pre className="text-sm whitespace-pre-wrap break-words">{JSON.stringify(m, null, 2)}</pre>
          </div>
        ))}
      </div>
    </section>
  );
}
