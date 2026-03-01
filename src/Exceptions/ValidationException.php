<?php

declare(strict_types=1);

namespace KiriMel\Exceptions;

/**
 * Validation exception (422)
 */
class ValidationException extends ApiException
{
    protected ?string $errorType = 'validation_error';
}
