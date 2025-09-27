package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/bhargav0605/ds-algo-go-backend/ws"
)

func main() {
	fmt.Println("hello")

	http.HandleFunc("/", ws.Handler)

	// http.HandleFunc("/")

	log.Println("Listening on 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
