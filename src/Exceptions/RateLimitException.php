<?php

declare(strict_types=1);

namespace KiriMel\Exceptions;

/**
 * Rate limit exception (429)
 */
class RateLimitException extends ApiException
{
    protected ?string $errorType = 'rate_limit_error';
    private ?int $retryAfter = null;

    public function __construct(
        string $message = '',
        int $code = 0,
        ?int $statusCode = null,
        ?array $errors = null,
        ?int $retryAfter = null
    ) {
        parent::__construct($message, $code, $statusCode, $errors);
        $this->retryAfter = $retryAfter;
    }

    public function getRetryAfter(): ?int
    {
        return $this->retryAfter;
    }
}
