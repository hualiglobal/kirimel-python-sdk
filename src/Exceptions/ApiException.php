<?php

declare(strict_types=1);

namespace KiriMel\Exceptions;

/**
 * Base API exception
 */
class ApiException extends \Exception
{
    protected ?string $errorType = null;
    protected ?array $errors = null;
    protected ?int $statusCode = null;

    public function __construct(
        string $message = '',
        int $code = 0,
        ?int $statusCode = null,
        ?array $errors = null
    ) {
        parent::__construct($message, $code);
        $this->statusCode = $statusCode;
        $this->errors = $errors;
    }

    public function getStatusCode(): ?int
    {
        return $this->statusCode;
    }

    public function getErrors(): ?array
    {
        return $this->errors;
    }

    public function getErrorType(): ?string
    {
        return $this->errorType;
    }
}
