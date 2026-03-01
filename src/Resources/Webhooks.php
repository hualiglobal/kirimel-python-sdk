<?php

declare(strict_types=1);

namespace KiriMel\Resources;

use KiriMel\HttpClient;

/**
 * Webhooks resource client
 */
class Webhooks
{
    private HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * List all webhooks
     */
    public function list(array $params = []): array
    {
        return $this->httpClient->get('webhooks', $params);
    }

    /**
     * Get single webhook
     */
    public function get(int $id): array
    {
        return $this->httpClient->get("webhooks/{$id}");
    }

    /**
     * Create webhook
     */
    public function create(array $data): array
    {
        return $this->httpClient->post('webhooks', $data);
    }

    /**
     * Update webhook
     */
    public function update(int $id, array $data): array
    {
        return $this->httpClient->post("webhooks/{$id}", $data);
    }

    /**
     * Delete webhook
     */
    public function delete(int $id): array
    {
        return $this->httpClient->delete("webhooks/{$id}");
    }

    /**
     * Test webhook
     */
    public function test(int $id): array
    {
        return $this->httpClient->post("webhooks/{$id}/test");
    }

    /**
     * Get webhook logs
     */
    public function logs(int $id): array
    {
        return $this->httpClient->get("webhooks/{$id}/logs");
    }

    /**
     * Get supported webhook events
     */
    public function events(): array
    {
        return $this->httpClient->get('webhooks/events');
    }

    /**
     * Regenerate webhook secret
     */
    public function regenerateSecret(int $id): array
    {
        return $this->httpClient->post("webhooks/{$id}/secret/regenerate");
    }
}
