package algo

import (
	"fmt"

	"github.com/bhargav0605/ds-algo-go-backend/utils"
)

// A simple struct for JSON response
type Message struct {
	Event string `json:"event"`
	Data  string `json:"data"`
}

func Add(msg *utils.IncomingMessage, sendEvent func(any)) {
	fmt.Println(msg.EventType)

	// message := Message{
	// 	Event: msg.EventType,
	// 	Data:  "Hello from Go 👋",
	// }

	// Consrtruct JSON here and send it
	msgg := utils.IncomingMessage{
		EventType: msg.EventType,
	}
	sendEvent(msgg)
}
