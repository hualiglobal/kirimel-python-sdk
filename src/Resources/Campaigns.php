<?php

declare(strict_types=1);

namespace KiriMel\Resources;

use KiriMel\HttpClient;

/**
 * Campaigns resource client
 */
class Campaigns
{
    private HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * List campaigns
     */
    public function list(array $params = []): array
    {
        return $this->httpClient->get('campaigns', $params);
    }

    /**
     * Get recent campaigns
     */
    public function recent(): array
    {
        return $this->httpClient->get('campaigns/recent');
    }

    /**
     * Get single campaign
     */
    public function get(int $id): array
    {
        return $this->httpClient->get("campaigns/{$id}");
    }

    /**
     * Create campaign
     */
    public function create(array $data): array
    {
        return $this->httpClient->post('campaigns', $data);
    }

    /**
     * Update campaign
     */
    public function update(int $id, array $data): array
    {
        return $this->httpClient->post("campaigns/{$id}", $data);
    }

    /**
     * Delete campaign
     */
    public function delete(int $id): array
    {
        return $this->httpClient->post("campaigns/{$id}/delete");
    }

    /**
     * Duplicate campaign
     */
    public function duplicate(int $id): array
    {
        return $this->httpClient->post("campaigns/{$id}/duplicate");
    }

    /**
     * Schedule campaign
     */
    public function schedule(int $id, string $scheduledAt): array
    {
        return $this->httpClient->post("campaigns/{$id}/schedule", [
            'scheduled_at' => $scheduledAt
        ]);
    }

    /**
     * Pause campaign
     */
    public function pause(int $id): array
    {
        return $this->httpClient->post("campaigns/{$id}/pause");
    }

    /**
     * Resume campaign
     */
    public function resume(int $id): array
    {
        return $this->httpClient->post("campaigns/{$id}/resume");
    }

    /**
     * Get campaign statistics
     */
    public function stats(int $id): array
    {
        return $this->httpClient->get("campaigns/{$id}/stats");
    }
}
