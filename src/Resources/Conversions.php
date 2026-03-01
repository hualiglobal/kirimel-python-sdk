<?php

declare(strict_types=1);

namespace KiriMel\Resources;

use KiriMel\HttpClient;

/**
 * Conversions resource client
 */
class Conversions
{
    private HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * List all conversion goals
     */
    public function list(): array
    {
        return $this->httpClient->get('conversions');
    }

    /**
     * Get single conversion goal
     */
    public function get(int $id): array
    {
        return $this->httpClient->get("conversions/{$id}");
    }

    /**
     * Create conversion goal
     */
    public function create(array $data): array
    {
        return $this->httpClient->post('conversions', $data);
    }

    /**
     * Update conversion goal
     */
    public function update(int $id, array $data): array
    {
        return $this->httpClient->post("conversions/{$id}", $data);
    }

    /**
     * Delete conversion goal
     */
    public function delete(int $id): array
    {
        return $this->httpClient->post("conversions/{$id}/delete");
    }

    /**
     * Track a conversion
     */
    public function track(array $data): array
    {
        return $this->httpClient->post('conversions/track', $data);
    }

    /**
     * Get conversions for a goal
     */
    public function conversions(int $id): array
    {
        return $this->httpClient->get("conversions/{$id}/conversions");
    }

    /**
     * Get ROI report
     */
    public function roi(): array
    {
        return $this->httpClient->get('conversions/roi');
    }

    /**
     * Get funnel analysis
     */
    public function funnel(int $id): array
    {
        return $this->httpClient->get("conversions/{$id}/funnel");
    }
}
