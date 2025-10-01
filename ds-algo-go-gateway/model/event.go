package model

type Event struct {
	Sorting   string `json:"sorting"`
	Array     []int  `json:"array"`
	StreamKey string `json:"stream_key"`
	StreamId  string `json:"stream_id"`
}
