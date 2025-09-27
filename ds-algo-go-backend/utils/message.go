package utils

type IncomingMessage struct {
	EventType string `json:"type"`
	Command   string `json:"cmd"`
	Array     []any  `json:"array"`
	Sorting   string `json:"sorting"`
	MinSize   int    `json:"minSize"`
	MaxSize   int    `json:"maxSize"`
	MinRange  int    `json:"minRange"`
	MaxRange  int    `json:"maxRange"`
	I         int    `json:"j"`
	J         int    `json:"i"`
}
