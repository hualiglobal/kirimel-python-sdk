<?php

declare(strict_types=1);

namespace KiriMel\Resources;

use KiriMel\HttpClient;

/**
 * Workflows resource client
 */
class Workflows
{
    private HttpClient $httpClient;

    public function __construct(HttpClient $httpClient)
    {
        $this->httpClient = $httpClient;
    }

    /**
     * List all workflows
     */
    public function list(): array
    {
        return $this->httpClient->get('workflows');
    }

    /**
     * Get single workflow
     */
    public function get(int $id): array
    {
        return $this->httpClient->get("workflows/{$id}");
    }

    /**
     * Create workflow
     */
    public function create(array $data): array
    {
        return $this->httpClient->post('workflows', $data);
    }

    /**
     * Update workflow
     */
    public function update(int $id, array $data): array
    {
        return $this->httpClient->post("workflows/{$id}", $data);
    }

    /**
     * Delete workflow
     */
    public function delete(int $id): array
    {
        return $this->httpClient->post("workflows/{$id}/delete");
    }

    /**
     * Duplicate workflow
     */
    public function duplicate(int $id): array
    {
        return $this->httpClient->post("workflows/{$id}/duplicate");
    }

    /**
     * Activate workflow
     */
    public function activate(int $id): array
    {
        return $this->httpClient->post("workflows/{$id}/activate");
    }

    /**
     * Pause workflow
     */
    public function pause(int $id): array
    {
        return $this->httpClient->post("workflows/{$id}/pause");
    }

    /**
     * Validate workflow
     */
    public function validate(int $id): array
    {
        return $this->httpClient->post("workflows/{$id}/validate");
    }

    /**
     * Get workflow executions
     */
    public function executions(int $id): array
    {
        return $this->httpClient->get("workflows/{$id}/executions");
    }

    /**
     * Get workflow templates
     */
    public function templates(): array
    {
        return $this->httpClient->get('workflows/templates');
    }

    /**
     * Create workflow from template
     */
    public function fromTemplate(int $templateId): array
    {
        return $this->httpClient->post('workflows/from-template', [
            'template_id' => $templateId
        ]);
    }

    /**
     * Get available node types
     */
    public function nodeTypes(): array
    {
        return $this->httpClient->get('workflows/node-types');
    }

    /**
     * Get workflow data
     */
    public function getData(int $id): array
    {
        return $this->httpClient->get("workflows/{$id}/data");
    }
}
