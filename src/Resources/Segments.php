<?php

declare(strict_types=1);

namespace KiriMel\Resources;

use KiriMel\HttpClient;

/**
 * Segments resource client
 */
class Segments
{
    private HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * List segments for a list
     */
    public function list(int $listId): array
    {
        return $this->httpClient->get("lists/{$listId}/segments");
    }

    /**
     * Get single segment
     */
    public function get(int $id): array
    {
        return $this->httpClient->get("segments/{$id}");
    }

    /**
     * Create segment
     */
    public function create(int $listId, array $data): array
    {
        return $this->httpClient->post("lists/{$listId}/segments", $data);
    }

    /**
     * Update segment
     */
    public function update(int $id, array $data): array
    {
        return $this->httpClient->post("segments/{$id}", $data);
    }

    /**
     * Delete segment
     */
    public function delete(int $id): array
    {
        return $this->httpClient->post("segments/{$id}/delete");
    }

    /**
     * Preview segment (without saving)
     */
    public function preview(int $listId, array $conditions): array
    {
        return $this->httpClient->post("lists/{$listId}/segments/preview", [
            'conditions' => $conditions
        ]);
    }

    /**
     * Get segment subscribers
     */
    public function subscribers(int $id, array $params = []): array
    {
        return $this->httpClient->get("segments/{$id}/subscribers", $params);
    }

    /**
     * Refresh segment count
     */
    public function refresh(int $id): array
    {
        return $this->httpClient->post("segments/{$id}/refresh");
    }

    /**
     * Get segment build logs
     */
    public function logs(int $id): array
    {
        return $this->httpClient->get("segments/{$id}/logs");
    }

    /**
     * Get segment templates
     */
    public function templates(): array
    {
        return $this->httpClient->get('segments/templates');
    }

    /**
     * Get available fields
     */
    public function fields(): array
    {
        return $this->httpClient->get('segments/fields');
    }
}
