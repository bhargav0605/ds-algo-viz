package main

import (
	"fmt"
	"log"

	"github.com/bhargav0605/ds-algo-go-gateway/httpclient"
	"github.com/bhargav0605/ds-algo-go-gateway/model"
	"github.com/bhargav0605/ds-algo-go-gateway/service"
)

/*
ToDo:
1. Array should be generated from the frontend side.
2. based on sorting algorithm used I need to send request to that group of IP address pool only.
3. User ID and run ID generation is also needs to get happend.
*/
func main() {
	fmt.Println("hello gateway")

	userId := 111111
	runId := 222222

	streamKey, streamId := service.GenerateStreamIdKey(userId, runId)

	// This data should be from the websocket (sorting, array)
	event := model.Event{
		Sorting:   "bs",
		Array:     []int{5, 4, 3, 2},
		StreamKey: streamKey,
		StreamId:  streamId,
	}

	// Here I need to add try catch for the specific worker node for that specific sorting IP pool.
	url := "http://localhost:8000/event"

	if err := httpclient.PostEvent(url, event); err != nil {
		log.Fatalf("failed to send event: %v", err)
	}

	fmt.Println("✅ Event successfully sent!")

}
