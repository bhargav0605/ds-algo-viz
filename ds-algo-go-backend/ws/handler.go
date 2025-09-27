package ws

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/bhargav0605/ds-algo-go-backend/algo"
	"github.com/bhargav0605/ds-algo-go-backend/utils"
	"github.com/gorilla/websocket"
)

// def create_response(
//         event_type: str,
//         cmd: str,
//         sorting: str,
//         array: Optional[List[Any]] = None,
//         minSize: int = 0,
//         maxSize: int = 0,
//         minRange: int = 0,
//         maxRange: int = 0,
//         i: int = 0,
//         j: int = 0) -> Dict:
//     return {
//         "type": event_type,
//         "cmd": cmd,
//         "array": array,
//         "sorting": sorting,
//         "minSize": minSize,
//         "maxSize": maxSize,
//         "minRange": minRange,
//         "maxRange": maxRange,
//         "i": i,
//         "j": j,
//     }

// Upgrade HTTP to Websocket
var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

// Handler with switch case for the algorithms
func Handler(w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		http.Error(w, "upgrade failed", http.StatusBadGateway)
		return
	}
	defer conn.Close()

	_ = conn.SetReadDeadline(time.Now().Add(60 * time.Second))
	conn.SetPongHandler(func(string) error {
		_ = conn.SetReadDeadline(time.Now().Add(60 * time.Second))
		return nil
	})

	for {
		msgType, data, err := conn.ReadMessage()
		if err != nil {
			log.Printf("read: ", err)
			return
		}

		fmt.Print(msgType)

		var incoming utils.IncomingMessage
		if err := json.Unmarshal(data, &incoming); err != nil {
			log.Println("json parse error:", err)
			return
		}
		fmt.Print(incoming)

		SendEvent := func(msg any) {
			if err := conn.WriteJSON(msg); err != nil {
				log.Printf("write: ", err)
				return
			}
		}

		switch incoming.Sorting {
		case "bs":
			algo.Add(&incoming, SendEvent)
		}
		// log.Println("Parsed value:", incoming.Echo) // 👉 this will print "hello"
		// fmt.Printf(string(data))
		// response := utils.Echo{Echo: string(data)}

		// if msgType != websocket.TextMessage {
		// 	msgType = websocket.TextMessage
		// }

		// Create a function which can be passed to write
		// SendEvent := func(msg string) {
		// 	if err := conn.WriteJSON(msg); err != nil {
		// 		log.Printf("write: ", err)
		// 		return
		// 	}
		// }

		// SendEvent("Hello")
		// if err := conn.WriteJSON(response); err != nil {
		// 	log.Printf("write: ", err)
		// 	return
		// }
	}
}
