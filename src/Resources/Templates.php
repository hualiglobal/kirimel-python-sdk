<?php

declare(strict_types=1);

namespace KiriMel\Resources;

use KiriMel\HttpClient;

/**
 * Templates resource client
 */
class Templates
{
    private HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * List all templates
     */
    public function list(array $params = []): array
    {
        return $this->httpClient->get('templates', $params);
    }

    /**
     * Get single template
     */
    public function get(int $id): array
    {
        return $this->httpClient->get("templates/{$id}");
    }

    /**
     * Create template
     */
    public function create(array $data): array
    {
        return $this->httpClient->post('templates', $data);
    }

    /**
     * Update template
     */
    public function update(int $id, array $data): array
    {
        return $this->httpClient->post("templates/{$id}", $data);
    }

    /**
     * Delete template
     */
    public function delete(int $id): array
    {
        return $this->httpClient->post("templates/{$id}/delete");
    }

    /**
     * Duplicate template
     */
    public function duplicate(int $id): array
    {
        return $this->httpClient->post("templates/{$id}/duplicate");
    }

    /**
     * Get templates by category
     */
    public function byCategory(string $category): array
    {
        return $this->httpClient->get("templates/category/{$category}");
    }

    /**
     * Search templates
     */
    public function search(string $query): array
    {
        return $this->httpClient->get('templates/search', ['q' => $query]);
    }

    /**
     * Get categories
     */
    public function categories(): array
    {
        return $this->httpClient->get('templates/categories');
    }
}
