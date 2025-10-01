package httpclient

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"time"

	"github.com/bhargav0605/ds-algo-go-gateway/model"
)

func PostEvent(url string, evt model.Event) error {
	// fmt.Println(evt)
	jsonData, err := json.Marshal(evt)
	fmt.Println("📦 Request Body (raw):", string(jsonData))
	if err != nil {
		return fmt.Errorf("failed to marshal event: %w", err)
	}

	client := &http.Client{
		Timeout: 5 * time.Second,
	}

	// Send POST request
	resp, err := client.Post(url, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		return fmt.Errorf("failed to send POST request: %w", err)
	}
	defer resp.Body.Close()

	// Read response
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return fmt.Errorf("failed to read response body: %w", err)
	}

	fmt.Println("Status:", resp.Status)
	fmt.Println("Response:", string(body))

	if resp.StatusCode >= 300 {
		return fmt.Errorf("server returned non-2xx status: %s", resp.Status)
	}

	return nil
}
