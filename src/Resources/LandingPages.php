<?php

declare(strict_types=1);

namespace KiriMel\Resources;

use KiriMel\HttpClient;

/**
 * Landing Pages resource client
 */
class LandingPages
{
    private HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * List all landing pages
     */
    public function list(): array
    {
        return $this->httpClient->get('landing-pages');
    }

    /**
     * Get single landing page
     */
    public function get(int $id): array
    {
        return $this->httpClient->get("landing-pages/{$id}");
    }

    /**
     * Create landing page
     */
    public function create(array $data): array
    {
        return $this->httpClient->post('landing-pages', $data);
    }

    /**
     * Update landing page
     */
    public function update(int $id, array $data): array
    {
        return $this->httpClient->post("landing-pages/{$id}", $data);
    }

    /**
     * Delete landing page
     */
    public function delete(int $id): array
    {
        return $this->httpClient->post("landing-pages/{$id}/delete");
    }

    /**
     * Duplicate landing page
     */
    public function duplicate(int $id): array
    {
        return $this->httpClient->post("landing-pages/{$id}/duplicate");
    }

    /**
     * Publish landing page
     */
    public function publish(int $id): array
    {
        return $this->httpClient->post("landing-pages/{$id}/publish");
    }

    /**
     * Unpublish landing page
     */
    public function unpublish(int $id): array
    {
        return $this->httpClient->post("landing-pages/{$id}/unpublish");
    }

    /**
     * Get landing page analytics
     */
    public function analytics(int $id): array
    {
        return $this->httpClient->get("landing-pages/{$id}/analytics");
    }

    /**
     * Get templates
     */
    public function templates(): array
    {
        return $this->httpClient->get('landing-pages/templates');
    }
}
