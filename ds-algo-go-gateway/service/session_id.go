package service

import (
	"fmt"
	"time"
)

func GenerateStreamIdKey(userId, runId int) (string, string) {
	millis := time.Now().UnixMilli()
	uniquePart := fmt.Sprintf("%d%d", userId, runId)
	streamId := fmt.Sprintf("%d-%s", millis, uniquePart)
	streamKey := fmt.Sprintf("algo:{%d}:%d", userId, runId)
	return streamKey, streamId
}
