<?php

declare(strict_types=1);

namespace KiriMel\Resources;

use KiriMel\HttpClient;

/**
 * Forms resource client
 */
class Forms
{
    private HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * List all forms
     */
    public function list(): array
    {
        return $this->httpClient->get('forms');
    }

    /**
     * Get single form
     */
    public function get(int $id): array
    {
        return $this->httpClient->get("forms/{$id}");
    }

    /**
     * Create form
     */
    public function create(array $data): array
    {
        return $this->httpClient->post('forms', $data);
    }

    /**
     * Update form
     */
    public function update(int $id, array $data): array
    {
        return $this->httpClient->post("forms/{$id}", $data);
    }

    /**
     * Delete form
     */
    public function delete(int $id): array
    {
        return $this->httpClient->post("forms/{$id}/delete");
    }

    /**
     * Duplicate form
     */
    public function duplicate(int $id): array
    {
        return $this->httpClient->post("forms/{$id}/duplicate");
    }

    /**
     * Get form analytics
     */
    public function analytics(int $id): array
    {
        return $this->httpClient->get("forms/{$id}/analytics");
    }

    /**
     * Get form submissions
     */
    public function submissions(int $id, array $params = []): array
    {
        return $this->httpClient->get("forms/{$id}/submissions", $params);
    }

    /**
     * Get embed code
     */
    public function embed(int $id): array
    {
        return $this->httpClient->get("forms/{$id}/embed");
    }
}
